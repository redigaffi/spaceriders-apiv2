from dataclasses import dataclass
from pydantic import BaseModel

from core.planet_email import PlanetEmail, PlanetSendEmailRequest
from core.shared.models import Planet, AppBaseException, PlanetResponse
from core.shared.ports import PlanetRepositoryPort, ResponsePort, ChainServicePort
from core.shared.static.game_data.Common import CommonKeys
from core.shared.static.game_data.PlanetLevelData import PlanetLevelData


class GivePlanetExperienceRequest(BaseModel):
    planet_id: str
    experience_amount: float

class LvlUpAlreadyClaimedException(AppBaseException):
    msg = "Level up has already been claimed"


class LvlUpNotConfirmedSmartContract(AppBaseException):
    msg = "Level up claim is not registered in the smart contract"


@dataclass
class PlanetLevel:
    planet_repository_port: PlanetRepositoryPort
    email_use_case: PlanetEmail
    contract_service: ChainServicePort
    response_port: ResponsePort

    async def give_planet_experience(self, request: GivePlanetExperienceRequest) -> Planet:
        planet = await self.planet_repository_port.get(request.planet_id)
        try:
            next_level_info = PlanetLevelData.LEVEL[planet.level + 1]
        except:
            return planet

        current_xp = planet.experience
        if current_xp + request.experience_amount >= next_level_info[CommonKeys.EXPERIENCE]:
            difference = (current_xp + request.experience_amount) - next_level_info[CommonKeys.EXPERIENCE]
            planet.level += 1
            planet.experience = difference
            await self.planet_repository_port.update(planet)

            email: PlanetSendEmailRequest = PlanetSendEmailRequest(planet_id_receiver=str(planet.id),
                                                                   title="Level up howdy!!",
                                                                   sub_title="You lovin' it!",
                                                                   template="plain",
                                                                   body=f"You have reached level {planet.level}. As a reward, you'll get free resources.")
            await self.email_use_case.create(email)
            return await self.response_port.publish_response(planet)

        planet.experience += request.experience_amount
        await self.planet_repository_port.update(planet)
        return await self.response_port.publish_response(planet)
