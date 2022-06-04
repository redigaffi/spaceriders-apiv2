from dataclasses import dataclass
from pydantic import BaseModel

from core.planet_emails import PlanetEmails, PlanetSendEmailRequest
from core.shared.models import LevelUpRewardClaims, Planet
from core.shared.ports import LevelUpRewardClaimsRepositoryPort, PlanetRepositoryPort, ResponsePort
from core.shared.static.game_data.Common import CommonKeys
from core.shared.static.game_data.PlanetLevelData import PlanetLevelData


class GivePlanetExperienceRequest(BaseModel):
    planet_id: str
    experience_amount: float


@dataclass
class PlanetLevel:
    planet_repository_port: PlanetRepositoryPort
    lvl_up_repository_port: LevelUpRewardClaimsRepositoryPort
    email_use_case: PlanetEmails
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

            if not planet.is_free():
                lvl_claim: LevelUpRewardClaims = LevelUpRewardClaims(level=planet.level, planet_id=str(request.planet_id))
                lvl_claim = await self.lvl_up_repository_port.create(lvl_claim)
                planet.pending_levelup_reward.append(lvl_claim)

            await self.planet_repository_port.update(planet)
            email: PlanetSendEmailRequest = PlanetSendEmailRequest(planet_id_receiver=str(planet.id),
                                                                   title="Pending level up claim!",
                                                                   sub_title="",
                                                                   template="plain",
                                                                   body=f"You have reached level {planet.level} as reward your $SPR Purchasing Power increases by {PlanetLevelData.LEVEL[planet.level][CommonKeys.REWARDS][CommonKeys.PURCHASING_POWER]}$. You can claim your reward in planet overview.")
            await self.email_use_case.create(email)
            return await self.response_port.publish_response(planet)

        planet.experience += request.experience_amount
        await self.planet_repository_port.update(planet)
        return await self.response_port.publish_response(planet)
