from dataclasses import dataclass

from beanie import PydanticObjectId
from bson import ObjectId

from core import planet_email
from core.nft_metadata import NftData
from core.planet_email import PlanetEmail
from core.planet_energy import PlanetEnergy, EnergyDepositRequest
from core.planet_level import PlanetLevel
from core.planet_resources_conversion import PlanetResourcesConversion, ResourceConvertRequest, \
    ConfirmConversionRequest, RetryConversionRequest
from core.planet_staking import Staking, CreateStakingRequest, ConfirmStakingRequest, UnStakeRequest
from core.shared.models import EnergyDeposit
from adapters.http.security import jwt_bearer
from core.authenticate import Authenticate
from core.buildable_items import BuildableItems, BuildableRequest
from core.fetch_chain_data import FetchChainData
from core.get_planets import GetPlanets
from core.mint_planet import FreePlanetRequest, MintPlanet, MintPaidPlanetRequest, FetchPlanetCostResponse, \
    FetchPlanetCostDataRequest, ClaimPlanetRequest
from core.authenticate import AuthenticationDetailsRequest
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from core.shared.models import Planet


object_id_encoder = {PydanticObjectId: lambda x: str(x)}
object_id_encoder1 = {ObjectId: lambda x: str(x)}


@dataclass
class HttpController:
    authenticate_use_case: Authenticate
    buy_planet_use_case: MintPlanet
    fetch_chain_data: FetchChainData
    get_planets: GetPlanets
    buildable_items: BuildableItems
    planet_energy: PlanetEnergy
    nft_data: NftData
    planet_emails: PlanetEmail
    staking: Staking
    lvl_reward_claim: PlanetLevel
    planet_resource_conversion: PlanetResourcesConversion

    async def jwt(self, req: AuthenticationDetailsRequest):
        return await self.authenticate_use_case(req)

    async def buy_planet(self, req: MintPaidPlanetRequest, user=Depends(jwt_bearer)) -> Planet:
        re: Planet = await self.buy_planet_use_case.buy_planet(user, req)
        return jsonable_encoder(re)

    async def claim_planet(self, req: ClaimPlanetRequest, user=Depends(jwt_bearer)) -> Planet:
        re: Planet = await self.buy_planet_use_case.claim_planet(user, req)
        return jsonable_encoder(re)

    async def planet_cost(self):
        re: FetchPlanetCostResponse = await self.buy_planet_use_case.fetch_planet_cost()
        return jsonable_encoder(re)

    async def planet_sign_cost_data(self, request: FetchPlanetCostDataRequest, user=Depends(jwt_bearer)):
        re = await self.buy_planet_use_case.fetch_planet_cost_data(user, request)
        return jsonable_encoder(re)

    async def mint_free_planet(self, req: FreePlanetRequest, user=Depends(jwt_bearer)) -> Planet:
        re: Planet = await self.buy_planet_use_case.mint_free_planet(user, req)
        return jsonable_encoder(re)

    async def get_chain_data(self):
        re = await self.fetch_chain_data.get_chain_data()
        return jsonable_encoder(re)

    async def get_chain_token_price(self):
        re = await self.fetch_chain_data.get_chain_token_price()
        return jsonable_encoder(re)

    async def fetch_all_planets(self, user=Depends(jwt_bearer)):
        re = await self.get_planets.fetch_all_planets(user)
        return jsonable_encoder(re, custom_encoder=object_id_encoder)

    async def fetch_planet_by_id(self, planet_id: str, user=Depends(jwt_bearer)):
        re = await self.get_planets.fetch_by_planet_id(user, planet_id)
        return jsonable_encoder(re)

    async def build(self, request: BuildableRequest, user=Depends(jwt_bearer)):
        re = await self.buildable_items.build(user, request)
        return jsonable_encoder(re)

    async def energy_deposit(self, request: EnergyDepositRequest, user=Depends(jwt_bearer)):
        re = await self.planet_energy.create_deposit(user, request)
        return jsonable_encoder(re)

    async def fetch_planet_nft_data(self, planet_id: str):
        re = await self.nft_data.planet_nft_view(planet_id)
        return jsonable_encoder(re)

    async def fetch_ticket_nft_data(self, token_id: int):
        re = await self.nft_data.testnet_ticket_nft(token_id)
        return jsonable_encoder(re)

    async def email_mark_as_read(self, email_id: str, user=Depends(jwt_bearer)):
        re = await self.planet_emails.mark_as_read(email_id)
        return jsonable_encoder(re)

    async def email_delete(self, email_id: str, user=Depends(jwt_bearer)):
        re = await self.planet_emails.delete(email_id)
        return jsonable_encoder(re)

    async def staking_info(self):
        re = await self.staking.tier_info()
        return jsonable_encoder(re)

    async def staking_create(self, request: CreateStakingRequest, user=Depends(jwt_bearer)):
        re = await self.staking.create_staking(request, user)
        return jsonable_encoder(re)

    async def staking_confirm(self, request: ConfirmStakingRequest, user=Depends(jwt_bearer)):
        re = await self.staking.confirm_staking(request, user)
        return jsonable_encoder(re)

    async def unstake(self, request: UnStakeRequest, user=Depends(jwt_bearer)):
        re = await self.staking.unstake(request, user)
        return jsonable_encoder(re)

    async def claim_planet_level_reward_sign(self, claim_id: str, user=Depends(jwt_bearer)):
        re = await self.lvl_reward_claim.claim_pending_lvl_up_reward_sign(claim_id, user)
        return jsonable_encoder(re)

    async def confirm_planet_level_reward(self, claim_id: str, user=Depends(jwt_bearer)):
        re = await self.lvl_reward_claim.confirm_pending_lvl_up_reward(claim_id, user)
        return jsonable_encoder(re)

    async def planet_resources_convert_preview(self, planet_id: str, user=Depends(jwt_bearer)):
        re = await self.planet_resource_conversion.preview_conversion(planet_id, user)
        return jsonable_encoder(re)

    async def planet_resources_convert_pending(self, planet_id: str, user=Depends(jwt_bearer)):
        re = await self.planet_resource_conversion.pending_conversions(planet_id, user)
        return jsonable_encoder(re)

    async def planet_resources_convert_sign(self, request: ResourceConvertRequest, user=Depends(jwt_bearer)):
        re = await self.planet_resource_conversion.convert_conversion(request, user)
        return jsonable_encoder(re)

    async def planet_resources_convert_confirm(self, request: ConfirmConversionRequest, user=Depends(jwt_bearer)):
        re = await self.planet_resource_conversion.confirm_conversion(request, user)
        return jsonable_encoder(re)

    async def planet_resources_convert_retry(self, request: RetryConversionRequest, user=Depends(jwt_bearer)):
        re = await self.planet_resource_conversion.retry_conversion(request, user)
        return jsonable_encoder(re)

    async def health(self):
        return jsonable_encoder({})
