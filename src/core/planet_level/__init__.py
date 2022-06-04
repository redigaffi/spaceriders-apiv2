from dataclasses import dataclass
from pydantic import BaseModel

from core.planet_email import PlanetEmail, PlanetSendEmailRequest
from core.shared.models import LevelUpRewardClaims, Planet, AppBaseException
from core.shared.ports import LevelUpRewardClaimsRepositoryPort, PlanetRepositoryPort, ResponsePort, ChainServicePort
from core.shared.static.game_data.Common import CommonKeys
from core.shared.static.game_data.PlanetLevelData import PlanetLevelData


class GivePlanetExperienceRequest(BaseModel):
    planet_id: str
    experience_amount: float


class ClaimPendingLvlUpRewardResponse(BaseModel):
    claim_id: str
    amount: float
    v: int
    r: str
    s: str


class LvlUpAlreadyClaimedException(AppBaseException):
    msg = "Level up has already been claimed"


class LvlUpNotConfirmedSmartContract(AppBaseException):
    msg = "Level up claim is not registered in the smart contract"


@dataclass
class PlanetLevel:
    planet_repository_port: PlanetRepositoryPort
    lvl_up_repository_port: LevelUpRewardClaimsRepositoryPort
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

            if not planet.is_free():
                lvl_claim: LevelUpRewardClaims = LevelUpRewardClaims(level=planet.level, planet_id=request.planet_id)
                lvl_claim = await self.lvl_up_repository_port.create(lvl_claim)
                planet.pending_levelup_reward.append(lvl_claim)

            await self.planet_repository_port.update(planet)
            email: PlanetSendEmailRequest = PlanetSendEmailRequest(planet_id_receiver=str(planet.id),
                                                                   title="Pending level up claim!",
                                                                   sub_title="You lovi'n it!",
                                                                   template="plain",
                                                                   body=f"You have reached level {planet.level} as reward your $SPR Purchasing Power increases by {PlanetLevelData.LEVEL[planet.level][CommonKeys.REWARDS][CommonKeys.PURCHASING_POWER]}$. You can claim your reward in planet overview.")
            await self.email_use_case.create(email)
            return await self.response_port.publish_response(planet)

        planet.experience += request.experience_amount
        await self.planet_repository_port.update(planet)
        return await self.response_port.publish_response(planet)

    async def claim_pending_lvl_up_reward_sign(self, lvl_up_id: str, user: str):
        lvl_up_claim = await self.lvl_up_repository_port.get(lvl_up_id)

        if lvl_up_claim.completed:
            raise LvlUpAlreadyClaimedException()
        planet = await self.planet_repository_port.get_my_planet(user, lvl_up_claim.planet_id)

        rewards = PlanetLevelData.LEVEL[planet.level][CommonKeys.REWARDS]
        pp_extra = rewards[CommonKeys.PURCHASING_POWER]

        signed_msg = await self.contract_service.sign_message(
            ['address', 'string', 'uint256'],
            [user, lvl_up_id, pp_extra]
        )

        re = ClaimPendingLvlUpRewardResponse(claim_id=lvl_up_id, amount=pp_extra, v=signed_msg['v'], r=signed_msg['r'], s=signed_msg['s'])
        return await self.response_port.publish_response(re)

    async def confirm_pending_lvl_up_reward(self, lvl_up_id: str, user: str) -> LevelUpRewardClaims:
        lvl_up_claim = await self.lvl_up_repository_port.get(lvl_up_id)

        claimed = await self.contract_service.spaceriders_game_call("claimedExtraPurchasingPower", lvl_up_id)

        if not claimed:
            raise LvlUpNotConfirmedSmartContract()

        lvl_up_claim.completed = True
        await self.lvl_up_repository_port.update(lvl_up_claim)
        return await self.response_port.publish_response(lvl_up_claim)

    async def recover_level_up(self, planet_id: str):
        planet = await self.planet_repository_port.get(planet_id)

        for level_up in planet.pending_levelup_reward:
            if level_up.completed:
                continue

            claimed = await self.contract_service.spaceriders_game_call("claimedExtraPurchasingPower", level_up.id)

            if claimed:
                level_up.completed = True

        await self.planet_repository_port.update(planet)
        return await self.response_port.publish_response(planet)

