from dataclasses import dataclass

from core.shared.models import Planet
from core.shared.ports import PlanetRepositoryPort, ResponsePort
from pydantic import BaseModel


class FavouritePlanetRequest(BaseModel):
    planet_id: str


@dataclass
class FavouritePlanet:
    planet_repository: PlanetRepositoryPort
    response_port: ResponsePort

    async def mark_planet_favourite(self, user: str, request: FavouritePlanetRequest):
        planet: Planet = await self.planet_repository.get_my_planet(user, request.planet_id)
        planet.is_favourite = True
        await self.planet_repository.update(planet)
        return await self.response_port.publish_response({})

    async def unmark_planet_favourite(self, user: str, request: FavouritePlanetRequest):
        planet: Planet = await self.planet_repository.get_my_planet(user, request.planet_id)
        planet.is_favourite = False
        await self.planet_repository.update(planet)
        return await self.response_port.publish_response({})
