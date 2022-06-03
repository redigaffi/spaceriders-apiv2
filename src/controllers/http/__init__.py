from dataclasses import dataclass

from core import planet_emails
from core.nft_metadata import NftData
from core.planet_emails import PlanetEmails
from core.planet_energy import PlanetEnergy, EnergyDepositRequest
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


@dataclass
class HttpController:
    authenticate_use_case: Authenticate
    buy_planet_use_case: MintPlanet
    fetch_chain_data: FetchChainData
    get_planets: GetPlanets
    buildable_items: BuildableItems
    planet_energy: PlanetEnergy
    nft_data: NftData
    planet_emails: PlanetEmails

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
        return jsonable_encoder(re)

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
        await self.planet_emails.create("629a3819ea41650638836fb7")

        re = await self.nft_data.planet_nft_view(planet_id)
        return jsonable_encoder(re)

    async def fetch_ticket_nft_data(self, token_id: int):
        re = await self.nft_data.testnet_ticket_nft(token_id)
        return jsonable_encoder(re)

    async def email_mark_as_read(self, email_id: str):
        re = await self.planet_emails.mark_as_read(email_id)
        return jsonable_encoder(re)

    async def email_delete(self, email_id: str):
        re = await self.planet_emails.delete(email_id)
        return jsonable_encoder(re)
