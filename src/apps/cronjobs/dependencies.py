import json
from pathlib import Path

from decouple import config
import emcache

from adapters.cronjobs import BlackHoleResponsePort
from adapters.shared.beani_repository_adapter import (
    BeaniPlanetRepositoryAdapter,
    BeaniUserRepositoryAdapter,
    BKMDepositRepositoryAdapter,
    EmailRepositoryAdapter,
    EnergyDepositRepositoryAdapter,
)
from adapters.shared.cache_adapter import MemCacheCacheServiceAdapter
from adapters.shared.evm_adapter import EvmChainServiceAdapter, TokenPriceAdapter
from adapters.shared.logging_adapter import LoggingAdapter, get_logger
from controllers.cronjobs import CronjobController
from core.mint_planet import MintPlanet
from core.planet_bkm import PlanetBKM
from core.planet_email import PlanetEmail
from core.planet_energy import PlanetEnergy
from core.experience_points import ExperiencePoints
from core.planet_staking import Staking
from core.pve.asteroid import Asteroid
from core.pve.space_pirates import SpacePirates
from core.shared.ports import CacheServicePort, ChainServicePort

response_adapter = BlackHoleResponsePort()
logging_adapter = LoggingAdapter(get_logger("cronjobs_app"))


async def cache_dependency():

    client = await emcache.create_client(
        [emcache.MemcachedHostAddress(config("CACHE_HOST"), int(config("CACHE_PORT")))]
    )

    return MemCacheCacheServiceAdapter(client)


async def contract_dependency(cache: CacheServicePort):
    root = Path(__file__).parent.parent.parent
    env = config("ENV")
    rpc_urls = config("RPCS_URL")

    path = str(root) + f"/static/contract_addresses/contracts.{env}.json"
    with open(path) as f:
        contract_addresses = json.loads(f.read())
        spaceriders_token_address: str = contract_addresses[
            ChainServicePort.SPACERIDERS_TOKEN_CONTRACT
        ]
        spaceriders_game_address: str = contract_addresses[
            ChainServicePort.SPACERIDERS_GAME_CONTRACT
        ]
        spaceriders_nft_address: str = contract_addresses[
            ChainServicePort.SPACERIDERS_NFT_CONTRACT
        ]
        spaceriders_ticket_nft_address: str = contract_addresses[
            ChainServicePort.SPACERIDERS_TICKET_NFT_CONTRACT
        ]
        router_address: str = contract_addresses[ChainServicePort.ROUTER_CONTRACT]
        busd_address: str = contract_addresses[ChainServicePort.BUSD_CONTRACT]
        pair_address: str = contract_addresses[ChainServicePort.PAIR_CONTRACT]

    abi_base_path = str(root) + f"/static/abi"

    with open(f"{abi_base_path}/Spaceriders.json") as f:
        spaceriders_token_abi = json.loads(f.read())

    with open(f"{abi_base_path}/SpaceRidersGame.json") as f:
        spaceriders_game_abi = json.loads(f.read())

    with open(f"{abi_base_path}/SpaceRiderNFT.json") as f:
        spaceriders_nft_abi = json.loads(f.read())

    with open(f"{abi_base_path}/TicketNft.json") as f:
        spaceriders_ticket_nft_abi = json.loads(f.read())

    with open(f"{abi_base_path}/PancakeRouter.json") as f:
        router_abi = json.loads(f.read())

    return EvmChainServiceAdapter(
        cache,
        rpc_urls,
        config("PRIVATE_KEY"),
        spaceriders_token_address,
        spaceriders_game_address,
        spaceriders_nft_address,
        spaceriders_ticket_nft_address,
        router_address,
        busd_address,
        pair_address,
        spaceriders_token_abi,
        spaceriders_game_abi,
        spaceriders_nft_abi,
        spaceriders_ticket_nft_abi,
        router_abi,
    )


user_repository = BeaniUserRepositoryAdapter()
planet_repository = BeaniPlanetRepositoryAdapter()
energy_repository = EnergyDepositRepositoryAdapter()
email_repository = EmailRepositoryAdapter()
bkm_repository = BKMDepositRepositoryAdapter()


async def cronjob_controller():
    cache = await cache_dependency()
    contract = await contract_dependency(cache)
    token_price_adapter = TokenPriceAdapter(cache, contract)

    energy_planet_use_case = PlanetEnergy(
        token_price_adapter,
        energy_repository,
        planet_repository,
        logging_adapter,
        contract,
        response_adapter,
    )
    staking_use_case = Staking(
        planet_repository, token_price_adapter, contract, response_adapter
    )

    email_use_case = PlanetEmail(planet_repository, email_repository, response_adapter)
    planet_level = ExperiencePoints(
        planet_repository, email_use_case, contract, response_adapter
    )

    planet_mint = MintPlanet(
        token_price_adapter,
        contract,
        config("API_ENDPOINT"),
        config("PLANET_IMAGES_BUCKET_PATH"),
        planet_repository,
        response_adapter,
    )

    asteroid_pve = Asteroid(
        planet_repository, planet_level, email_use_case, response_adapter
    )
    space_pirate_pve = SpacePirates(
        planet_repository, planet_level, email_use_case, response_adapter
    )

    planet_bkm = PlanetBKM(
        bkm_repository, planet_repository, logging_adapter, contract, response_adapter
    )

    return CronjobController(
        energy_planet_use_case,
        staking_use_case,
        planet_level,
        planet_mint,
        asteroid_pve,
        space_pirate_pve,
        planet_bkm,
    )
