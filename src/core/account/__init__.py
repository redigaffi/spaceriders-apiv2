from dataclasses import dataclass

from core.shared.models import User
from core.shared.ports import PlanetRepositoryPort, ResponsePort, UserRepositoryPort
from pydantic import BaseModel

from core.shared.static.game_data import AccountLevelData
from core.shared.static.game_data.AccountLevelData import AccountLevelData


class AccountInfoResponse(BaseModel):
    wallet: str
    experience: int
    level: int




@dataclass
class Account:
    user_repository_port: UserRepositoryPort
    response_port: ResponsePort

    async def account_info(self, wallet_id: str):
        user: User = await self.user_repository_port.find_user(wallet_id)
        planets = user.planets

        total_planet_xp = 0
        for planet in planets:
            total_planet_xp += planet.experience

        account_level = 0
        for i in range(15):
            xp_total_required = AccountLevelData.get_level_experience(i)

            if total_planet_xp < xp_total_required:
                break

            account_level += 1

        return await self.response_port.publish_response(AccountInfoResponse(
            wallet=wallet_id,
            experience=total_planet_xp,
            level=account_level
        ))
