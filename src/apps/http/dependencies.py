from decouple import config

from adapters.shared.beani_repository_adapter import EnergyDepositRepositoryAdapter, EmailRepositoryAdapter
from adapters.shared.logging_adapter import LoggingAdapter, get_logger
from core.nft_metadata import NftData
from core.planet_emails import PlanetEmails
from core.planet_energy import PlanetEnergy
from core.authenticate import Authenticate
from adapters.shared.beani_repository_adapter import BeaniUserRepositoryAdapter, BeaniPlanetRepositoryAdapter
from core.buildable_items import BuildableItems
from core.fetch_chain_data import FetchChainData
from core.get_planets import GetPlanets
from core.mint_planet import MintPlanet
from adapters.http import HttpResponsePort
from adapters.shared.cache_adapter import MemCacheCacheServiceAdapter
from adapters.shared.evm_adapter import EvmChainServiceAdapter, TokenPriceAdapter
import emcache
import json
from pathlib import Path
from controllers.http import HttpController
from core.planet_resources import PlanetResources
from core.shared.ports import ChainServicePort, CacheServicePort, TokenPricePort, UserRepositoryPort, \
    PlanetRepositoryPort, EmailRepositoryPort

http_response_port = HttpResponsePort()
logging_adapter = LoggingAdapter(get_logger("http_app"))


async def cache_dependency():
    cache_driver = config('CACHE_DRIVER')

    client = await emcache.create_client(
        [emcache.MemcachedHostAddress(config('CACHE_HOST'), int(config('CACHE_PORT')))]
    )

    return MemCacheCacheServiceAdapter(client)


async def contract_dependency(cache: CacheServicePort, rpc_urls: str):
    root = Path(__file__).parent.parent.parent
    env = config('ENV')

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

    return EvmChainServiceAdapter(cache, rpc_urls, config('PRIVATE_KEY'), spaceriders_token_address,
                                  spaceriders_game_address, spaceriders_nft_address,
                                  spaceriders_ticket_nft_address, spaceriders_token_abi, spaceriders_game_abi,
                                  spaceriders_nft_abi, spaceriders_ticket_nft_abi, router_abi)


async def token_price_dependency(cache: CacheServicePort, contract: ChainServicePort):
    return TokenPriceAdapter(cache, contract)


# Use cases


async def authenticate_use_case(user_repo: UserRepositoryPort):
    return Authenticate(config('SECRET_KEY'), config('ENV'), user_repo, http_response_port)


async def buy_planet_use_case(token_price: TokenPricePort, contract: ChainServicePort,
                              planet_repository: PlanetRepositoryPort):
    return MintPlanet(token_price, contract, config('API_ENDPOINT'), config('PLANET_IMAGES_BUCKET_PATH'),
                      planet_repository, http_response_port)


async def fetch_chain_data_use_case(token_price: TokenPricePort, contract: ChainServicePort):
    return FetchChainData(token_price, contract, config('CHAIN_ID'), config('CHAIN_NAME'), http_response_port)


async def get_planets_use_case(planet_repository: PlanetRepositoryPort):
    return GetPlanets(planet_repository, config('PLANET_IMAGES_BUCKET_PATH'), http_response_port)


async def get_buildable_items_use_case(planet_repository: PlanetRepositoryPort):
    return BuildableItems(planet_repository, http_response_port)


async def get_planet_resources_use_case(planet_repository: PlanetRepositoryPort):
    return PlanetResources(planet_repository, http_response_port)


async def get_planet_energy_use_case(token_price_adapter: TokenPricePort,
                                     energy_repository: EnergyDepositRepositoryAdapter,
                                     planet_repository: PlanetRepositoryPort, logging_adapter: LoggingAdapter,
                                     contract: ChainServicePort):
    return PlanetEnergy(token_price_adapter, energy_repository, planet_repository, logging_adapter, contract,
                        http_response_port)


async def nft_data_use_case(api_endpoint: str, planet_images_base_url: str, testnet_ticket_images_base_url: str,
                            planet_repository_port: PlanetRepositoryPort, contract_testnet: ChainServicePort):
    return NftData(api_endpoint, planet_images_base_url, testnet_ticket_images_base_url, planet_repository_port, contract_testnet, http_response_port)


async def get_email_use_case(planet_repository_port: PlanetRepositoryPort, email_repository_port: EmailRepositoryPort):
    return PlanetEmails(planet_repository_port, email_repository_port, http_response_port)

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
    email_repository = EmailRepositoryAdapter()

    cache = await cache_dependency()
    contract_service = await contract_dependency(cache, config('RPCS_URL'))
    contract_mainnet_service = await contract_dependency(cache, config('RPCS_URL_MAINNET'))

    token_price = await token_price_dependency(cache, contract_service)

    a = await authenticate_use_case(user_repository)
    b = await buy_planet_use_case(token_price, contract_service, planet_repository)
    c = await fetch_chain_data_use_case(token_price, contract_service)
    d = await get_planets_use_case(planet_repository)
    e = await get_buildable_items_use_case(planet_repository)
    f = await get_planet_energy_use_case(token_price, energy_repository, planet_repository, logging_adapter,
                                         contract_service)

    nft_contract_service = contract_service
    if config('ENV') == "testnet":
        nft_contract_service = contract_mainnet_service

    g = await nft_data_use_case(config('API_ENDPOINT'), config('PLANET_IMAGES_BUCKET_PATH'), config('TESTNET_TICKET_IMAGES_BUCKET_PATH'),
                                planet_repository, nft_contract_service)

    h = await get_email_use_case(planet_repository, email_repository)
    return HttpController(a, b, c, d, e, f, g, h)
