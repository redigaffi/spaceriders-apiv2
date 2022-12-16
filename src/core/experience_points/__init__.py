from dataclasses import dataclass

from pydantic import BaseModel

from core.planet_email import PlanetEmail, PlanetSendEmailRequest
from core.shared.models import AppBaseException, Planet, PlanetResponse, User
from core.shared.ports import ChainServicePort, PlanetRepositoryPort, ResponsePort, UserRepositoryPort
from core.shared.static.game_data.AccountLevelData import AccountLevelData
from core.shared.static.game_data.Common import CommonKeys
from core.shared.static.game_data.PlanetLevelData import PlanetLevelData


class GivePlanetExperienceRequest(BaseModel):
    planet_id: str
    experience_amount: float

class GiveUserExperienceRequest(BaseModel):
    user_id: str
    experience_amount: float


class LvlUpAlreadyClaimedException(AppBaseException):
    msg = "Level up has already been claimed"


class LvlUpNotConfirmedSmartContract(AppBaseException):
    msg = "Level up claim is not registered in the smart contract"


@dataclass
class ExperiencePoints:
    planet_repository_port: PlanetRepositoryPort
    user_repository_port: UserRepositoryPort
    email_use_case: PlanetEmail
    contract_service: ChainServicePort
    response_port: ResponsePort

    def __has_reached_next_level(self, next_level_info, current_xp, experience_amount) -> bool:
        return (current_xp + experience_amount) >= next_level_info[CommonKeys.EXPERIENCE]

    async def give_planet_experience(
        self, request: GivePlanetExperienceRequest
    ) -> Planet:
        planet = await self.planet_repository_port.get(request.planet_id)
        try:
            next_level_info = PlanetLevelData.LEVEL[planet.level + 1]
        except:
            return planet

        current_xp = planet.experience
        if self.__has_reached_next_level(next_level_info, current_xp, request.experience_amount):
            difference = (current_xp + request.experience_amount) - next_level_info[
                CommonKeys.EXPERIENCE
            ]
            planet.level += 1
            planet.experience = difference
            await self.planet_repository_port.update(planet)

            email: PlanetSendEmailRequest = PlanetSendEmailRequest(
                planet_id_receiver=str(planet.id),
                title="Level up howdy!",
                sub_title="You lovin' it!",
                template="plain",
                topic="level_up",
                body=f"You have reached level {planet.level}. Congratulations!",
            )
            await self.email_use_case.create(email)
            return await self.response_port.publish_response(planet)

        planet.experience += request.experience_amount
        await self.planet_repository_port.update(planet)
        return await self.response_port.publish_response(planet)

    async def give_user_experience(
            self, request: GiveUserExperienceRequest
    ) -> User:
        user = await self.user_repository_port.find_user(request.user_id)

        try:
            next_level_info = AccountLevelData.LEVEL[user.level + 1]
        except:
            return user

        current_xp = user.experience
        if self.__has_reached_next_level(next_level_info, current_xp, request.experience_amount):
            difference = (current_xp + request.experience_amount) - next_level_info[
                CommonKeys.EXPERIENCE
            ]

            user.level += 1
            user.experience = difference
            await self.user_repository_port.update(user)
            return await self.response_port.publish_response(user)

        user.experience += request.experience_amount
        await self.user_repository_port.update(user)
        return await self.response_port.publish_response(user)
