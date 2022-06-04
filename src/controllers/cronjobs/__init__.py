from dataclasses import dataclass
from core.planet_energy import PlanetEnergy, PlanetEnergyRecoverEnergyDepositsRequest
from core.planet_level import PlanetLevel
from core.planet_staking import Staking
from core.resource_exchange import ResourcesExchange


@dataclass
class CronjobController:
    energy_planet_use_case: PlanetEnergy
    staking_use_case: Staking
    planet_level: PlanetLevel
    resources_exchange: ResourcesExchange

    async def recover_deposits(self, req: PlanetEnergyRecoverEnergyDepositsRequest):
        return await self.energy_planet_use_case.recover_deposits(req)

    async def recover_staking(self, planet_id: str):
        return await self.staking_use_case.tier_recover(planet_id)

    async def recover_level_up(self, planet_id: str):
        return await self.planet_level.recover_level_up(planet_id)

    async def generate_new_resource_price(self):
        return await self.resources_exchange.new_resource_exchange_price()
