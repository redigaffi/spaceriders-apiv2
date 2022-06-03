from abc import ABC, abstractmethod
from core.shared.models import User, Planet, EnergyDeposit, Email


class LoggingPort(ABC):
    @abstractmethod
    async def info(self, msg, extra=None):
        pass

    @abstractmethod
    async def error(self, msg, extra=None):
        pass


class EmailRepositoryPort(ABC):
    @abstractmethod
    async def create(self, email: Email) -> Email:
        pass


class EnergyDepositRepositoryPort(ABC):
    @abstractmethod
    async def get(self, id: str) -> EnergyDeposit | None:
        pass

    @abstractmethod
    async def create_energy_deposit(self, energy_deposit: EnergyDeposit) -> EnergyDeposit:
        pass


class UserRepositoryPort(ABC):
    @abstractmethod
    async def find_user(self, wallet: str) -> User:
        pass

    @abstractmethod
    async def find_user_or_throw(self, wallet: str) -> User:
        pass

    @abstractmethod
    async def create_user(self, wallet: str) -> User:
        pass


class PlanetRepositoryPort(ABC):
    @abstractmethod
    async def all_claimed_planets(self) -> list[Planet]:
        pass

    @abstractmethod
    async def update(self, planet: Planet) -> Planet:
        pass

    @abstractmethod
    async def all_user_planets(self, user_id: str) -> list[Planet]:
        pass

    @abstractmethod
    async def get(self, planet_id: str) -> Planet | None:
        pass

    @abstractmethod
    async def get_my_planet(self, user_id: str, planet_id: str) -> Planet | None:
        pass

    @abstractmethod
    async def has_free_planet(self, user_id: str) -> bool:
        pass

    @abstractmethod
    async def create_planet(self, planet_data: Planet) -> Planet:
        pass

    @abstractmethod
    async def last_created_planet(self) -> Planet|bool:
        pass


class ResponsePort(ABC):
    @abstractmethod
    async def publish_response(self, response):
        pass


class CacheServicePort(ABC):
    FASTEST_RPC = "fastest_rpc"

    @abstractmethod
    async def set(self, key: str, value, expiry: int):
        pass

    @abstractmethod
    async def get(self, key: str):
        pass


class ChainServicePort(ABC):
    SPACERIDERS_TOKEN_CONTRACT = "SPACERIDERS_TOKEN_CONTRACT"
    SPACERIDERS_GAME_CONTRACT = "SPACERIDERS_GAME_CONTRACT"
    SPACERIDERS_NFT_CONTRACT = "SPACERIDERS_NFT_CONTRACT"
    SPACERIDERS_TICKET_NFT_CONTRACT = "SPACERIDERS_TICKET_NFT_CONTRACT"

    @abstractmethod
    async def get_rpc_url(self):
        pass

    @abstractmethod
    async def get_contract_address(self, contract_name: str) -> str:
        pass

    @abstractmethod
    async def sign_message(self, types: list, values: list) -> dict:
        pass

    @abstractmethod
    async def router_call(self, func_name, *args):
        pass

    @abstractmethod
    async def spaceriders_token_call(self, func_name, *args):
        pass

    @abstractmethod
    async def spaceriders_nft_call(self, func_name, *args):
        pass

    @abstractmethod
    async def spaceriders_ticket_nft_call(self, func_name, *args):
        pass

    @abstractmethod
    async def spaceriders_game_call(self, func_name, *args):
        pass


class TokenPricePort(ABC):
    @abstractmethod
    async def fetch_token_price_usd(self) -> float:
        pass
