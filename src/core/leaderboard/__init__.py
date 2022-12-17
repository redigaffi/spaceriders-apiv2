from dataclasses import dataclass
from typing import Optional

from core.shared.ports import PlanetRepositoryPort, UserRepositoryPort, ResponsePort

from pydantic import BaseModel


class PlanetLeaderBoardResponse(BaseModel):
    planet_name: str
    level: int
    experience: int
    faction: str
    dominion: int
    badges: list[str]


class UserLeaderBoardResponse(BaseModel):
    wallet: str
    username: Optional[str] = None
    level: int
    experience: int
    faction: str
    dominion: int
    badges: list[str]


@dataclass
class LeaderBoard:
    planet_repository_port: PlanetRepositoryPort
    user_repository_port: UserRepositoryPort
    response_port: ResponsePort

    async def get_by_planets(self, page: int, per_page: int):
        all_planets = await self.planet_repository_port.planet_leaderboard(page, per_page)

        re = []
        for planet in all_planets:
            re.append(
                PlanetLeaderBoardResponse(
                    planet_name=planet.name,
                    level=planet.level,
                    experience=planet.experience,
                    faction="",
                    dominion=0,
                    badges=[]
                )
            )

        return await self.response_port.publish_response(re)

    async def get_by_users(self, page: int, per_page: int):
        all_users = await self.user_repository_port.user_leaderboard(page, per_page)
        re = []
        for user in all_users:
            re.append(
                UserLeaderBoardResponse(
                    wallet=user.wallet,
                    username=user.username,
                    level=user.level,
                    experience=user.experience,
                    faction="",
                    dominion=0,
                    badges=[]
                )
            )

        return await self.response_port.publish_response(re)

