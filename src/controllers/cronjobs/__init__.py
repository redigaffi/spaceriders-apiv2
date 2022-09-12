from dataclasses import dataclass

from core.mint_planet import MintPlanet
from core.planet_energy import PlanetEnergy, PlanetEnergyRecoverEnergyDepositsRequest
from core.planet_level import PlanetLevel
from core.planet_staking import Staking
from core.pve.asteroid import Asteroid
from core.pve.space_pirates import SpacePirates, SpacePirateRequest
from core.resource_exchange import ResourcesExchange


@dataclass
class CronjobController:
    energy_planet_use_case: PlanetEnergy
    staking_use_case: Staking
    planet_level: PlanetLevel
    resources_exchange: ResourcesExchange
    mint_planet: MintPlanet
    asteroid: Asteroid
    space_pirate: SpacePirates

    async def recover_planets(self, user: str):
        return await self.mint_planet.recover_planet(user)

    async def recover_deposits(self, req: PlanetEnergyRecoverEnergyDepositsRequest):
        return await self.energy_planet_use_case.recover_deposits(req)

    async def recover_staking(self, planet_id: str):
        return await self.staking_use_case.tier_recover(planet_id)

    async def asteroid_pve(self, planet_id: str):
        return await self.asteroid(planet_id)

    async def space_pirate_pve(self, planet_id: str):
        return await self.space_pirate(SpacePirateRequest(planet_id=planet_id))
