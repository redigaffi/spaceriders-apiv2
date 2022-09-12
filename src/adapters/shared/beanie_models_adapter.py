from __future__ import annotations
from typing import Optional, List
from beanie import Document, Indexed, Link, PydanticObjectId
import pymongo
from datetime import datetime
from core.shared.models import EnergyDeposit, Email, ResourceExchange, TokenConversions, CurrencyMarketOrder, \
    CurrencyMarketTrade
from core.shared.models import User, PlanetTier, Resources, Planet, Reserves, BuildableItem, UserNotFoundException


class TokenConversionsDocument(Document, TokenConversions):
    completed: bool = False
    created_time: float = None
    metal: float = None
    petrol: float = None
    crystal: float = None
    token: float = None

    class Settings:
        name = "token_conversions"
        use_revision = True
        use_state_management = True


class ResourceExchangeDocument(Document, ResourceExchange):
    created_time: float | None = 0
    metal_usd_price: float
    crystal_usd_price: float
    petrol_usd_price: float

    class Settings:
        name = "resource_exchange"
        use_revision = True
        use_state_management = True




class EmailDocument(Document, Email):
    title: str = None
    sub_title: str = None
    template: str = None
    body: str = None
    sender: str = None
    read: bool = False
    planet: str

    # def to_email(self) -> Email:
    #     return Email(id=str(self.id), title=self.title, sub_title=self.sub_title, template=self.template,
    #                                    body=self.body, sender=self.sender, read=self.read, planet=self.planet)
    #
    # @staticmethod
    # def from_email(email: Email):
    #     return EmailDocument(id=PydanticObjectId(email.id), title=email.title, sub_title=email.sub_title, template=email.template,
    #                  body=email.body, sender=email.sender, read=email.read, planet=email.planet)

    class Settings:
        name = "emails"
        use_revision = True
        use_state_management = True


# INFO: Seems like order matters, if I put this below planet it wont create DBRef in db (no reference)
class EnergyDepositDocument(Document, EnergyDeposit):
    request_id: str
    created_time: float | None = 0
    token_amount: float | None = 0
    usd_value: float | None = 0
    planet_id: str
    was_recovered: bool = False

    class Settings:
        name = "energy_deposits"
        use_revision = True
        use_state_management = True


class PlanetDocument(Document, Planet):
    request_id: str = None
    created_at: float

    name: str = "Planet"
    rarity: str = "Common"
    image: str | None = 0
    level: int | None = 0
    experience: int | None = 0
    diameter: int | None = 0
    slots: int | None = 0  # = Diameter/1000
    slots_used: int | None = 0
    min_temperature: int | None = 0
    max_temperature: int | None = 0

    # Original resources reserve
    original_total_metal_amount: int | None = 0
    original_total_crystal_amount: int | None = 0
    original_total_petrol_amount: int | None = 0

    galaxy: int | None = 0
    solar_system: int | None = 0
    position: int | None = 0

    # below works
    user: str

    claimable: float = None  # timestamp
    claimed: bool = False

    tier: PlanetTier = None
    resources: Resources = None

    reserves: Reserves = None
    resources_level: List[BuildableItem] = None
    installation_level: List[BuildableItem] = None
    research_level: List[BuildableItem] = None
    defense_items: List[BuildableItem] = None

    energy_deposits: List[Link[EnergyDepositDocument]] = []
    emails: List[Link[EmailDocument]] = []
    resource_conversions: List[Link[TokenConversionsDocument]] = []

    price_paid: int = 0

    class Settings:
        name = "planets"
        use_revision = True
        use_state_management = True


class UserDocument(Document, User):
    wallet: str
    username: Optional[str] = None

    planets: List[Link[PlanetDocument]] = []

    class Settings:
        name = "user"
        use_revision = True
        use_state_management = True


class CurrencyMarketOrderDocument(Document, CurrencyMarketOrder):
    order_type: str  # buy, sell
    user_id: str
    planet_id: str
    created_time: float | None = None
    updated_time: float | None = None
    market_code: str  # Metal/Petrol - Metal/Spr ...
    price: float
    amount: float
    amount_filled: float
    state: str

    class Settings:
        name = "currency_market_order"
        use_revision = True
        use_state_management = True


class CurrencyMarketTradeDocument(Document, CurrencyMarketTrade):
    market_code: str  # Metal/Petrol - Metal/Spr ...
    price: float = None
    amount: float = None
    created_time: Indexed(datetime)

    class Settings:
        name = "currency_market_trade"
        use_revision = True
        use_state_management = True
