from dataclasses import dataclass
import datetime as dt
import logging as log
import math
import random
from random import random

from pydantic import BaseModel

from core.shared.models import (
    AppBaseException,
    NotMyPlanetException,
    Planet,
    PlanetIdAlreadyExistsException,
    PlanetNameMissingException,
    PlanetResponse,
)
from core.shared.ports import (
    ChainServicePort,
    PlanetRepositoryPort,
    ResponsePort,
    TokenPricePort,
)
from core.shared.service.planet import (
    get_new_planet,
    get_new_random_planet_planet_position,
)
from core.shared.static.game_data.PlanetData import PlanetData


class MintPaidPlanetRequest(BaseModel):
    planet_id: str
    name: str


class ClaimPlanetRequest(BaseModel):
    planet_id: str


class FetchPlanetCostResponse(BaseModel):
    usd_cost: float
    token_cost: float


class FetchPlanetCostDataRequest(BaseModel):
    planet_id: str


class FetchPlanetCostDataResponse(BaseModel):
    planet_id: str
    price: str
    token_uri: str
    v: str
    r: str
    s: str


class FreePlanetRequest(BaseModel):
    name: str


class CantMintMoreFreePlanets(AppBaseException):
    msg = "You already have a free planet"


class PlanetAlreadyClaimed(AppBaseException):
    msg = "Planet already claimed..."


class PlanetNotClaimableYet(AppBaseException):
    msg = "Planet can't be claimed yet..."


class PlanetIdNotFoundSmartContractException(AppBaseException):
    msg = "This planet is not registered in the smart contract..."


@dataclass
class MintPlanet:
    token_price_service: TokenPricePort
    contract_service: ChainServicePort
    api_base_path: str
    planet_images_bucket_path: str
    planet_repository: PlanetRepositoryPort
    response_port: ResponsePort

    async def __planet_cost(self):
        token_price: float = await self.token_price_service.fetch_token_price_usd()
        planet_cost = PlanetData.BUY_PLANET_COST_USD
        token_amount_cost = math.floor(planet_cost / token_price)
        return planet_cost, token_amount_cost

    async def fetch_planet_cost_data(
        self, user: str, request: FetchPlanetCostDataRequest
    ) -> FetchPlanetCostDataResponse:
        """
        Fetches planet cost signed message to allow smart contract to create the planet
        :return:
        """
        planet_cost, token_amount_cost = await self.__planet_cost()

        token_amount_cost_wei = token_amount_cost * 10**18

        planet: Planet = await self.planet_repository.get(request.planet_id)

        if planet is not None:
            raise PlanetIdAlreadyExistsException()

        signed_msg = await self.contract_service.sign_message(
            ["string", "address", "uint256"],
            [request.planet_id, user, token_amount_cost_wei],
        )

        url = f"{self.api_base_path}/nft/planet/{request.planet_id}"
        response = FetchPlanetCostDataResponse(
            planet_id=request.planet_id,
            price=token_amount_cost_wei,
            token_uri=url,
            v=signed_msg["v"],
            r=signed_msg["r"],
            s=signed_msg["s"],
        )

        return await self.response_port.publish_response(response)

    async def fetch_planet_cost(self) -> FetchPlanetCostResponse:
        """
        Fetches Planet cost
        :return
        """
        planet_cost, token_amount_cost = await self.__planet_cost()
        return await self.response_port.publish_response(
            FetchPlanetCostResponse(usd_cost=planet_cost, token_cost=token_amount_cost)
        )

    async def recover_planet(self, user: str):
        user_token_ids = await self.contract_service.spaceriders_nft_call(
            "getTokenIdByOwner", user
        )
        if not user_token_ids:
            return await self.response_port.publish_response({})

        not_stored_planet_ids = []
        for i in user_token_ids:
            tmp_planet = await self.contract_service.spaceriders_nft_call(
                "byTokenIdIdData", i
            )

            exists = await self.planet_repository.get_by_request_id(tmp_planet[1])
            if exists is None:
                not_stored_planet_ids.append(tmp_planet)

        planet_names = ["Mars", "Pluto", "Jupiter"]

        for planet in not_stored_planet_ids:
            planet_id = str(planet[1])

            planet: Planet = await get_new_planet(
                user,
                random.choice(planet_names),
                self.planet_repository,
                PlanetData.BUY_PLANET_COST_USD,
                self.planet_images_bucket_path,
                True,
                True,
            )

            planet.request_id = planet_id
            re = await self.planet_repository.create_planet(planet)

        return await self.response_port.publish_response({})

    async def buy_planet(
        self, user: str, request: MintPaidPlanetRequest
    ) -> PlanetResponse:
        log.info(f"User {user} minting paid planet")

        planet: Planet = await self.planet_repository.get(request.planet_id)

        if planet is not None:
            raise PlanetIdAlreadyExistsException()

        if not request.name:
            raise PlanetNameMissingException()

        nft_token_id = await self.contract_service.spaceriders_nft_call(
            "byPlanetIdData", request.planet_id
        )
        requested_planets_data: list = await self.contract_service.spaceriders_nft_call(
            "byTokenIdIdData", nft_token_id
        )

        exists = bool(requested_planets_data[2])
        owner = str(requested_planets_data[4])

        if not exists:
            raise PlanetIdNotFoundSmartContractException()

        if owner.lower() != user.lower():
            raise NotMyPlanetException()

        claimable = int(dt.datetime.now(dt.timezone.utc).timestamp() + 60)

        # Mint paid planet should have some claim time
        planet: Planet = await get_new_planet(
            user,
            request.name,
            self.planet_repository,
            PlanetData.BUY_PLANET_COST_USD,
            self.planet_images_bucket_path,
            False,
            claimable,
        )

        planet.request_id = request.planet_id
        re = await self.planet_repository.create_planet(planet)

        log.info(f"User {user} minting paid planet finished")
        return await self.response_port.publish_response(PlanetResponse.from_planet(re))

    async def claim_planet(
        self, user: str, request: ClaimPlanetRequest
    ) -> PlanetResponse:
        planet: Planet = await self.planet_repository.get(request.planet_id)

        if planet.claimed:
            raise PlanetAlreadyClaimed()

        if dt.datetime.now(dt.timezone.utc).timestamp() < planet.claimable:
            raise PlanetNotClaimableYet()

        # @TODO: at this point entity from domain should be separated from response
        # or until they fix pydantic python @property...
        planet.set_image_url(self.planet_images_bucket_path)

        planet.claimed = True
        planet.claimable = None
        planet = await self.planet_repository.update(planet)

        return await self.response_port.publish_response(
            PlanetResponse.from_planet(planet)
        )
