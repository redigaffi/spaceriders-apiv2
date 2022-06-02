from controllers.http import HttpController
from core.authenticate import JwtResponse
from core.buildable_items import BuildableResponse
from core.fetch_chain_data import FetchChainDataResponse, FetchChainTokenPriceResponse
from core.get_planets import FetchByPlanetIdResponse
from core.mint_planet import FetchPlanetCostResponse, FetchPlanetCostDataResponse
from core.shared.models import Planet, BuildableItem, EnergyDeposit


async def register_fastapi_routes(http_controller: HttpController) -> list:
    return [
        dict(path="/jwt", response_model=JwtResponse, endpoint=http_controller.jwt, methods=["post"]),

        dict(path="/planet/buy", response_model=Planet, endpoint=http_controller.buy_planet, methods=["post"]),

        dict(path="/planet/claim", response_model=Planet, endpoint=http_controller.claim_planet, methods=["post"]),

        dict(path="/planet/free", response_model=Planet, endpoint=http_controller.mint_free_planet, methods=["post"]),

        dict(path="/planet/fetch_cost", response_model=FetchPlanetCostResponse,
             endpoint=http_controller.fetch_planet_cost, methods=["get"]),

        dict(path="/planet/fetch_cost_data", response_model=FetchPlanetCostDataResponse,
             endpoint=http_controller.fetch_planet_cost_data, methods=["post"]),

        dict(path="/chain", response_model=FetchChainDataResponse, endpoint=http_controller.get_chain_data,
             methods=["get"]),

        dict(path="/chain/tokenprice", response_model=FetchChainTokenPriceResponse,
             endpoint=http_controller.get_chain_token_price, methods=["get"]),

        dict(path=r"/planets", response_model=list[Planet],
             endpoint=http_controller.fetch_all_planets, methods=["get"]),

        dict(path=r"/planet/{planet_id}", response_model=FetchByPlanetIdResponse,
             endpoint=http_controller.fetch_planet_by_id, methods=["get"]),

        dict(path=r"/planet/build", response_model=BuildableResponse,
             endpoint=http_controller.build, methods=["post"]),

        dict(path=r"/planet/energy", response_model=EnergyDeposit,
             endpoint=http_controller.energy_deposit, methods=["post"])
    ]
