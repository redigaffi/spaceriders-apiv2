from dataclasses import dataclass
from typing import List

from core.shared.models import NoPlanetFoundException, Planet, PlanetResponse
from core.shared.ports import PlanetRepositoryPort, ResponsePort
from pydantic import BaseModel


class FetchByPlanetIdResponse(BaseModel):
    planet: PlanetResponse
    resources: dict
    research: dict
    installation: dict
    defense: dict
    emails: list

@dataclass
class GetPlanets:
    planet_repository: PlanetRepositoryPort
    planet_images_bucket_path: str
    response_port: ResponsePort

    async def fetch_by_planet_id(self, user: str, planet_id: str):
        planet: Planet = await self.planet_repository.get_my_planet(user, planet_id, True)

        if planet is None:
            raise NoPlanetFoundException()

        ri = planet.get_planet_resource_data()
        re = planet.get_planet_research_data()
        ii = planet.get_planet_installation_data()
        di = planet.get_planet_defense_data()
        em = planet.get_emails()

        planet.set_image_url(self.planet_images_bucket_path)

        response = FetchByPlanetIdResponse(
            planet=PlanetResponse.from_planet(planet),
            resources=ri,
            research=re,
            installation=ii,
            defense=di,
            emails=em
        )

        return await self.response_port.publish_response(response)

    async def fetch_all_planets(self, user: str) -> list[PlanetResponse]:
        planets = await self.planet_repository.all_user_planets(user, True)

        re = []
        for planet in planets:
            planet.set_image_url(self.planet_images_bucket_path)
            re.append(PlanetResponse.from_planet(planet))

        return await self.response_port.publish_response(re)
