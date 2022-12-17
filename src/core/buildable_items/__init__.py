from dataclasses import dataclass
import datetime
import math

from pydantic import BaseModel

from core.experience_points import GivePlanetExperienceRequest, ExperiencePoints, GiveUserExperienceRequest
from core.shared.models import (
    AppBaseException,
    BuildableItem,
    NoPlanetFoundException,
    Planet,
    QueueIsFullException, BuildingQueueItem, BuildableItemState,
)
from core.shared.ports import PlanetRepositoryPort, ResponsePort
from core.shared.service.buildable_items import is_queue_full
from core.shared.service.tier_benefit import tier_benefit_buildable_items
from core.shared.static.game_data.Common import (
    BuildableItemBaseType,
    BuildableItemLevelInfo,
)
from core.shared.static.game_data.DefenseData import DefenseData
from core.shared.static.game_data.GameData import GameData
from core.shared.static.game_data.GameDataFactory import game_data_factory
from core.shared.static.game_data.InstallationData import InstallationData
from core.shared.static.game_data.ResearchData import ResearchData
from core.shared.static.game_data.ResourceData import ResourceData


class FinishBuildRequest(BaseModel):
    planet_id: str


class PayToClearQueueRequest(BaseModel):
    planet_id: str


class BuildableRequest(BaseModel):
    type: str
    label: str
    planet_id: str
    quantity: int = None


class ClearQueuePaidResponse(BaseModel):
    total_cost: float


class BuildableResponse(BuildableItem):
    queue_item_info: BuildingQueueItem = None
    metal_paid: float = None
    crystal_paid: float = None
    petrol_paid: float = None

    @staticmethod
    def from_buildable_item(item: BuildableItem):
        return BuildableResponse(
            label=item.label,
            type=item.type,
            current_level=item.current_level,
            building=item.building,
            finish=item.finish,
            repairing=item.repairing,
            health=item.health,
            quantity=item.quantity,
            quantity_building=item.quantity_building,
        )


class CantClearQueueNotFundsException(AppBaseException):
    msg = "Can't clear queue, not enough $BKM"


class WrongBuildableException(AppBaseException):
    msg = "Wrong type, label or quantity for the building element/s..."


class CantBuildOrRepairException(AppBaseException):
    msg = "Can't upgrade, already upgrading/repairing..."


class CantBuildSlotsFullException(AppBaseException):
    msg = "Can't build, no more space in your planet, please research terraforming..."


class NotEnoughFundsForBuildException(AppBaseException):
    msg = "Can't build, not enough funds to cover building costs..."


class CantUpgradeIfHealthIsNotFullException(AppBaseException):
    msg = "Cant upgrade if health is not 100%, please repair before."


class CantRepairIfHealthIsFullException(AppBaseException):
    msg = "Cant upgrade if health full."


