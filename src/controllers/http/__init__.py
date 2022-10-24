from dataclasses import dataclass

from beanie import PydanticObjectId
from bson import ObjectId
from fastapi import Depends
from fastapi.encoders import jsonable_encoder

from adapters.http.security import jwt_bearer
from core.authenticate import Authenticate, AuthenticationDetailsRequest
from core.buildable_items import BuildableItems, BuildableRequest
from core.currency_market import CurrencyMarket, MyOpenOrdersResponse
from core.fetch_chain_data import FetchChainData
from core.get_planets import FetchByPlanetPositionRangeRequest, GetPlanets
from core.mint_planet import (
    ClaimPlanetRequest,
    FetchPlanetCostDataRequest,
    FetchPlanetCostResponse,
    MintPaidPlanetRequest,
    MintPlanet,
)
from core.nft_metadata import NftData
from core.planet_bkm import BKMTransactionRequest, PlanetBKM
from core.planet_email import PlanetEmail
from core.planet_energy import EnergyDepositRequest, PlanetEnergy
from core.planet_staking import (
    ConfirmStakingRequest,
    CreateStakingRequest,
    Staking,
    UnStakeRequest,
)
from core.shared.models import Planet
from core.medium_scraper import MediumScraper

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
    currency_market: CurrencyMarket
    planet_bkm: PlanetBKM
    medium_scrapper: MediumScraper

    async def jwt(self, req: AuthenticationDetailsRequest):
        return await self.authenticate_use_case(req)

    async def buy_planet(
        self, req: MintPaidPlanetRequest, user=Depends(jwt_bearer)
    ) -> Planet:
        re: Planet = await self.buy_planet_use_case.buy_planet(user, req)
        return jsonable_encoder(re)

    async def claim_planet(
        self, req: ClaimPlanetRequest, user=Depends(jwt_bearer)
    ) -> Planet:
        re: Planet = await self.buy_planet_use_case.claim_planet(user, req)
        return jsonable_encoder(re)

    async def planet_cost(self):
        re: FetchPlanetCostResponse = await self.buy_planet_use_case.fetch_planet_cost()
        return jsonable_encoder(re)

    async def planet_sign_cost_data(
        self, request: FetchPlanetCostDataRequest, user=Depends(jwt_bearer)
    ):
        re = await self.buy_planet_use_case.fetch_planet_cost_data(user, request)
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

    async def fetch_planets_by_position(
        self,
        galaxy: int,
        from_solar_system: int,
        to_solar_system: int,
        user=Depends(jwt_bearer),
    ):
        request = FetchByPlanetPositionRangeRequest(
            galaxy=galaxy,
            from_solar_system=from_solar_system,
            to_solar_system=to_solar_system,
        )

        re = await self.get_planets.fetch_by_position_range(request)
        return jsonable_encoder(re)

    async def fetch_planet_by_id(self, planet_id: str, user=Depends(jwt_bearer)):
        re = await self.get_planets.fetch_by_planet_id(user, planet_id)
        return jsonable_encoder(re)

    async def build(self, request: BuildableRequest, user=Depends(jwt_bearer)):
        re = await self.buildable_items.build(user, request)
        return jsonable_encoder(re)

    async def repair(self, request: BuildableRequest, user=Depends(jwt_bearer)):
        re = await self.buildable_items.repair(user, request)
        return jsonable_encoder(re)

    async def energy_deposit(
        self, request: EnergyDepositRequest, user=Depends(jwt_bearer)
    ):
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

    async def email_delete_all(self, planet_id, user=Depends(jwt_bearer)):
        re = await self.planet_emails.delete_all(planet_id)
        return jsonable_encoder(re)

    async def staking_info(self):
        re = await self.staking.tier_info()
        return jsonable_encoder(re)

    async def staking_create(
        self, request: CreateStakingRequest, user=Depends(jwt_bearer)
    ):
        re = await self.staking.create_staking(request, user)
        return jsonable_encoder(re)

    async def staking_confirm(
        self, request: ConfirmStakingRequest, user=Depends(jwt_bearer)
    ):
        re = await self.staking.confirm_staking(request, user)
        return jsonable_encoder(re)

    async def unstake(self, request: UnStakeRequest, user=Depends(jwt_bearer)):
        re = await self.staking.unstake(request, user)
        return jsonable_encoder(re)

    async def currency_market_fetch_open_orders(
        self, market_code: str, planet_id: str
    ) -> list[MyOpenOrdersResponse]:
        re = await self.currency_market.fetch_my_open_orders(market_code, planet_id)
        return jsonable_encoder(re)

    async def currency_market_close_open_order(self, order_id: str):
        re = await self.currency_market.cancel_open_order(order_id)
        return jsonable_encoder(re)

    async def fetch_all_market_info(self):
        re = await self.currency_market.get_all_market_info()
        return jsonable_encoder(re)

    async def bkm_withdraw(
        self, request: BKMTransactionRequest, user=Depends(jwt_bearer)
    ):
        re = await self.planet_bkm.withdraw(user, request)
        return jsonable_encoder(re)

    async def bkm_transaction(
        self, request: BKMTransactionRequest, user=Depends(jwt_bearer)
    ):
        re = await self.planet_bkm.create_transaction(user, request)
        return jsonable_encoder(re)

    async def health(self):
        return jsonable_encoder({})

    async def medium_feed(self):
        re = await self.medium_scrapper.get_medium_feed()
        return jsonable_encoder(re)
