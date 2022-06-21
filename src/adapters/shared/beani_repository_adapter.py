from __future__ import annotations

from typing import Any, Tuple

from beanie import PydanticObjectId, WriteRules, DeleteRules
from pydantic import BaseModel

from adapters.shared.beanie_models_adapter import EnergyDepositDocument, PlanetDocument, UserDocument, EmailDocument, \
    LevelUpRewardClaimsDocument, ResourceExchangeDocument, TokenConversionsDocument, CurrencyMarketTradeDocument, \
    CurrencyMarketOrderDocument
from core.shared.models import OpenOrdersGroupedByPrice, PriceCandleDataGroupedByTimeInterval, Volume24Info
from core.shared.ports import UserRepositoryPort, PlanetRepositoryPort, EnergyDepositRepositoryPort, \
    EmailRepositoryPort, LevelUpRewardClaimsRepositoryPort, ResourceExchangeRepositoryPort, \
    TokenConversionsRepositoryPort, CurrencyMarketTradeRepositoryPort, CurrencyMarketOrderRepositoryPort
from core.shared.models import User, PlanetTier, Planet, UserNotFoundException, \
    LevelUpRewardClaims, EnergyDeposit, Email, ResourceExchange, TokenConversions, CurrencyMarketTrade, \
    CurrencyMarketOrder
from datetime import datetime
from beanie.operators import In


class TokenConversionsRepositoryAdapter(TokenConversionsRepositoryPort):
    async def create(self, token_conversion: TokenConversions) -> TokenConversions:
        # TokenConversionsDocument.update_forward_refs()
        token_conversion_doc = TokenConversionsDocument(completed=token_conversion.completed,
                                                        created_time=token_conversion.created_time,
                                                        metal=token_conversion.metal,
                                                        petrol=token_conversion.petrol,
                                                        crystal=token_conversion.crystal,
                                                        token=token_conversion.token)

        await token_conversion_doc.save()
        return token_conversion_doc

    async def get(self, token_conversion: str) -> TokenConversions | None:
        # TokenConversionsDocument.update_forward_refs()

        return await TokenConversionsDocument.find_one(
            TokenConversionsDocument.id == PydanticObjectId(token_conversion))

    async def get_latest(self) -> TokenConversions | None:
        TokenConversionsDocument.update_forward_refs()

        last_conversion = await TokenConversionsDocument.all().sort(-TokenConversionsDocument.created_time).limit(
            1).to_list()

        if len(last_conversion) > 0:
            return last_conversion[0]

    async def update(self, token_conversion: TokenConversionsDocument) -> TokenConversions:
        TokenConversionsDocument.update_forward_refs()

        await token_conversion.save_changes()
        return token_conversion


class ResourceExchangeRepositoryAdapter(ResourceExchangeRepositoryPort):
    async def create(self, resource_exchange: ResourceExchange) -> ResourceExchange:
        resource_exchange_doc = ResourceExchangeDocument(created_time=resource_exchange.created_time,
                                                         metal_usd_price=resource_exchange.metal_usd_price,
                                                         crystal_usd_price=resource_exchange.crystal_usd_price,
                                                         petrol_usd_price=resource_exchange.petrol_usd_price)

        await resource_exchange_doc.save()
        return resource_exchange_doc

    async def get(self, resource_exchange: str) -> ResourceExchange | None:
        return await ResourceExchangeDocument.get(PydanticObjectId(resource_exchange))

    async def get_latest(self) -> ResourceExchange | None:
        last_price = await ResourceExchangeDocument.all().sort(-ResourceExchangeDocument.created_time).limit(
            1).to_list()

        if len(last_price) > 0:
            return last_price[0]

    async def update(self, resource_exchange: ResourceExchangeDocument) -> ResourceExchange:
        await resource_exchange.save_changes()
        return resource_exchange


class LevelUpRewardClaimsRepositoryAdapter(LevelUpRewardClaimsRepositoryPort):
    async def create(self, lvl_up: LevelUpRewardClaims) -> LevelUpRewardClaims:
        lvl_up_document = LevelUpRewardClaimsDocument(level=lvl_up.level, completed=lvl_up.completed,
                                                      planet_id=lvl_up.planet_id)
        await lvl_up_document.save()
        return lvl_up_document

    async def get(self, lvl_up_id: str) -> LevelUpRewardClaims | None:
        return await LevelUpRewardClaimsDocument.get(PydanticObjectId(lvl_up_id))

    async def update(self, lvl_up: LevelUpRewardClaimsDocument) -> LevelUpRewardClaims:
        await lvl_up.save_changes()
        return lvl_up


