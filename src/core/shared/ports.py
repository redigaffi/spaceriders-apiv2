from abc import ABC, abstractmethod
from datetime import datetime

from core.shared.models import OpenOrdersGroupedByPrice, PriceCandleDataGroupedByTimeInterval, Volume24Info
from core.shared.models import User, Planet, EnergyDeposit, Email, LevelUpRewardClaims, ResourceExchange, \
    TokenConversions, CurrencyMarketTrade, CurrencyMarketOrder
from typing import TypedDict, Tuple


class LoggingPort(ABC):
    @abstractmethod
    async def info(self, msg, extra=None):
        pass

    @abstractmethod
    async def error(self, msg, extra=None):
        pass


class TokenConversionsRepositoryPort(ABC):
    @abstractmethod
    async def create(self, token_conversion: TokenConversions) -> TokenConversions:
        pass

    @abstractmethod
    async def get(self, token_conversion: str) -> TokenConversions | None:
        pass

    @abstractmethod
    async def get_latest(self) -> TokenConversions | None:
        pass

    @abstractmethod
    async def update(self, token_conversion: TokenConversions) -> TokenConversions:
        pass


class ResourceExchangeRepositoryPort(ABC):
    @abstractmethod
    async def create(self, resource_exchange: ResourceExchange) -> ResourceExchange:
        pass

    @abstractmethod
    async def get(self, resource_exchange: str) -> ResourceExchange | None:
        pass

    @abstractmethod
    async def get_latest(self) -> ResourceExchange | None:
        pass

    @abstractmethod
    async def update(self, resource_exchange: ResourceExchange) -> ResourceExchange:
        pass


class LevelUpRewardClaimsRepositoryPort(ABC):
    @abstractmethod
    async def create(self, lvl_up: LevelUpRewardClaims) -> LevelUpRewardClaims:
        pass

    @abstractmethod
    async def get(self, lvl_up_id: str) -> LevelUpRewardClaims | None:
        pass

    @abstractmethod
    async def update(self, lvl_up: LevelUpRewardClaims) -> LevelUpRewardClaims:
        pass


class EmailRepositoryPort(ABC):
    @abstractmethod
    async def create(self, email: Email) -> Email:
        pass

    @abstractmethod
    async def update(self, email: Email) -> Email:
        pass

    @abstractmethod
    async def delete(self, email: Email):
        pass

    @abstractmethod
    async def get(self, email_id) -> Email:
        pass


class EnergyDepositRepositoryPort(ABC):
    @abstractmethod
    async def get(self, id: str) -> EnergyDeposit | None:
        pass

    @abstractmethod
    async def create_energy_deposit(self, energy_deposit: EnergyDeposit) -> EnergyDeposit:
        pass


class CurrencyMarketOrderRepositoryPort(ABC):
    @abstractmethod
    async def delete(self, id: str):
        pass

    @abstractmethod
    async def open_orders_grouped_price(self, market_code: str) -> Tuple[list[OpenOrdersGroupedByPrice], list[OpenOrdersGroupedByPrice]]:
        pass

    @abstractmethod
    async def create_order(self, order: CurrencyMarketOrder) -> CurrencyMarketOrder | None:
        pass

    @abstractmethod
    async def find_matching_orders(self, market_code: str, trade_type: str, order_type: str, price: float) -> list[CurrencyMarketOrder]:
        pass

    @abstractmethod
    async def my_open_orders_by_planet(self, market_code: str, planet_id: str) -> list[CurrencyMarketOrder]:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> CurrencyMarketOrder | None:
        pass

    @abstractmethod
    async def update(self, order: CurrencyMarketOrder) -> CurrencyMarketOrder:
        pass


class CurrencyMarketTradeRepositoryPort(ABC):
    @abstractmethod
    async def last_24_info(self, market_code: str) -> Volume24Info:
        pass

    @abstractmethod
    async def price_last_candle_data_grouped_time(self, market_code: str, interval: int) -> list[PriceCandleDataGroupedByTimeInterval]:
        pass

    @abstractmethod
    async def last(self, market_code: str) -> list[CurrencyMarketTrade]:
        pass

    @abstractmethod
    async def price_candle_data_grouped_time_range(self, market_code: str, interval: str, time_start: datetime) -> list[PriceCandleDataGroupedByTimeInterval]:
        pass

    @abstractmethod
    async def price_candle_data_grouped_time(self, market_code: str, time_start: datetime, interval: str) -> list[PriceCandleDataGroupedByTimeInterval]:
        pass

    @abstractmethod
    async def all(self) -> list[CurrencyMarketTrade] | None:
        pass

    @abstractmethod
    async def all_descending_limit_by_day(self, market_code: str) -> list[CurrencyMarketTrade] | None:
        pass

    @abstractmethod
    async def create_trade(self, trade: CurrencyMarketTrade) -> CurrencyMarketTrade | None:
        pass




class UserRepositoryPort(ABC):

    @abstractmethod
    async def all(self) -> list[User] | None:
        pass

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
    async def get_by_request_id(self, request_id: str, fetch_links=False) -> Planet | None:
        pass

    @abstractmethod
    async def all_claimed_planets(self, fetch_links=False) -> list[Planet]:
        pass

    @abstractmethod
    async def update(self, planet: Planet) -> Planet:
        pass

    @abstractmethod
    async def all_user_planets(self, user_id: str, fetch_links=False) -> list[Planet]:
        pass

    @abstractmethod
    async def by_position_range(self, galaxy: int, from_solar_system: int, to_solar_system: int, fetch_links=False) -> list[Planet]:
        pass

    @abstractmethod
    async def get(self, planet_id: str, fetch_links=False) -> Planet | None:
        pass

    @abstractmethod
    async def get_my_planet(self, user_id: str, planet_id: str, fetch_links=False) -> Planet | None:
        pass

    @abstractmethod
    async def has_free_planet(self, user_id: str) -> bool:
        pass

    @abstractmethod
    async def create_planet(self, planet_data: Planet) -> Planet:
        pass

    @abstractmethod
    async def last_created_planet(self, fetch_links=False) -> Planet|bool:
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


class SignedMessageDict(TypedDict):
    v: int
    r: str
    s: str


class ChainServicePort(ABC):
    SPACERIDERS_TOKEN_CONTRACT = "SPACERIDERS_TOKEN_CONTRACT"
    SPACERIDERS_GAME_CONTRACT = "SPACERIDERS_GAME_CONTRACT"
    SPACERIDERS_NFT_CONTRACT = "SPACERIDERS_NFT_CONTRACT"
    SPACERIDERS_TICKET_NFT_CONTRACT = "SPACERIDERS_TICKET_NFT_CONTRACT"

    @abstractmethod
    async def to_wei(self, amount: float) -> int:
        pass

    @abstractmethod
    async def get_rpc_url(self):
        pass

    @abstractmethod
    async def get_contract_address(self, contract_name: str) -> str:
        pass

    @abstractmethod
    async def sign_message(self, types: list, values: list) -> SignedMessageDict:
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
