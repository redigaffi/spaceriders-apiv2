from dataclasses import dataclass
from core.planet_energy import PlanetEnergy, PlanetEnergyRecoverEnergyDepositsRequest
from core.planet_staking import Staking


@dataclass
class CronjobController:
    energy_planet_use_case: PlanetEnergy
    staking_use_case: Staking

    async def recover_deposits(self, req: PlanetEnergyRecoverEnergyDepositsRequest):
        return await self.energy_planet_use_case.recover_deposits(req)

    async def recover_staking(self, planet_id: str):
        return await self.staking_use_case.tier_recover(planet_id)