class EmailRepositoryAdapter(EmailRepositoryPort):
    async def create(self, email: Email) -> Email:
        email_document = EmailDocument(title=email.title, sub_title=email.sub_title, template=email.template,
                                       body=email.body, sender=email.sender, read=email.read, planet=email.planet)

        await email_document.save()
        return email_document

    async def update(self, email: EmailDocument) -> Email:
        await email.save_changes()
        return email

    async def delete(self, email: Email):
        email_document: EmailDocument = await EmailDocument.get(PydanticObjectId(email.id))
        planet = await PlanetDocument.get(PydanticObjectId(email.planet))
        await planet.fetch_link(PlanetDocument.emails)
        planet.emails = [x for x in planet.emails if str(x.id) != email.id]

        await planet.save_changes()
        await email_document.delete(link_rule=DeleteRules.DELETE_LINKS)

    async def get(self, email_id) -> Email:
        email = await EmailDocument.get(PydanticObjectId(email_id))
        return email


class EnergyDepositRepositoryAdapter(EnergyDepositRepositoryPort):

    async def get(self, id: str) -> EnergyDeposit | None:
        return await EnergyDepositDocument.find_one(EnergyDepositDocument.request_id == id)

    async def create_energy_deposit(self, energy_deposit: EnergyDeposit) -> EnergyDeposit:
        energy_document = EnergyDepositDocument(request_id=energy_deposit.request_id,
                                                planet_id=energy_deposit.planet_id,
                                                was_recovered=energy_deposit.was_recovered,
                                                created_time=energy_deposit.created_time,
                                                token_amount=energy_deposit.token_amount,
                                                usd_value=energy_deposit.usd_value)
        await energy_document.save()
        return energy_document


