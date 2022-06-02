from dataclasses import dataclass
from src.core.planet_energy import PlanetEnergy, PlanetEnergyRecoverEnergyDepositsRequest

@dataclass
class CronjobController:
    energy_planet_use_case: PlanetEnergy

    async def recover_deposits(self, req: PlanetEnergyRecoverEnergyDepositsRequest):
        return await self.energy_planet_use_case.recover_deposits(req)
