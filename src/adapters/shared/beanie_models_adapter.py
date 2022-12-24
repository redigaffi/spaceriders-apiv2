from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from beanie import Document, Indexed, Link, PydanticObjectId

from core.shared.models import (
    BKMTransaction,
    BuildableItem,
    CurrencyMarketOrder,
    CurrencyMarketTrade,
    Email,
    EnergyDeposit,
    Planet,
    PlanetTier,
    Reserves,
    Resources,
    User,
    UserNotFoundException, BuildingQueueItem, BuildingQueue,
)


class EmailDocument(Document, Email):
    title: str = None
    sub_title: str = None
    template: str = None
    body: str = None
    sender: str = None
    read: bool = False
    planet: str
    topic: str = None

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

    created_time: float | None = 0
    energy_amount: float = None
    planet_id: str

    class Settings:
        name = "energy_deposits"
        use_revision = True
        use_state_management = True


class BKMTransactionDocument(Document, BKMTransaction):
    request_id: str
    created_time: float | None = 0
    token_amount: float | None = 0
    usd_value: float | None = 0
    planet_id: str
    was_recovered: bool = False
    type: str

    class Settings:
        name = "bkm_deposits"
        use_revision = True
        use_state_management = True


class PlanetDocument(Document, Planet):
    request_id: str = None
    created_at: float

    name: str = "Planet"
    rarity: str = "Common"
    image: str | None = 0
    type: str | None = ""
    level: int | None = 0
    experience: int | None = 0
    diameter: int | None = 0
    slots: int | None = 0  # = Diameter/1000
    slots_used: int | None = 0
    min_temperature: int | None = 0
    max_temperature: int | None = 0

    is_favourite: bool = False

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
    resources_level: list[BuildableItem] = None
    installation_level: list[BuildableItem] = None
    research_level: list[BuildableItem] = None
    defense_items: list[BuildableItem] = None

    building_queue: BuildingQueue = None
    energy_deposits: list[Link[EnergyDepositDocument]] = []
    bkm_deposits: list[Link[BKMTransactionDocument]] = []
    emails: list[Link[EmailDocument]] = []

    price_paid: int = 0

    class Settings:
        name = "planets"
        use_revision = True
        use_state_management = True


class UserDocument(Document, User):
    wallet: str
    username: str | None = ""
    level: int | None = 0
    experience: int | None = 0
    planets: list[Link[PlanetDocument]] = []

    daily_login_next_reward_timer: int | None = None
    daily_login_streak: int | None = None

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