@dataclass
class BuildableItems:
    planet_repository_port: PlanetRepositoryPort
    planet_level_use_case: ExperiencePoints
    response_port: ResponsePort

    async def _update_item_state(self, planet, item, queue):
        game_data: GameData = game_data_factory[item.type]
        last_update_field_names = {
            ResourceData.METAL_MINE: "metal_last_updated",
            ResourceData.CRYSTAL_MINE: "crystal_last_updated",
            ResourceData.PETROL_MINE: "petrol_last_updated",
        }

        if item.state == BuildableItemState.BUILDING:

            if item.type in [
                ResourceData.TYPE,
                InstallationData.TYPE,
                ResearchData.TYPE,
            ]:
                item.current_level += 1

            if item.type in [ResourceData.TYPE]:
                if item.label in last_update_field_names:
                    setattr(
                        planet.resources,
                        last_update_field_names[item.label],
                        item.finish,
                    )

                item.health = (
                    game_data.get_item(item.label)
                    .get_level_info(item.current_level)
                    .health
                )

            if item.type in [InstallationData.TYPE, ResourceData.TYPE]:
                planet.slots_used += 1

            if item.type in [ResearchData.TYPE]:
                if item.label == ResearchData.TERRAFORMING:
                    planet.slots += 1

            if item.type in [DefenseData.TYPE]:
                data = game_data.get_item(item.label).get_level_info(0)
                new_health = item.quantity * data.health

                item.quantity += item.quantity_building
                item.quantity_building = 0
                item.health += new_health

            item.finish = None
            item.building = False
            item.state = BuildableItemState.FINISHED
            planet.building_queue.items = queue

        elif item.state == BuildableItemState.REPAIRING:
            info = game_data.get_item(item.label).get_level_info(item.current_level)
            if item.label in last_update_field_names:
                setattr(
                    planet.resources,
                    last_update_field_names[item.label],
                    item.finish,
                )

            item.health = info.health
            item.repairing = False
            item.finish = None
            item.state = BuildableItemState.FINISHED
            planet.building_queue.items = queue

    async def pay_to_clear_queue(self, user: str, request: PayToClearQueueRequest) -> ClearQueuePaidResponse:
        planet: Planet = await self.planet_repository_port.get(request.planet_id)
        if planet is None:
            raise NoPlanetFoundException()

        queue: list[BuildingQueueItem] = planet.building_queue.items
        buildable_item_queue = []

        now = datetime.datetime.timestamp(datetime.datetime.now())

        total_cost = 0
        for item in queue:
            mapping = {
                ResourceData.TYPE: "resources_level",
                InstallationData.TYPE: "installation_level",
                ResearchData.TYPE: "research_level",
                DefenseData.TYPE: "defense_items",
            }

            diff_seconds = (item.start_at + item.time_to_finish) - now
            minutes = diff_seconds/60
            total_cost += minutes * 2

            buildable_items = getattr(planet, mapping[item.type])
            buildable: BuildableItem = list(
                filter(lambda x: x.label == item.label, buildable_items)
            )[0]

            buildable_item_queue.append(buildable)

        if planet.resources.bkm < total_cost:
            raise CantClearQueueNotFundsException

        planet.resources.bkm -= total_cost

        for item in buildable_item_queue:
            await self._update_item_state(planet, item, [])

        await self.planet_repository_port.update(planet)
        return ClearQueuePaidResponse(total_cost=total_cost)

    async def finish_item(self, finish_request: FinishBuildRequest) -> Planet:
        """
        Transition from building state to finished state
        :param finish_request:
        :return:
        """

        planet: Planet = await self.planet_repository_port.get(finish_request.planet_id)
        if planet is None:
            raise NoPlanetFoundException()

        queue: list[BuildingQueueItem] = planet.building_queue.items
        if len(queue) <= 0:
            return await self.response_port.publish_response(planet)

        items: list[BuildingQueueItem] = [queue.pop(0)]

        buildable_item_queue = []
        for item in items:

            mapping = {
                ResourceData.TYPE: "resources_level",
                InstallationData.TYPE: "installation_level",
                ResearchData.TYPE: "research_level",
                DefenseData.TYPE: "defense_items",
            }

            buildable_items = getattr(planet, mapping[item.type])
            buildable: BuildableItem = list(
                filter(lambda x: x.label == item.label, buildable_items)
            )[0]

            buildable_item_queue.append(buildable)

        item: BuildableItem
        for item in buildable_item_queue:
            game_data: GameData = game_data_factory[item.type]
            last_update_field_names = {
                ResourceData.METAL_MINE: "metal_last_updated",
                ResourceData.CRYSTAL_MINE: "crystal_last_updated",
                ResourceData.PETROL_MINE: "petrol_last_updated",
            }

            now = datetime.datetime.timestamp(datetime.datetime.now())

            if now <= item.finish:
                continue

            if item.building:

                if item.type in [
                    ResourceData.TYPE,
                    InstallationData.TYPE,
                    ResearchData.TYPE,
                ]:
                    item.current_level += 1

                if item.type in [ResourceData.TYPE]:
                    if item.label in last_update_field_names:
                        setattr(
                            planet.resources,
                            last_update_field_names[item.label],
                            item.finish,
                        )

                    item.health = (
                        game_data.get_item(item.label)
                        .get_level_info(item.current_level)
                        .health
                    )

                if item.type in [InstallationData.TYPE, ResourceData.TYPE]:
                    planet.slots_used += 1

                if item.type in [ResearchData.TYPE]:
                    if item.label == ResearchData.TERRAFORMING:
                        planet.slots += 1

                if item.type in [DefenseData.TYPE]:
                    data = game_data.get_item(item.label).get_level_info(0)
                    new_health = item.quantity * data.health

                    item.quantity += item.quantity_building
                    item.quantity_building = 0
                    item.health += new_health

                item.finish = None
                item.building = False

                item.state = BuildableItemState.FINISHED
                planet.building_queue.items = queue
                # Dont save without changes it will break
                planet = await self.planet_repository_port.update(planet)

            elif item.repairing:
                info = game_data.get_item(item.label).get_level_info(item.current_level)
                if item.label in last_update_field_names:
                    setattr(
                        planet.resources,
                        last_update_field_names[item.label],
                        item.finish,
                    )

                item.health = info.health
                item.repairing = False
                item.finish = None

                item.state = BuildableItemState.FINISHED
                planet.building_queue.items = queue

                # Dont save without changes it will break
                planet = await self.planet_repository_port.update(planet)

        return await self.response_port.publish_response(planet)

    async def build(self, user: str, request: BuildableRequest) -> BuildableResponse:

        if request.type in [DefenseData.TYPE] and request.quantity is None:
            raise WrongBuildableException()

        if request.type not in [
            ResourceData.TYPE,
            DefenseData.TYPE,
            InstallationData.TYPE,
            ResearchData.TYPE,
        ]:
            raise WrongBuildableException()

        if request.label not in ResourceData.TYPES + DefenseData.TYPES + InstallationData.TYPES + ResearchData.TYPES:
            raise WrongBuildableException()

        planet: Planet = await self.planet_repository_port.get_my_planet(
            user, request.planet_id
        )

        if planet is None:
            raise NoPlanetFoundException()

        if is_queue_full(planet):
            raise QueueIsFullException()

        mapping = {
            ResourceData.TYPE: "resources_level",
            InstallationData.TYPE: "installation_level",
            ResearchData.TYPE: "research_level",
            DefenseData.TYPE: "defense_items",
        }

        buildable_items = getattr(planet, mapping[request.type])
        buildable: BuildableItem = list(
            filter(lambda x: x.label == request.label, buildable_items)
        )[0]

        if buildable.building or buildable.repairing:
            raise CantBuildOrRepairException()

        game_data: GameData = game_data_factory[request.type]
        label_info: BuildableItemBaseType = game_data.get_item(request.label)
        next_lvl: BuildableItemLevelInfo = label_info.get_level_info(
            buildable.current_level + 1
        )
        next_lvl: BuildableItemLevelInfo = tier_benefit_buildable_items(
            planet.tier.tier_code, next_lvl
        )

        if (
            request.type == ResourceData.TYPE
            and buildable.health
            < label_info.get_level_info(buildable.current_level).health
        ):
            raise CantUpgradeIfHealthIsNotFullException()

        if planet.slots_used >= planet.slots:
            raise CantBuildSlotsFullException()

        if (
            planet.resources.metal < next_lvl.cost_metal
            or planet.resources.crystal < next_lvl.cost_crystal
            or planet.resources.petrol < next_lvl.cost_petrol
        ):
            raise NotEnoughFundsForBuildException()

        planet.resources.metal -= next_lvl.cost_metal
        planet.resources.crystal -= next_lvl.cost_crystal
        planet.resources.petrol -= next_lvl.cost_petrol
        buildable.building = True
        buildable.state = BuildableItemState.BUILDING

        time = next_lvl.time
        if request.type in [DefenseData.TYPE]:
            time *= request.quantity
            buildable.quantity_building = request.quantity

        now = datetime.datetime.timestamp(datetime.datetime.now())

        if request.label == ResourceData.TYPE:
            buildable.health = next_lvl.health

        if request.label in [ResourceData.TYPE, InstallationData.TYPE]:
            planet.slots_used += 1

        if len(planet.building_queue.items) == 0:
            start_at = now
        else:
            previous_item_finish = planet.building_queue.items[0].start_at + planet.building_queue.items[0].time_to_finish
            start_at = previous_item_finish

        buildable.finish = start_at + datetime.timedelta(seconds=time).total_seconds()

        new_queue_item = BuildingQueueItem(
            label=request.label,
            type=request.type,
            action=BuildableItemState.BUILDING,
            next_level=next_lvl.level,
            quantity=request.quantity,
            time_to_finish=datetime.timedelta(seconds=time).total_seconds(),
            start_at=start_at
        )

        planet.building_queue.items.append(new_queue_item)
        planet = await self.planet_repository_port.update(planet)
        await self.planet_level_use_case.give_planet_experience(
            GivePlanetExperienceRequest(
                planet_id=str(planet.id), experience_amount=next_lvl.experience
            )
        )
        await self.planet_level_use_case.give_user_experience(
            GiveUserExperienceRequest(
                user_id=str(planet.user), experience_amount=next_lvl.experience
            )
        )

        response = BuildableResponse.from_buildable_item(buildable)
        response.metal_paid = next_lvl.cost_metal
        response.crystal_paid = next_lvl.cost_crystal
        response.petrol_paid = next_lvl.cost_petrol
        response.queue_item_info = new_queue_item

        return await self.response_port.publish_response(response)

    async def repair(self, user: str, request: BuildableRequest) -> BuildableResponse:
        if request.type != ResourceData.TYPE or request.label not in ResourceData.TYPES:
            raise WrongBuildableException()

        planet: Planet = await self.planet_repository_port.get_my_planet(
            user, request.planet_id
        )

        if planet is None:
            raise NoPlanetFoundException()

        if is_queue_full(planet):
            raise QueueIsFullException()

        mapping = {
            ResourceData.TYPE: "resources_level",
        }

        buildable_items = getattr(planet, mapping[request.type])
        buildable: BuildableItem = list(
            filter(lambda x: x.label == request.label, buildable_items)
        )[0]

        if buildable.building or buildable.repairing:
            raise CantBuildOrRepairException()

        game_data: GameData = game_data_factory[request.type]
        label_info: BuildableItemBaseType = game_data.get_item(request.label)
        current_level_info: BuildableItemLevelInfo = label_info.get_level_info(
            buildable.current_level
        )

        current_health = buildable.health
        full_health = current_level_info.health

        if current_health == full_health:
            raise CantRepairIfHealthIsFullException()

        percentage = 1 - (current_health / full_health)
        cost_metal = math.ceil(current_level_info.cost_metal * percentage)
        cost_crystal = math.ceil(current_level_info.cost_crystal * percentage)
        cost_petrol = math.ceil(current_level_info.cost_petrol * percentage)
        time = math.ceil(current_level_info.time * percentage)
        experience = math.ceil(current_level_info.experience * percentage)

        if (
            planet.resources.metal < cost_metal
            or planet.resources.crystal < cost_crystal
            or planet.resources.petrol < cost_petrol
        ):
            raise NotEnoughFundsForBuildException()

        planet.resources.metal -= cost_metal
        planet.resources.crystal -= cost_crystal
        planet.resources.petrol -= cost_petrol
        buildable.repairing = True

        now = datetime.datetime.timestamp(datetime.datetime.now())

        if len(planet.building_queue.items) == 0:
            start_at = now
        else:
            previous_item_finish = planet.building_queue.items[0].start_at + planet.building_queue.items[0].time_to_finish
            start_at = previous_item_finish

        buildable.finish = start_at + datetime.timedelta(seconds=time).total_seconds()

        new_queue_item = BuildingQueueItem(
            label=request.label,
            type=request.type,
            action=BuildableItemState.REPAIRING,
            next_level=current_level_info.level,
            quantity=request.quantity,
            time_to_finish=datetime.timedelta(seconds=time).total_seconds(),
            start_at=start_at
        )

        planet.building_queue.items.append(new_queue_item)
        planet = await self.planet_repository_port.update(planet)

        await self.planet_level_use_case.give_planet_experience(
            GivePlanetExperienceRequest(
                planet_id=str(planet.id), experience_amount=experience
            )
        )
        await self.planet_level_use_case.give_user_experience(
            GiveUserExperienceRequest(
                user_id=str(planet.user), experience_amount=experience
            )
        )

        response = BuildableResponse.from_buildable_item(buildable)
        response.metal_paid = cost_metal
        response.crystal_paid = cost_crystal
        response.petrol_paid = cost_petrol
        response.queue_item_info = new_queue_item

        return await self.response_port.publish_response(response)
