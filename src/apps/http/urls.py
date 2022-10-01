from controllers.http import HttpController
from core.authenticate import JwtResponse
from core.buildable_items import BuildableResponse
from core.currency_market import MyOpenOrdersResponse
from core.fetch_chain_data import FetchChainDataResponse, FetchChainTokenPriceResponse
from core.get_planets import FetchByPlanetIdResponse, PlanetResponse, FetchByPlanetPositionRangeResponse
from core.mint_planet import FetchPlanetCostResponse, FetchPlanetCostDataResponse
from core.nft_metadata import OpenseaMetadataNftResponse
from core.planet_bkm import BKMWithdrawResponse
from core.planet_staking import TierInfoResponse, CreateStakingResponse
from core.shared.models import Planet, BuildableItem, EnergyDeposit, PlanetTier, BKMTransaction


async def register_fastapi_routes(http_controller: HttpController) -> list:
    return [
        dict(path="/jwt", response_model=JwtResponse, endpoint=http_controller.jwt, methods=["post"]),

        dict(path="/planet/buy", response_model=PlanetResponse, endpoint=http_controller.buy_planet, methods=["post"]),

        dict(path="/planet/claim", response_model=PlanetResponse, endpoint=http_controller.claim_planet, methods=["post"]),

        dict(path="/planet/cost", response_model=FetchPlanetCostResponse,
             endpoint=http_controller.planet_cost, methods=["get"]),

        dict(path="/planet/cost/sign", response_model=FetchPlanetCostDataResponse,
             endpoint=http_controller.planet_sign_cost_data, methods=["post"]),

        dict(path="/chain", response_model=FetchChainDataResponse, endpoint=http_controller.get_chain_data,
             methods=["get"]),

        dict(path="/chain/tokenprice", response_model=FetchChainTokenPriceResponse,
             endpoint=http_controller.get_chain_token_price, methods=["get"]),

        dict(path=r"/planets", response_model=list[PlanetResponse],
             endpoint=http_controller.fetch_all_planets, methods=["get"]),

        dict(path=r"/planets/{galaxy}/{from_solar_system}/{to_solar_system}", response_model=FetchByPlanetPositionRangeResponse,
             endpoint=http_controller.fetch_planets_by_position, methods=["get"]),

        dict(path=r"/planet/{planet_id}", response_model=FetchByPlanetIdResponse,
             endpoint=http_controller.fetch_planet_by_id, methods=["get"]),

        dict(path=r"/planet/build", response_model=BuildableResponse,
             endpoint=http_controller.build, methods=["post"]),

        dict(path=r"/planet/energy", response_model=EnergyDeposit,
             endpoint=http_controller.energy_deposit, methods=["post"]),

        dict(path=r"/planet/bkm/withdraw", response_model=BKMWithdrawResponse,
             endpoint=http_controller.bkm_withdraw, methods=["post"]),

        dict(path=r"/planet/bkm", response_model=BKMTransaction,
             endpoint=http_controller.bkm_transaction, methods=["post"]),

        dict(path=r"/nft/planet/{planet_id}", response_model=OpenseaMetadataNftResponse,
             endpoint=http_controller.fetch_planet_nft_data, methods=["get"]),

        dict(path=r"/nft/ticket/{token_id}", response_model=OpenseaMetadataNftResponse,
             endpoint=http_controller.fetch_ticket_nft_data, methods=["get"]),

        dict(path=r"/planet/email/{email_id}/read", response_model={},
             endpoint=http_controller.email_mark_as_read, methods=["post"]),

        dict(path=r"/planet/email/{email_id}/delete",
             endpoint=http_controller.email_delete, methods=["post"]),
        
        dict(path=r"/planet/{planet_id}/email",
             endpoint=http_controller.email_delete_all, methods=["delete"]),

        dict(path=r"/planet/staking/info", response_model=dict[str, TierInfoResponse],
             endpoint=http_controller.staking_info, methods=["get"]),

        dict(path=r"/planet/staking/create", response_model=CreateStakingResponse,
             endpoint=http_controller.staking_create, methods=["post"]),

        dict(path=r"/planet/staking/confirm", response_model=PlanetTier,
             endpoint=http_controller.staking_confirm, methods=["post"]),

        dict(path=r"/planet/staking/unstake", response_model=PlanetTier,
             endpoint=http_controller.unstake, methods=["post"]),

        dict(path=r"/currency_market/orders/open/{market_code}/{planet_id}",
             response_model=list[MyOpenOrdersResponse], endpoint=http_controller.currency_market_fetch_open_orders, methods=["get"]),

        dict(path=r"/currency_market/order/{order_id}/close", endpoint=http_controller.currency_market_close_open_order,
             methods=["post"]),

        dict(path=r"/currency_market/all", endpoint=http_controller.fetch_all_market_info,
             methods=["get"]),

        dict(path=r"/health",
             endpoint=http_controller.health, methods=["get"]),
    ]
