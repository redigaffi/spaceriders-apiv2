from decouple import config

from adapters.shared.beani_repository_adapter import EnergyDepositRepositoryAdapter
from adapters.shared.logging_adapter import LoggingAdapter, get_logger
from core.planet_energy import PlanetEnergy
from src.core.authenticate import Authenticate
from src.adapters.shared.beani_repository_adapter import BeaniUserRepositoryAdapter, BeaniPlanetRepositoryAdapter
from src.core.buildable_items import BuildableItems
from src.core.fetch_chain_data import FetchChainData
from src.core.get_planets import GetPlanets
from src.core.mint_planet import MintPlanet
from src.adapters.http import HttpResponsePort
from src.adapters.shared.cache_adapter import MemCacheCacheServiceAdapter
from src.adapters.shared.evm_adapter import EvmChainServiceAdapter, TokenPriceAdapter
import emcache
import json
from pathlib import Path
from src.controllers.http import HttpController
from src.core.planet_resources import PlanetResources
from src.core.shared.ports import ChainServicePort, CacheServicePort, TokenPricePort, UserRepositoryPort, \
    PlanetRepositoryPort

http_response_port = HttpResponsePort()
logging_adapter = LoggingAdapter(get_logger("http_app"))


async def cache_dependency():
    cache_driver = config('CACHE_DRIVER')

    client = await emcache.create_client(
        [emcache.MemcachedHostAddress(config('CACHE_HOST'), int(config('CACHE_PORT')))]
    )

    return MemCacheCacheServiceAdapter(client)


async def contract_dependency(cache: CacheServicePort):
    root = Path(__file__).parent.parent.parent
    env = config('ENV')
    rpc_urls = config('RPCS_URL')

    path = str(root) + f"/static/contract_addresses/contracts.{env}.json"
    with open(path, "r") as f:
        contract_addresses = json.loads(f.read())
        spaceriders_token_address: str = contract_addresses[ChainServicePort.SPACERIDERS_TOKEN_CONTRACT]
        spaceriders_game_address: str = contract_addresses[ChainServicePort.SPACERIDERS_GAME_CONTRACT]
        spaceriders_nft_address: str = contract_addresses[ChainServicePort.SPACERIDERS_NFT_CONTRACT]
        spaceriders_ticket_nft_address: str = contract_addresses[ChainServicePort.SPACERIDERS_TICKET_NFT_CONTRACT]

    abi_base_path = str(root) + f"/static/abi"

    with open(f"{abi_base_path}/Spaceriders.json", "r") as f:
        spaceriders_token_abi = json.loads(f.read())

    with open(f"{abi_base_path}/SpaceRidersGame.json", "r") as f:
        spaceriders_game_abi = json.loads(f.read())

    with open(f"{abi_base_path}/SpaceRiderNFT.json", "r") as f:
        spaceriders_nft_abi = json.loads(f.read())

    with open(f"{abi_base_path}/TicketNft.json", "r") as f:
        spaceriders_ticket_nft_abi = json.loads(f.read())

    with open(f"{abi_base_path}/PancakeRouter.json", "r") as f:
        router_abi = json.loads(f.read())

    return EvmChainServiceAdapter(cache, rpc_urls, config('PRIVATE_KEY'), spaceriders_token_address, spaceriders_game_address, spaceriders_nft_address,
                                  spaceriders_ticket_nft_address, spaceriders_token_abi, spaceriders_game_abi,
                                  spaceriders_nft_abi, spaceriders_ticket_nft_abi, router_abi)


async def token_price_dependency(cache: CacheServicePort, contract: ChainServicePort):
    return TokenPriceAdapter(cache, contract)

# Use cases


async def authenticate_use_case(user_repo: UserRepositoryPort):
    return Authenticate(config('SECRET_KEY'), config('ENV'), user_repo, http_response_port)


async def buy_planet_use_case(token_price: TokenPricePort, contract: ChainServicePort, planet_repository: PlanetRepositoryPort):
    return MintPlanet(token_price, contract, config('API_ENDPOINT'), config('PLANET_IMAGES_BUCKET_PATH'), planet_repository, http_response_port)


async def fetch_chain_data_use_case(token_price: TokenPricePort, contract: ChainServicePort):
    return FetchChainData(token_price, contract, config('CHAIN_ID'), config('CHAIN_NAME'), http_response_port)


async def get_planets_use_case(planet_repository: PlanetRepositoryPort):
    return GetPlanets(planet_repository, config('PLANET_IMAGES_BUCKET_PATH'), http_response_port)


async def get_buildable_items_use_case(planet_repository: PlanetRepositoryPort):
    return BuildableItems(planet_repository, http_response_port)


async def get_planet_resources_use_case(planet_repository: PlanetRepositoryPort):
    return PlanetResources(planet_repository, http_response_port)


async def get_planet_energy_use_case(token_price_adapter: TokenPricePort, energy_repository: EnergyDepositRepositoryAdapter, planet_repository: PlanetRepositoryPort, logging_adapter: LoggingAdapter, contract: ChainServicePort):
    return PlanetEnergy(token_price_adapter, energy_repository, planet_repository, logging_adapter, contract, http_response_port)


# Controllers

async def get_middleware():
    planet_repository = BeaniPlanetRepositoryAdapter()
    items_use_case = await get_buildable_items_use_case(planet_repository)
    planet_resources = await get_planet_resources_use_case(planet_repository)
    return items_use_case, planet_resources


async def http_controller():
    user_repository = BeaniUserRepositoryAdapter()
    planet_repository = BeaniPlanetRepositoryAdapter()
    energy_repository = EnergyDepositRepositoryAdapter()

    cache = await cache_dependency()
    contract_service = await contract_dependency(cache)
    token_price = await token_price_dependency(cache, contract_service)

    a = await authenticate_use_case(user_repository)
    b = await buy_planet_use_case(token_price, contract_service, planet_repository)
    d = await fetch_chain_data_use_case(token_price, contract_service)
    e = await get_planets_use_case(planet_repository)
    f = await get_buildable_items_use_case(planet_repository)
    g = await get_planet_energy_use_case(token_price, energy_repository, planet_repository, logging_adapter, contract_service)
    return HttpController(a, b, d, e, f, g)
