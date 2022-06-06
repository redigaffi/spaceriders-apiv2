from adapters.cronjobs import BlackHoleResponsePort
from adapters.shared.beani_repository_adapter import BeaniUserRepositoryAdapter, BeaniPlanetRepositoryAdapter, \
    EnergyDepositRepositoryAdapter, LevelUpRewardClaimsRepositoryAdapter, EmailRepositoryAdapter, \
    ResourceExchangeRepositoryAdapter
from adapters.shared.cache_adapter import MemCacheCacheServiceAdapter
from adapters.shared.evm_adapter import EvmChainServiceAdapter, TokenPriceAdapter
from adapters.shared.logging_adapter import LoggingAdapter, get_logger
from controllers.cronjobs import CronjobController
from core.mint_planet import MintPlanet
from core.planet_email import PlanetEmail
from core.planet_energy import PlanetEnergy
from decouple import config
import emcache
import json
from pathlib import Path

from core.planet_level import PlanetLevel
from core.planet_staking import Staking
from core.pve.asteroid import Asteroid
from core.resource_exchange import ResourcesExchange
from core.shared.ports import CacheServicePort, ChainServicePort, TokenPricePort

response_adapter = BlackHoleResponsePort()
logging_adapter = LoggingAdapter(get_logger("cronjobs_app"))


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


user_repository = BeaniUserRepositoryAdapter()
planet_repository = BeaniPlanetRepositoryAdapter()
energy_repository = EnergyDepositRepositoryAdapter()
lvl_up_repository = LevelUpRewardClaimsRepositoryAdapter()
email_repository = EmailRepositoryAdapter()
resource_repository = ResourceExchangeRepositoryAdapter()

async def cronjob_controller():
    cache = await cache_dependency()
    contract = await contract_dependency(cache)
    token_price_adapter = TokenPriceAdapter(cache, contract)

    energy_planet_use_case = PlanetEnergy(token_price_adapter, energy_repository, planet_repository, logging_adapter, contract, response_adapter)
    staking_use_case = Staking(planet_repository, token_price_adapter, contract, response_adapter)

    email_use_case = PlanetEmail(planet_repository, email_repository, response_adapter)
    planet_level = PlanetLevel(planet_repository, lvl_up_repository, email_use_case, contract, response_adapter)
    resource_exchange = ResourcesExchange(resource_repository, response_adapter)

    planet_mint = MintPlanet(token_price_adapter, contract, config('API_ENDPOINT'), config('PLANET_IMAGES_BUCKET_PATH'),
                      planet_repository, response_adapter)

    asteroid_pve = Asteroid(planet_repository, planet_level, email_use_case, response_adapter)
    return CronjobController(energy_planet_use_case, staking_use_case, planet_level, resource_exchange, planet_mint, asteroid_pve)
