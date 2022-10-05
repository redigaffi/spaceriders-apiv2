from dataclasses import dataclass
from datetime import datetime
import math

from pydantic import BaseModel

from core.shared.models import AppBaseException, Email, PlanetResponse, PlanetTier
from core.shared.ports import (
    ChainServicePort,
    EmailRepositoryPort,
    PlanetRepositoryPort,
    ResponsePort,
    TokenPricePort,
)
from core.shared.static.game_data.StakingData import StakingBenefits, StakingData


class TierInfoResponse(BaseModel):
    token_cost: float = None
    name: str = None
    tokens_time_locked: float = None
    benefit_lines: list[str] = []


class CreateStakingRequest(BaseModel):
    tier_code: str
    planet_id: str


class ConfirmStakingRequest(BaseModel):
    planet_id: str


class UnStakeRequest(BaseModel):
    planet_id: str


class CreateStakingResponse(BaseModel):
    planet_id: str = None
    amount: float = None
    tier: str = None
    time_release: float = None
    v: int = None
    r: str = None
    s: str = None
    router: str = None


class PlanetAlreadyStakedException(AppBaseException):
    msg = "Already staking, wait until your other stake finishes"


class TierNotFoundException(AppBaseException):
    msg = "Tier doesn't exists"


class StakeTier0Exception(AppBaseException):
    msg = "Cant stake TIER 0"


class NotEnoughSprBalanceException(AppBaseException):
    msg = "Not holding enough $BKM (in usd value)"


class NotStakedException(AppBaseException):
    msg = "Not staked..."


class StakingTimeAlreadyPassedException(AppBaseException):
    msg = "Staking time has already passed, please unstake your LP"


class NotStakingOwnerException(AppBaseException):
    msg = "Not the owner..."


class StakingTimeHasntPassedException(AppBaseException):
    msg = "Can't unstake yet, time hasn't pased..."


