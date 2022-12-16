from dataclasses import dataclass

from core.shared.ports import PlanetRepositoryPort, UserRepositoryPort, ResponsePort


@dataclass
class LeaderBoard:
    planet_repository_port: PlanetRepositoryPort
    user_repository_port: UserRepositoryPort
    response_port: ResponsePort

    async def get_by_planets(self):
        pass

    async def get_by_users(self):
        pass