class BeaniCurrencyMarketOrderRepositoryAdapter(CurrencyMarketOrderRepositoryPort):

    async def update(self, order: CurrencyMarketOrderDocument) -> CurrencyMarketOrder:
        await order.save_changes()
        return order

    async def find_matching_orders(self, market_code: str, trade_type: str, order_type: str, price: float) -> list[
        CurrencyMarketOrder]:
        matching_orders = []

        if trade_type == "limit":
            if order_type == "buy":
                matching_orders = await CurrencyMarketOrderDocument.find(
                    CurrencyMarketOrderDocument.market_code == market_code,
                    CurrencyMarketOrderDocument.price <= price,
                    CurrencyMarketOrderDocument.order_type == "sell",
                    In(CurrencyMarketOrderDocument.state, ["not_filled", "partially_filled"])
                ).sort(+CurrencyMarketOrderDocument.price, +CurrencyMarketOrderDocument.created_time).to_list()
            elif order_type == "sell":
                matching_orders = await CurrencyMarketOrderDocument.find(
                    CurrencyMarketOrderDocument.market_code == market_code,
                    CurrencyMarketOrderDocument.price >= price,
                    CurrencyMarketOrderDocument.order_type == "buy",
                    In(CurrencyMarketOrderDocument.state, ["not_filled", "partially_filled"])
                ).sort(-CurrencyMarketOrderDocument.price, +CurrencyMarketOrderDocument.created_time).to_list()

        elif trade_type == "market":
            if order_type == "buy":
                matching_orders = await CurrencyMarketOrderDocument.find(
                    CurrencyMarketOrderDocument.market_code == market_code,
                    CurrencyMarketOrderDocument.order_type == "sell",
                    In(CurrencyMarketOrderDocument.state, ["not_filled", "partially_filled"])
                ).sort(+CurrencyMarketOrderDocument.price, +CurrencyMarketOrderDocument.created_time).to_list()
            elif order_type == "sell":
                matching_orders = await CurrencyMarketOrderDocument.find(
                    CurrencyMarketOrderDocument.market_code == market_code,
                    CurrencyMarketOrderDocument.order_type == "buy",
                    In(CurrencyMarketOrderDocument.state, ["not_filled", "partially_filled"])
                ).sort(-CurrencyMarketOrderDocument.price, +CurrencyMarketOrderDocument.created_time).to_list()

        return matching_orders

    async def open_orders_grouped_price(self, market_code: str) -> Tuple[
        list[OpenOrdersGroupedByPrice], list[OpenOrdersGroupedByPrice]]:
        def q(order):
            return [
                # limit before but in case of huge trading data
                # {
                #     "$limit": 500
                # },
                {
                    "$sort":
                        {
                            "price": order
                        }
                },
                {
                    "$group":
                        {
                            "_id": "$price",
                            "order_type": {"$first": "$order_type"},
                            "grouped_price": {"$first": "$price"},
                            "sum_amount": {"$sum": "$amount"},
                            "sum_amount_filled": {"$sum": "$amount_filled"}
                        }
                },

                {
                    "$addFields":
                        {
                            "sum_to_be_filled": {"$subtract": ["$sum_amount", "$sum_amount_filled"]},
                            "total_price": {
                                "$multiply": ["$grouped_price", {"$subtract": ["$sum_amount", "$sum_amount_filled"]}]},
                        }
                },
                {
                    "$sort":
                        {
                            "grouped_price": order
                        }
                },
                {
                    "$limit": 8
                },
            ]

        buy_group = await CurrencyMarketOrderDocument.find(
            CurrencyMarketOrderDocument.market_code == market_code,
            In(CurrencyMarketOrderDocument.state, ["not_filled", "partially_filled"]),
            CurrencyMarketOrderDocument.order_type == "buy"
        ).aggregate(
            q(-1),
            projection_model=OpenOrdersGroupedByPrice
        ).to_list()

        sell_group = await CurrencyMarketOrderDocument.find(
            CurrencyMarketOrderDocument.market_code == market_code,
            In(CurrencyMarketOrderDocument.state, ["not_filled", "partially_filled"]),
            CurrencyMarketOrderDocument.order_type == "sell"
        ).aggregate(
            q(1),
            projection_model=OpenOrdersGroupedByPrice
        ).to_list()

        return buy_group, sell_group

    async def create_order(self, order: CurrencyMarketOrder) -> CurrencyMarketOrder | None:
        order = CurrencyMarketOrderDocument(
            order_type=order.order_type,
            user_id=order.user_id,
            planet_id=order.planet_id,
            created_time=order.created_time,
            updated_time=order.updated_time,
            market_code=order.market_code,
            price=order.price,
            amount=order.amount,
            amount_filled=order.amount_filled,
            state=order.state
        )

        await order.create()
        return order