@dataclass
class Staking:
    planet_repository_port: PlanetRepositoryPort
    token_price_port: TokenPricePort
    chain_service_port: ChainServicePort
    response_port: ResponsePort

    async def tier_info(self):
        current_token_price = await self.token_price_port.fetch_token_price_usd()
        re = {}
        for stake_code in StakingData.TIERS:
            tmp = TierInfoResponse()
            if stake_code == StakingData.TIER_0:
                continue

            staking_data: StakingBenefits = StakingData.DATA[stake_code]

            tier_cost_usd = staking_data.usd_cost
            token_price = tier_cost_usd / current_token_price

            tmp.token_cost = f"{round(token_price, 2):.2f}"
            tmp.name = StakingData.TIER_NAMES[stake_code]
            tmp.tokens_time_locked = staking_data.tokens_time_locked

            # tmp.benefit_lines.append(f"{staking_data.max_queue} items in queue simultaneously")
            # tmp.benefit_lines.append(f"{staking_data.discount_items}% discount on all in-game purchases")
            # tmp.benefit_lines.append(f"{staking_data.experience_boost}% experience boost")
            re[stake_code] = tmp

        return await self.response_port.publish_response(re)

    async def create_staking(
        self, request: CreateStakingRequest, user: str
    ) -> CreateStakingResponse:
        planet = await self.planet_repository_port.get_my_planet(
            user, request.planet_id
        )

        if planet.tier.staked:
            raise PlanetAlreadyStakedException()

        if request.tier_code not in StakingData.TIERS:
            raise TierNotFoundException()

        if request.tier_code == StakingData.TIER_0:
            raise StakeTier0Exception()

        user_token_balance_raw = await self.chain_service_port.spaceriders_token_call(
            "balanceOf", user
        )
        user_token_balance = user_token_balance_raw / 10**18

        current_token_price = await self.token_price_port.fetch_token_price_usd()
        total_usd_amount = user_token_balance * current_token_price

        tier_data = StakingData.DATA[request.tier_code]

        if total_usd_amount < tier_data.usd_cost:
            raise NotEnoughSprBalanceException()

        token_amount_cost = math.floor(tier_data.usd_cost / current_token_price)
        token_amount_cost_crypto = token_amount_cost * 10**18

        now = int(datetime.timestamp(datetime.now()))
        time_release = now + tier_data.tokens_time_locked

        signed_message = await self.chain_service_port.sign_message(
            ["string", "uint256", "string", "uint256"],
            [
                request.planet_id,
                token_amount_cost_crypto,
                request.tier_code,
                time_release,
            ],
        )

        response = CreateStakingResponse(
            planet_id=request.planet_id,
            amount=token_amount_cost_crypto,
            tier=request.tier_code,
            time_release=time_release,
            v=signed_message["v"],
            r=signed_message["r"],
            s=signed_message["s"],
            router=await self.chain_service_port.get_contract_address(
                self.chain_service_port.ROUTER_CONTRACT
            ),
        )

        return await self.response_port.publish_response(response)

    async def confirm_staking(
        self, request: ConfirmStakingRequest, user: str
    ) -> PlanetTier:
        planet = await self.planet_repository_port.get_my_planet(
            user, request.planet_id
        )

        if planet.tier.staked:
            raise PlanetAlreadyStakedException()

        info = await self.chain_service_port.spaceriders_game_call(
            "userStaking", request.planet_id
        )
        staked = info[6]

        if not staked:
            raise NotStakedException()

        time_release_timestamp = info[5]
        now = int(datetime.timestamp(datetime.now()))

        if now > time_release_timestamp:
            planet.tier.tier_code = StakingData.TIER_0
            planet.tier.tier_name = StakingData.TIER_NAMES[StakingData.TIER_0]
            await self.planet_repository_port.update(planet)
            raise StakingTimeAlreadyPassedException()

        owner: str = info[0]

        if owner.lower() != user.lower():
            raise NotStakingOwnerException()

        amount = info[2]
        tier = info[3]

        if tier not in StakingData.TIERS:
            raise TierNotFoundException()

        tokens = int(amount) / 10**18
        current_token_price = await self.token_price_port.fetch_token_price_usd()
        usd_value = tokens * current_token_price

        planet.tier.tier_code = tier
        planet.tier.tier_name = StakingData.TIER_NAMES[tier]
        planet.tier.token_amount = tokens
        planet.tier.time_release = time_release_timestamp
        planet.tier.staked = staked
        planet = await self.planet_repository_port.update(planet)

        return await self.response_port.publish_response(planet.tier)

    async def unstake(self, request: UnStakeRequest, user: str):
        planet = await self.planet_repository_port.get_my_planet(
            user, request.planet_id
        )

        if not planet.tier.staked:
            raise NotStakedException()

        now = int(datetime.timestamp(datetime.now()))
        if planet.tier.time_release > now:
            raise StakingTimeHasntPassedException()

        planet.tier.tier_code = StakingData.TIER_0
        planet.tier.tier_name = StakingData.TIER_NAMES[StakingData.TIER_0]
        planet.tier.token_amount = 0
        planet.tier.time_release = None
        planet.tier.staked = False
        planet = await self.planet_repository_port.update(planet)
        planet = await self.planet_repository_port.get_my_planet(
            user, request.planet_id, True
        )
        re = PlanetResponse.from_planet(planet)
        return await self.response_port.publish_response(re)

    async def tier_expired_reset(self, planet_id: str):
        """
        Resets user tier in case it has finished but user has not withdrawn yet.
        :param planet_id:
        :return:
        """
        planet = await self.planet_repository_port.get(planet_id)

        now = int(datetime.timestamp(datetime.now()))
        if planet.tier.staked and planet.tier.time_release < now:
            planet.tier.tier_code = StakingData.TIER_0
            planet.tier.tier_name = StakingData.TIER_NAMES[StakingData.TIER_0]
            planet = await self.planet_repository_port.update(planet)

        return await self.response_port.publish_response(planet.tier)

    async def tier_recover(self, planet_id: str):
        """
        Recover tier in case tx got submitted but API is not up-to-date.
        :return:
        """
        planet = await self.planet_repository_port.get(planet_id)
        staking_data = await self.chain_service_port.spaceriders_game_call(
            "userStaking", planet_id
        )

        owner = staking_data[0]
        planet_id = staking_data[1]
        amount = staking_data[2]
        tier_code_sm = staking_data[3]
        time = staking_data[4]
        time_release = staking_data[5]
        staked = staking_data[6]

        if not staked:
            return await self.response_port.publish_response(planet.tier)

        if not planet.tier.staked or tier_code_sm != planet.tier.tier_code:
            planet.tier.staked = True
            planet.tier.tier_code = tier_code_sm
            planet.tier.tier_name = StakingData.TIER_NAMES[tier_code_sm]
            planet.tier.time_release = time_release
            planet.tier.token_amount = amount / 10**18
            await self.planet_repository_port.update(planet)

        return await self.response_port.publish_response(planet.tier)
