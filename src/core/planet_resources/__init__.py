from dataclasses import dataclass
import datetime
import math

from pydantic import BaseModel

from core.shared.models import BuildableItem, Planet
from core.shared.ports import PlanetRepositoryPort, ResponsePort
from core.shared.static.game_data.Common import BuildableItemLevelInfo, CommonKeys
from core.shared.static.game_data.PlanetData import PlanetData
from core.shared.static.game_data.ResourceData import ResourceData as RD


class PlanetResourcesUpdateRequest(BaseModel):
    planet_id: str


@dataclass
class PlanetResources:
    planet_repository_port: PlanetRepositoryPort
    response_port: ResponsePort

    async def __call__(self, request: PlanetResourcesUpdateRequest):

        planet: Planet = await self.planet_repository_port.get(request.planet_id)

        resource_levels: list[BuildableItem] = planet.resources_level
        mines: list[BuildableItem] = list(
            filter(
                lambda x: x.label in [RD.METAL_MINE, RD.CRYSTAL_MINE, RD.PETROL_MINE],
                resource_levels,
            )
        )

        warehouses = {
            RD.METAL_WAREHOUSE: next(
                (x for x in resource_levels if x.label == RD.METAL_WAREHOUSE), False
            ),
            RD.CRYSTAL_WAREHOUSE: next(
                (x for x in resource_levels if x.label == RD.CRYSTAL_WAREHOUSE), False
            ),
            RD.PETROL_WAREHOUSE: next(
                (x for x in resource_levels if x.label == RD.PETROL_WAREHOUSE), False
            ),
        }

        last_update_field_names = {
            RD.METAL_MINE: "metal_last_updated",
            RD.CRYSTAL_MINE: "crystal_last_updated",
            RD.PETROL_MINE: "petrol_last_updated",
        }

        resource_names = {
            RD.METAL_MINE: "metal",
            RD.CRYSTAL_MINE: "crystal",
            RD.PETROL_MINE: "petrol",
        }
        # mine: BuildableItem
        for mine in mines:
            planet: Planet = await self.planet_repository_port.get(request.planet_id)

            now = datetime.datetime.timestamp(datetime.datetime.now())
            label = mine.label

            last_update = getattr(planet.resources, last_update_field_names[label])
            if last_update is None:
                last_update = now

            diff_seconds = abs(now - last_update)
            diff_minutes = math.trunc(diff_seconds / 60)

            # If upgrading or no minute has passed, skip this mine, nothing to do.
            if diff_minutes <= 0:
                continue

            if mine.building or mine.repairing:
                setattr(planet.resources, last_update_field_names[label], now)
                planet = await self.planet_repository_port.update(planet)
                continue

            mine_info: BuildableItemLevelInfo = RD.get_item(label).get_level_info(
                mine.current_level
            )

            mine_health = mine.health
            lvl_health = mine_info.health

            production = self.__calculate_production_health(
                diff_minutes, mine, mine_info
            )
            energy_usage = self.__energy_usage_health_factor(
                mine_health / lvl_health, (mine_info.energy_usage * diff_minutes)
            )

            if energy_usage > planet.resources.energy:
                try:
                    credit_minutes = (
                        float(planet.resources.energy) / mine_info.energy_usage
                    )
                except:
                    credit_minutes = 0

                production = self.__calculate_production_health(
                    credit_minutes, mine, mine_info
                )
                energy_usage = self.__energy_usage_health_factor(
                    mine_health / lvl_health, (mine_info.energy_usage * credit_minutes)
                )

            if planet.resources.energy <= 0:
                production = 0
                energy_usage = 0

            self.__update_resources(planet, label, warehouses, production, energy_usage)
            setattr(
                planet.resources,
                last_update_field_names[label],
                datetime.datetime.timestamp(datetime.datetime.now()),
            )

            # Dont save without changes
            planet = await self.planet_repository_port.update(planet)

        return await self.response_port.publish_response(planet)

    def __update_resources(
        self,
        planet: Planet,
        label: str,
        warehouses: dict[str, BuildableItem],
        production: float,
        energy_usage: float,
    ):
        mapping = {
            RD.METAL_MINE: RD.METAL_WAREHOUSE,
            RD.PETROL_MINE: RD.PETROL_WAREHOUSE,
            RD.CRYSTAL_MINE: RD.CRYSTAL_WAREHOUSE,
        }
        fields = {
            RD.METAL_MINE: {
                "resource_name": "metal",
                "reserve_name": "total_metal",
            },
            RD.CRYSTAL_MINE: {
                "resource_name": "crystal",
                "reserve_name": "total_crystal",
            },
            RD.PETROL_MINE: {
                "resource_name": "petrol",
                "reserve_name": "total_petrol",
            },
        }

        warehouse_type = mapping.get(label)
        warehouse = warehouses[warehouse_type]
        warehouse_info = RD.get_item(warehouse_type).get_level_info(
            warehouse.current_level
        )

        warehouse_health = warehouse.health
        max_health = warehouse_info.health
        health_percentage = warehouse_health / max_health
        storage_capacity = warehouse_info.capacity
        storage_capacity *= health_percentage

        reserve_withdraw = production
        resource_planet_reserve = getattr(
            planet.reserves, fields[label]["reserve_name"]
        )

        # Extract from visible reserve
        if resource_planet_reserve - production < 0:
            energy_factor = float(resource_planet_reserve) / production
            energy_usage = energy_usage * energy_factor
            production = resource_planet_reserve
            reserve_withdraw = resource_planet_reserve

        if production <= 0:
            return

        current_resource_amount = getattr(
            planet.resources, fields[label]["resource_name"]
        )

        # Can we store the current production
        # TODO: Bug: when you have full stored resources (resources > capacity) and an asteroid hits,
        # and reduces the capacity for storing resources of the warehouse, then that "excess" resource gets lots,
        # So for e.g, your metal warehouse can store 200 metal, you have 200 metal, asteroid hits and damages warehouse,
        # 1% or so.., now your warehouse can store 197, currently what happens, you loose 3 of metal since warehouse can
        # only store 197 so you lost 3 of metal, now you have 197
        if (current_resource_amount + production) > storage_capacity:
            production = storage_capacity - current_resource_amount

        planet.resources.energy -= energy_usage

        setattr(
            planet.resources,
            fields[label]["resource_name"],
            (current_resource_amount + production),
        )
        setattr(
            planet.reserves,
            fields[label]["reserve_name"],
            (resource_planet_reserve - reserve_withdraw),
        )

    def __calculate_production_health(
        self,
        diff_minutes: float,
        mine: BuildableItem,
        mine_info: BuildableItemLevelInfo,
    ):
        production = mine_info.production * diff_minutes
        mine_health = mine.health
        lvl_health = mine_info.health
        health_percentage = mine_health / lvl_health
        production *= health_percentage
        return production

    def __energy_usage_health_factor(self, health_percentage, energy_usage):
        if health_percentage < 1:
            energy_health_factor = health_percentage * 1.5
            if energy_health_factor > 1:
                energy_health_factor = 1

            energy_usage *= energy_health_factor

        return energy_usage