class BeaniCurrencyMarketTradeRepositoryAdapter(CurrencyMarketTradeRepositoryPort):
    async def _beani_interval_query(self, interval: str) -> dict:
        candle_time_frame_mapping = {
            "1m": {
                "int": 1,
                "pre_date_format": "%Y-%m-%dT%H:",
                "interval_time_selector": "$minute",
                "post_date_format": ":00.000000Z",
            },
            "15m": {
                "int": 15,
                "pre_date_format": "%Y-%m-%dT%H:",
                "interval_time_selector": "$minute",
                "post_date_format": ":00.000000Z",
            },
            "1h": {
                "int": 1,
                "pre_date_format": "%Y-%m-%dT",
                "interval_time_selector": "$hour",
                "post_date_format": ":00:00.000000Z",
            },
        }

        return candle_time_frame_mapping[interval]

    async def last_24_info(self, market_code: str) -> Volume24Info:
        start = datetime.utcnow()
        start_str = start.strftime(f"%Y-%m-%dT00:00:00.000000Z")
        start_dt = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:00.000000Z")

        return await CurrencyMarketTradeDocument.find(
            CurrencyMarketTradeDocument.market_code == market_code
        ).aggregate(
            [
                {
                    "$match": {
                        "created_time": {"$gte": start_dt},
                    },
                },
                {
                    "$group": {
                        "_id": {
                            "date_formatted": {"$dateToString": {
                                "format": "%Y-%m-%d",
                                "date": "$created_time"
                            }}
                        },
                        "max_24": {"$max": "$price"},
                        "min_24": {"$min": "$price"},
                        "pair1_volume": {"$sum": "$amount"},
                        "pair2_volume": {"$sum": {"$multiply": ["$amount", "$price"]}},
                    },
                },

            ],
            projection_model=Volume24Info
        ).to_list()

    async def price_candle_data_grouped_time_range(self, market_code: str, interval: str, time_start: datetime) -> list[
        PriceCandleDataGroupedByTimeInterval]:

        interval_query_info = await self._beani_interval_query(interval)


        # https://stackoverflow.com/a/26814496
        return await CurrencyMarketTradeDocument.find(
            CurrencyMarketTradeDocument.market_code == market_code
        ).aggregate(
            [
                {
                    "$match": {
                        "created_time": {"$gte": time_start},
                    }
                },
                {
                    "$sort":
                        {
                            "created_time": 1
                        }
                },
                {
                    "$group":
                        {
                            "_id": {
                                "date_formatted": {"$dateToString": {
                                    "format":
                                        {"$concat": [interval_query_info["pre_date_format"],
                                                     {"$toString": {
                                                         "$cond": {
                                                             "if": {
                                                                 "$lt": [
                                                                     {
                                                                         "$subtract": [
                                                                             {interval_query_info["interval_time_selector"]: "$created_time"},
                                                                             {"$mod": [{interval_query_info["interval_time_selector"]: "$created_time"},
                                                                                       interval_query_info["int"]]}
                                                                         ]
                                                                     },
                                                                     10
                                                                 ]
                                                             },

                                                             "then": {
                                                                 "$concat": ["0", {"$toString": {
                                                                     "$subtract": [
                                                                         {interval_query_info["interval_time_selector"]: "$created_time"},
                                                                         {"$mod": [{interval_query_info["interval_time_selector"]: "$created_time"},
                                                                                   interval_query_info["int"]]}
                                                                     ]
                                                                 }}]
                                                             },

                                                             "else": {
                                                                 "$subtract": [
                                                                     {interval_query_info["interval_time_selector"]: "$created_time"},
                                                                     {"$mod": [{interval_query_info["interval_time_selector"]: "$created_time"},
                                                                               interval_query_info["int"]]}
                                                                 ]
                                                             }
                                                         },

                                                     }}, interval_query_info["post_date_format"]]},
                                    "date": "$created_time"
                                }},
                            },
                            # "date": {"$first": "$created_time"},
                            ## need to remove seconds from candle
                            # "date": {"$dateToString": {"$date": {"$first": "$created_time"}, "$format": "%Y-%m-%dT%H:%M"}},
                            "open": {"$first": "$price"},
                            "close": {"$last": "$price"},
                            "high": {"$max": "$price"},
                            "low": {"$min": "$price"}
                        }
                },

                {
                    "$limit": 300
                },
            ],
            projection_model=PriceCandleDataGroupedByTimeInterval
        ).to_list()



    async def price_candle_data_grouped_time(self, market_code: str, time_start: datetime, interval: str) -> list[
        PriceCandleDataGroupedByTimeInterval]:

        interval_query_info = await self._beani_interval_query(interval)

        # https://stackoverflow.com/a/26814496
        return await CurrencyMarketTradeDocument.find(
            CurrencyMarketTradeDocument.market_code == market_code
        ).aggregate(
            [
                {
                    "$match": {
                        "created_time": {"$gte": time_start},
                    }
                },
                {
                    "$group":
                        {
                            "_id": {
                                "date_formatted": {"$dateToString": {
                                    "format":
                                        {"$concat": [interval_query_info["pre_date_format"],
                                                     {"$toString": {
                                                         "$cond": {
                                                             "if": {
                                                                 "$lt": [
                                                                     {
                                                                         "$subtract": [
                                                                             {interval_query_info["interval_time_selector"]: "$created_time"},
                                                                             {"$mod": [{interval_query_info["interval_time_selector"]: "$created_time"},
                                                                                       interval_query_info["int"]]}
                                                                         ]
                                                                     },
                                                                     10
                                                                 ]
                                                             },

                                                             "then": {
                                                                 "$concat": ["0", {"$toString": {
                                                                     "$subtract": [
                                                                         {interval_query_info["interval_time_selector"]: "$created_time"},
                                                                         {"$mod": [{interval_query_info["interval_time_selector"]: "$created_time"},
                                                                                   interval_query_info["int"]]}
                                                                     ]
                                                                 }}]
                                                             },

                                                             "else": {
                                                                 "$subtract": [
                                                                     {interval_query_info["interval_time_selector"]: "$created_time"},
                                                                     {"$mod": [{interval_query_info["interval_time_selector"]: "$created_time"},
                                                                               interval_query_info["int"]]}
                                                                 ]
                                                             }
                                                         },

                                                     }}, interval_query_info["post_date_format"]]},
                                    "date": "$created_time"
                                }},
                            },

                            "open": {"$first": "$price"},
                            "close": {"$last": "$price"},
                            "high": {"$max": "$price"},
                            "low": {"$min": "$price"}
                        }
                },
                {
                    "$limit": 300
                },
                {
                    "$sort":
                        {
                            "_id.date_formatted": 1
                        }
                },
            ],
            projection_model=PriceCandleDataGroupedByTimeInterval
        ).to_list()

    async def price_last_candle_data_grouped_time(self, market_code: str, interval: int) -> list[
        PriceCandleDataGroupedByTimeInterval]:
        # https://stackoverflow.com/a/26814496
        return (await CurrencyMarketTradeDocument.find(
            CurrencyMarketTradeDocument.market_code == market_code
        ).aggregate(
            [

                {
                    "$group":
                        {
                            "_id": {
                                "minute": {"$minute": "$created_time"},
                                "date_formatted": {"$dateToString": {
                                    "format": "%Y-%m-%dT%H:%M:00.000000Z", "date": "$created_time"
                                }},
                                "interval": {
                                    "$subtract": [
                                        {"$minute": "$created_time"},
                                        {"$mod": [{"$minute": "$created_time"}, 1]}
                                    ]
                                },

                                "date_parsed": {"$dateFromString": {
                                    "dateString": {"$dateToString": {
                                        "format": "%Y-%m-%dT%H:%M:00",
                                        "date": "$created_time"
                                    }}
                                }}
                            },
                            # "date": {"$first": "$created_time"},
                            ## need to remove seconds from candle
                            # "date": {"$dateToString": {"$date": {"$first": "$created_time"}, "$format": "%Y-%m-%dT%H:%M"}},
                            "open": {"$first": "$price"},
                            "close": {"$last": "$price"},
                            "high": {"$max": "$price"},
                            "low": {"$min": "$price"}
                        }
                },
                {
                    "$sort":
                        {
                            "_id.date_parsed": -1
                        }
                },
                {
                    "$limit": 1
                }
            ],
            projection_model=PriceCandleDataGroupedByTimeInterval
        ).to_list())

    async def last(self) -> list[CurrencyMarketTradeDocument]:
        return await CurrencyMarketTradeDocument.all().sort(-CurrencyMarketTradeDocument.created_time).limit(
            2).to_list()

    async def all(self) -> list[CurrencyMarketTradeDocument] | None:
        return await CurrencyMarketTradeDocument.all().to_list()

    async def all_descending_limit_by_day(self, market_code: str) -> list[CurrencyMarketTradeDocument] | None:
        start = datetime.strptime(datetime
                                  .utcnow()
                                  .strftime("%Y-%m-%dT00:00:00.000000Z"), "%Y-%m-%dT%H:%M:00.000000Z")

        return await CurrencyMarketTradeDocument.find(
            CurrencyMarketTradeDocument.market_code == market_code,
            CurrencyMarketTradeDocument.created_time >= start
        ).sort(+CurrencyMarketTradeDocument.created_time).to_list()

    async def create_trade(self, trade: CurrencyMarketTrade) -> CurrencyMarketTrade | None:
        trade = CurrencyMarketTradeDocument(
            market_code=trade.market_code,
            price=trade.price,
            amount=trade.amount,
            created_time=datetime.utcnow()
        )

        await trade.create()
        return trade


