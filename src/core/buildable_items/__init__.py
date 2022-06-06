import datetime
from dataclasses import dataclass
from pydantic import BaseModel

from core.planet_level import PlanetLevel, GivePlanetExperienceRequest
from core.shared.models import AppBaseException, Planet, NoPlanetFoundException, QueueIsFullException, BuildableItem
from core.shared.ports import PlanetRepositoryPort, ResponsePort
from core.shared.service.buildable_items import is_queue_full
from core.shared.service.planet import resource_reserve_als
from core.shared.service.tier_benefit import tier_benefit_service
from core.shared.static.game_data.Common import BuildableItemBaseType, BuildableItemLevelInfo
from core.shared.static.game_data.GameData import GameData
from core.shared.static.game_data.GameDataFactory import game_data_factory
from core.shared.static.game_data.ResourceData import ResourceData
from core.shared.static.game_data.DefenseData import DefenseData
from core.shared.static.game_data.InstallationData import InstallationData
from core.shared.static.game_data.ResearchData import ResearchData


class FinishBuildRequest(BaseModel):
    planet_id: str


class BuildableRequest(BaseModel):
    type: str
    label: str
    planet_id: str
    quantity: int = None


class BuildableResponse(BuildableItem):
    metal_paid: float = None
    crystal_paid: float = None
    petrol_paid: float = None

    @staticmethod
    def from_buildable_item(item: BuildableItem):
        return BuildableResponse(label=item.label,
                                 type=item.type,
                                 current_level=item.current_level,
                                 building=item.building,
                                 finish=item.finish,
                                 repairing=item.repairing,
                                 health=item.health,
                                 quantity=item.quantity,
                                 quantity_building=item.quantity_building)


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


@dataclass
class BuildableItems:
    planet_repository_port: PlanetRepositoryPort
    planet_level_use_case: PlanetLevel
    response_port: ResponsePort

    async def finish_build(self, finish_request: FinishBuildRequest) -> Planet:
        """
        Transition from building state to finished state
        :param finish_request:
        :return:
        """

        planet: Planet = await self.planet_repository_port.get(finish_request.planet_id)
        if planet is None:
            raise NoPlanetFoundException()

        queue: list[BuildableItem] = planet.building_queue()

        item: BuildableItem
        for item in queue:
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

                if item.type in [ResourceData.TYPE, InstallationData.TYPE, ResearchData.TYPE]:
                    item.current_level += 1

                if item.type in [ResourceData.TYPE]:
                    if item.label in last_update_field_names:
                        setattr(planet.resources, last_update_field_names[item.label], item.finish)

                    item.health = game_data.get_item(item.label).get_level_info(item.current_level).health

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
                # Dont save without changes it will break
                planet = await self.planet_repository_port.update(planet)

            elif item.repairing:
                info = game_data.get_item(item.label).get_level_info(item.current_level)
                if item.label in last_update_field_names:
                    setattr(planet.resources, last_update_field_names[item.label], item.finish)

                item.health = info.health
                item.repairing = False
                item.finish = None
            # Dont save without changes it will break
                planet = await self.planet_repository_port.update(planet)

        return await self.response_port.publish_response(planet)

    async def build(self, user: str, request: BuildableRequest) -> BuildableResponse:

        if request.type in [DefenseData.TYPE] and request.quantity is None:
            raise WrongBuildableException()

        if request.type not in [ResourceData.TYPE, DefenseData.TYPE, InstallationData.TYPE, ResearchData.TYPE]:
            raise WrongBuildableException()

        if request.label not in (ResourceData.TYPES +
                                 DefenseData.TYPES +
                                 InstallationData.TYPES +
                                 ResearchData.TYPES):
            raise WrongBuildableException()

        planet: Planet = await self.planet_repository_port.get_my_planet(user, request.planet_id)

        if planet is None:
            raise NoPlanetFoundException()

        if is_queue_full(planet):
            raise QueueIsFullException()

        mapping = {
            ResourceData.TYPE: "resources_level",
            InstallationData.TYPE: "installation_level",
            ResearchData.TYPE: "research_level",
            DefenseData.TYPE: "defense_items"
        }

        buildable_items = getattr(planet, mapping[request.type])
        buildable: BuildableItem = list(filter(lambda x: x.label == request.label, buildable_items))[0]

        if buildable.building or buildable.repairing:
            raise CantBuildOrRepairException()

        game_data: GameData = game_data_factory[request.type]
        label_info: BuildableItemBaseType = game_data.get_item(request.label)
        next_lvl: BuildableItemLevelInfo = label_info.get_level_info(buildable.current_level + 1)
        next_lvl: BuildableItemLevelInfo = tier_benefit_service(planet.tier.tier_code, next_lvl)

        if request.type == ResourceData.TYPE and buildable.health < label_info.get_level_info(buildable.current_level).health:
            raise CantUpgradeIfHealthIsNotFullException()

        if planet.slots_used >= planet.slots:
            raise CantBuildSlotsFullException()

        if planet.resources.metal < next_lvl.cost_metal or planet.resources.crystal < next_lvl.cost_crystal or planet.resources.petrol < next_lvl.cost_petrol:
            raise NotEnoughFundsForBuildException()

        planet.resources.metal -= next_lvl.cost_metal
        planet.resources.crystal -= next_lvl.cost_crystal
        planet.resources.petrol -= next_lvl.cost_petrol
        buildable.building = True

        time = next_lvl.time
        if request.type in [DefenseData.TYPE]:
            time *= request.quantity
            buildable.quantity_building = request.quantity

        now = datetime.datetime.timestamp(datetime.datetime.now())
        buildable.finish = now + datetime.timedelta(seconds=time).total_seconds()

        if request.label == ResourceData.TYPE:
            buildable.health = next_lvl.health

        if request.label in [ResourceData.TYPE, InstallationData.TYPE]:
            planet.slots_used += 1

        planet = resource_reserve_als(request.label, planet, next_lvl)
        planet = await self.planet_repository_port.update(planet)
        await self.planet_level_use_case.give_planet_experience(GivePlanetExperienceRequest(planet_id=str(planet.id), experience_amount=next_lvl.experience))

        response = BuildableResponse.from_buildable_item(buildable)
        response.metal_paid = next_lvl.cost_metal
        response.crystal_paid = next_lvl.cost_crystal
        response.petrol_paid = next_lvl.cost_petrol

        return await self.response_port.publish_response(response)
