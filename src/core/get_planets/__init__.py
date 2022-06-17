from dataclasses import dataclass

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


class FetchByPlanetPositionRangeRequest(BaseModel):
    galaxy: int
    from_solar_system: int
    to_solar_system: int


class PlanetInformationResponse(BaseModel):
    id: str = False
    name: str = None
    rarity: str = None
    image: str = None
    image_url: str = None
    image_bg_url: str = None
    level: int = None
    galaxy: int = None
    solar_system: int = None
    position: int = None
    user: str = None

    @staticmethod
    def from_planet_response(p: PlanetResponse) -> "PlanetInformationResponse":
        re = PlanetInformationResponse()
        re.id = p.id
        re.name = p.name
        re.rarity = p.rarity
        re.image = p.image
        re.image_url = p.image_url
        re.level = p.level
        re.galaxy = p.galaxy
        re.solar_system = p.solar_system
        re.position = p.position
        re.user = p.user
        return re


class FetchByPlanetPositionRangeResponse(BaseModel):
    planets: list = []  # position : planet



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

    async def fetch_by_position_range(self, request: FetchByPlanetPositionRangeRequest):
        planets = await self.planet_repository.by_position_range(request.galaxy,
                                                                 request.from_solar_system,
                                                                 request.to_solar_system,
                                                                 True)

        planets_by_position = {}
        for planet in planets:
            planet.set_image_url(self.planet_images_bucket_path)
            planet_position = f"{planet.galaxy}:{planet.solar_system}:{planet.position-1}"
            planet_response_raw = PlanetResponse.from_planet(planet)
            # re.planets[planet_position] = PlanetInformationResponse.from_planet_response(planet_response)
            planets_by_position[planet_position] = PlanetInformationResponse.from_planet_response(planet_response_raw)

        re = FetchByPlanetPositionRangeResponse()
        for a in range(7):
            re.planets.append([])
            for b in range(12):
                pos = f"{request.galaxy}:{request.from_solar_system+a}:{b}"
                re.planets[a].append(PlanetInformationResponse())

                try:
                    re.planets[a][b] = planets_by_position[pos]
                    planet_rarity = planets_by_position[pos].rarity.lower()
                    planet_image = planets_by_position[pos].image
                    re.planets[a][b].image_bg_url = f"{self.planet_images_bucket_path}/{planet_image}-{planet_rarity}.png"
                except KeyError:
                    empty_planet = PlanetInformationResponse()
                    empty_planet.galaxy = request.galaxy
                    empty_planet.solar_system = request.from_solar_system+a
                    empty_planet.position = b
                    re.planets[a][b] = empty_planet

        return await self.response_port.publish_response(re)
