from __future__ import annotations
from typing import Optional, List
from beanie import Document, Indexed, Link, PydanticObjectId
import pymongo
from datetime import datetime
from core.shared.models import EnergyDeposit, Email, ResourceExchange, TokenConversions, CurrencyMarketOrder, \
    CurrencyMarketTrade
from core.shared.models import User, PlanetTier, Resources, Planet, Reserves, BuildableItem, UserNotFoundException, \
    LevelUpRewardClaims

# async def to_planet(planet_document: PlanetDocument) -> Planet:
#     planet = Planet()
#     planet.id = str(planet_document.id)
#     planet.created_at = planet_document.created_at
#     planet.name = planet_document.name
#     planet.rarity = planet_document.rarity
#     planet.image = planet_document.image
#     planet.level = planet_document.level
#     planet.experience = planet_document.experience
#     planet.diameter = planet_document.diameter
#     planet.slots = planet_document.slots
#     planet.slots_used = planet_document.slots_used
#     planet.min_temperature = planet_document.min_temperature
#     planet.max_temperature = planet_document.max_temperature
#     planet.original_total_metal_amount = planet_document.original_total_metal_amount
#     planet.original_total_crystal_amount = planet_document.original_total_crystal_amount
#     planet.original_total_petrol_amount = planet_document.original_total_petrol_amount
#     planet.galaxy = planet_document.galaxy
#     planet.solar_system = planet_document.solar_system
#     planet.position = planet_document.position
#     planet.user = planet_document.user
#     planet.claimable = planet_document.claimable
#     planet.claimed = planet_document.claimed
#     planet.tier = planet_document.tier
#     planet.resources = planet_document.resources
#     planet.price_paid = planet_document.price_paid
#     planet.free_tokens = planet_document.free_tokens
#     planet.reserves = planet_document.reserves
#     planet.resources_level = planet_document.resources_level
#     planet.installation_level = planet_document.installation_level
#     planet.research_level = planet_document.research_level
#     planet.defense_items = planet_document.defense_items
#     planet.pending_levelup_reward = planet_document.pending_levelup_reward
#     planet.energy_deposits = [(await x.fetch()).to_energy_deposit() for x in planet_document.energy_deposits if x is not None]
#     planet.emails = [(await x.fetch()).to_email() for x in planet_document.emails if x is not None]
#     planet.pending_levelup_reward = [(await x.fetch()).to_lvl_up() for x in planet_document.pending_levelup_reward if x is not None]
#     planet.resource_conversions = planet_document.resource_conversions
#     return planet

#
# def from_planet(planet: Planet):
#         planet_document = PlanetDocument(user=planet.user, created_at=planet.created_at)
#         planet_document.id = planet.id
#         planet_document.name = planet.name
#         planet_document.rarity = planet.rarity
#         planet_document.image = planet.image
#         planet_document.diameter = planet.diameter
#         planet_document.level = planet.level
#         planet_document.experience = planet.experience
#         planet_document.slots = planet.slots
#         planet_document.slots_used = planet.slots_used
#         planet_document.min_temperature = planet.min_temperature
#         planet_document.max_temperature = planet.max_temperature
#         planet_document.reserves = planet.reserves
#         # self.original_total_metal_amount=planet_data.original_total_metal_amount
#         # self.original_total_crystal_amount=planet_data.original_total_crystal_amount
#         # self.original_total_petrol_amount=planet_data.original_total_petrol_amount
#         planet_document.galaxy = planet.galaxy
#         planet_document.solar_system = planet.solar_system
#         planet_document.position = planet.position
#         planet_document.claimable = planet.claimable
#         planet_document.claimed = planet.claimed
#         planet_document.tier = planet.tier
#         planet_document.resources = planet.resources
#         planet_document.price_paid = planet.price_paid
#         planet_document.free_tokens = planet.free_tokens
#         planet_document.resources_level = planet.resources_level
#         planet_document.installation_level = planet.installation_level
#         planet_document.research_level = planet.research_level
#         planet_document.defense_items = planet.defense_items
#         planet_document.pending_levelup_reward = planet.pending_levelup_reward
#         planet_document.energy_deposits = [EnergyDepositDocument.from_energy_deposit(x) for x in planet.energy_deposits]
#         planet_document.emails = [EmailDocument.from_email(x) for x in planet.emails]
#         planet_document.pending_levelup_reward = [LevelUpRewardClaimsDocument.from_lvl_up(x) for x in planet.pending_levelup_reward]
#         planet_document.resource_conversions = planet.resource_conversions
#
#         return planet_document


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


class LevelUpRewardClaimsDocument(Document, LevelUpRewardClaims):
    level: int = None
    completed: bool = False
    planet_id: str

    # def to_lvl_up(self) -> LevelUpRewardClaims:
    #     return LevelUpRewardClaims(id=str(self.id), level=self.level, completed=self.completed, planet_id=self.planet_id)
    #
    # @staticmethod
    # def from_lvl_up(lvl_up: LevelUpRewardClaims):
    #     return LevelUpRewardClaimsDocument(id=PydanticObjectId(lvl_up.id), level=lvl_up.level, completed=lvl_up.completed, planet_id=lvl_up.planet_id)

    class Settings:
        name = "level_up_reward_claims"
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

    pending_levelup_reward: List[Link[LevelUpRewardClaimsDocument]] = []
    energy_deposits: List[Link[EnergyDepositDocument]] = []
    emails: List[Link[EmailDocument]] = []
    resource_conversions: List[Link[TokenConversionsDocument]] = []

    price_paid: int = 0
    free_tokens: float | None = 0

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
