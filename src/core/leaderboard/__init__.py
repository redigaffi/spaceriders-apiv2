from dataclasses import dataclass
from typing import Optional

from core.shared.ports import PlanetRepositoryPort, UserRepositoryPort, ResponsePort

from pydantic import BaseModel

from core.shared.static.game_data.AccountLevelData import AccountLevelData
from core.shared.static.game_data.PlanetLevelData import PlanetLevelData

class PaginatedResponse(BaseModel):
    total_elements: int
    total_pages: int
    per_page: int
    current_page: int
    data: list


class PlanetLeaderBoardResponse(BaseModel):
    planet_name: str
    level: int
    experience: int
    experience_needed: int
    image_url_bg: str = None


class UserLeaderBoardResponse(BaseModel):
    wallet: str
    username: Optional[str] = None
    level: int
    experience: int
    faction: str
    dominion: int
    badges: list[str]
    experience_needed: int


@dataclass
class LeaderBoard:
    planet_repository_port: PlanetRepositoryPort
    user_repository_port: UserRepositoryPort
    planet_images_bucket_path: str
    response_port: ResponsePort

    async def get_by_planets(self, page: int, per_page: int):
        all_planets = await self.planet_repository_port.planet_leaderboard(page, per_page)
        planet_count = await self.planet_repository_port.all_claimed_planets_count()

        data = []
        for planet in all_planets:
            planet.set_image_url(self.planet_images_bucket_path)
            data.append(
                PlanetLeaderBoardResponse(
                    planet_name=planet.name,
                    level=planet.level,
                    experience=planet.experience,
                    experience_needed=PlanetLevelData.get_level_experience(planet.level+1),
                    image_url_bg=planet.image_url_bg
                )
            )

        return await self.response_port.publish_response(PaginatedResponse(
            total_elements=planet_count,
            total_pages=planet_count//per_page,
            per_page=per_page,
            current_page=page,
            data=data
        ))

    async def get_by_users(self, page: int, per_page: int):
        all_users = await self.user_repository_port.user_leaderboard(page, per_page)
        user_count = await self.user_repository_port.all_users_count()

        data = []
        for user in all_users:
            data.append(
                UserLeaderBoardResponse(
                    wallet=user.wallet,
                    username=user.username,
                    level=user.level,
                    experience=user.experience,
                    faction="",
                    dominion=0,
                    badges=[],
                    experience_needed=AccountLevelData.get_level_experience(user.level + 1)
                )
            )

        return await self.response_port.publish_response(PaginatedResponse(
            total_elements=user_count,
            total_pages=user_count // per_page,
            per_page=per_page,
            current_page=page,
            data=data
        ))