class BeaniUserRepositoryAdapter(UserRepositoryPort):

    async def all(self) -> list[User] | None:
        return await UserDocument.all().to_list()

    async def find_user(self, wallet: str) -> User | None:
        re = await UserDocument.find_one(UserDocument.wallet == wallet)
        return re

    async def find_user_or_throw(self, wallet: str) -> User:
        re = await UserDocument.find_one(UserDocument.wallet == wallet)

        if not re:
            raise UserNotFoundException()

        return re

    async def create_user(self, wallet: str) -> User:
        user = UserDocument(wallet=wallet)
        await user.create()
        return user


class BeaniPlanetRepositoryAdapter(PlanetRepositoryPort):
    # seems like you cant update if it had fetch_links
    async def all_claimed_planets(self) -> list[Planet]:
        planets = await PlanetDocument.find(PlanetDocument.claimed == True).to_list()
        return planets

    async def by_position_range(self, galaxy: int, from_solar_system: int, to_solar_system: int, fetch_links=False) -> \
            list[Planet]:
        planets = await PlanetDocument.find(PlanetDocument.galaxy == galaxy,
                                            PlanetDocument.solar_system >= from_solar_system,
                                            PlanetDocument.solar_system <= to_solar_system,
                                            fetch_links=fetch_links).to_list()

        return planets

    async def all_user_planets(self, user_id: str, fetch_links=False) -> list[Planet]:
        planets = await PlanetDocument.find(PlanetDocument.user == user_id, fetch_links=fetch_links).to_list()
        return planets

    async def update(self, planet: PlanetDocument) -> Planet:
        await planet.save_changes()
        return planet

    async def get_my_planet(self, user_id: str, planet_id: str, fetch_links=False) -> Planet | None:
        # if fetch_links provided energy_deposits comes null?
        # @README: seems like fetch_link works with emails but not with energy_deposits, only difference is that
        # on energy deposit we set our own id.
        planet = await PlanetDocument.find_one(
            PlanetDocument.id == PydanticObjectId(planet_id),
            PlanetDocument.user == user_id,
            fetch_links=fetch_links
        )

        return planet

    async def get(self, planet_id: str, fetch_links=False) -> Planet | None:
        # TokenConversionsDocument.update_forward_refs()
        planet = await PlanetDocument.find_one(PlanetDocument.id == PydanticObjectId(planet_id),
                                               fetch_links=fetch_links)
        return planet

    async def get_by_request_id(self, request_id: str, fetch_links=False) -> Planet | None:
        # TokenConversionsDocument.update_forward_refs()
        planet = await PlanetDocument.find_one(PlanetDocument.request_id == request_id, fetch_links=fetch_links)
        return planet

    async def has_free_planet(self, user_id: str) -> bool:
        free_planet = await PlanetDocument.find(PlanetDocument.user == user_id,
                                                PlanetDocument.price_paid == 0).limit(1).to_list()

        return len(free_planet) > 0

    async def last_created_planet(self, fetch_links=False) -> Planet | bool:
        last_planet = await PlanetDocument.all(fetch_links=fetch_links).sort(-PlanetDocument.created_at).limit(
            1).to_list()

        if not last_planet:
            return False

        return last_planet[0]

    async def create_planet(self, planet_data: Planet) -> Planet:
        user = await UserDocument.find_one(UserDocument.wallet == planet_data.user)

        planet_tier = PlanetTier()

        # id = bson.objectid.ObjectId()
        new_planet = PlanetDocument(
            request_id=planet_data.request_id,
            name=planet_data.name,
            created_at=datetime.timestamp(datetime.now()),
            rarity=planet_data.rarity,
            image=planet_data.image,
            diameter=planet_data.diameter,
            level=0,
            experience=0,
            slots=planet_data.slots,
            slots_used=planet_data.slots_used,
            min_temperature=planet_data.min_temperature,
            max_temperature=planet_data.max_temperature,
            reserves=planet_data.reserves,
            original_total_metal_amount=planet_data.reserves.total_metal,
            original_total_crystal_amount=planet_data.reserves.total_crystal,
            original_total_petrol_amount=planet_data.reserves.total_petrol,
            galaxy=planet_data.galaxy,
            solar_system=planet_data.solar_system,
            position=planet_data.position,
            user=user.wallet,
            claimable=planet_data.claimable,
            claimed=planet_data.claimed,
            tier=planet_tier,
            resources=planet_data.resources,
            price_paid=planet_data.price_paid,
            free_tokens=0,
            resources_level=planet_data.resources_level,
            installation_level=planet_data.installation_level,
            research_level=planet_data.research_level,
            defense_items=planet_data.defense_items,
            pending_levelup_reward=[],
            energy_deposits=[]
        )

        await new_planet.save(link_rule=WriteRules.WRITE)
        user.planets.append(new_planet)
        await user.save(link_rule=WriteRules.WRITE)

        return new_planet
