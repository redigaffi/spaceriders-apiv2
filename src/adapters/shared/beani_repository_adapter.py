from __future__ import annotations

from datetime import datetime

from beanie import DeleteRules, PydanticObjectId, WriteRules
from beanie.operators import In

from adapters.shared.beanie_models_adapter import (
    BKMTransactionDocument,
    CurrencyMarketOrderDocument,
    CurrencyMarketTradeDocument,
    EmailDocument,
    EnergyDepositDocument,
    PlanetDocument,
    UserDocument,
)
from core.shared.models import (
    BKMTransaction,
    CurrencyMarketOrder,
    CurrencyMarketTrade,
    Email,
    EnergyDeposit,
    OpenOrdersGroupedByPrice,
    Planet,
    PlanetTier,
    PriceCandleDataGroupedByTimeInterval,
    User,
    UserNotFoundException,
    Volume24Info,
)
from core.shared.ports import (
    BKMDepositRepositoryPort,
    CurrencyMarketOrderRepositoryPort,
    CurrencyMarketTradeRepositoryPort,
    EmailRepositoryPort,
    EnergyDepositRepositoryPort,
    PlanetRepositoryPort,
    UserRepositoryPort,
)


class EmailRepositoryAdapter(EmailRepositoryPort):
    async def create(self, email: Email) -> Email:
        email_document = EmailDocument(
            title=email.title,
            sub_title=email.sub_title,
            template=email.template,
            body=email.body,
            sender=email.sender,
            read=email.read,
            planet=email.planet,
        )

        await email_document.save()
        return email_document

    async def update(self, email: EmailDocument) -> Email:
        await email.save_changes()
        return email

    async def delete(self, email: Email):
        email_document: EmailDocument = await EmailDocument.get(
            PydanticObjectId(email.id)
        )
        planet = await PlanetDocument.get(PydanticObjectId(email.planet))
        await planet.fetch_link(PlanetDocument.emails)
        planet.emails = [x for x in planet.emails if str(x.id) != email.id]

        await planet.save_changes()
        await email_document.delete(link_rule=DeleteRules.DELETE_LINKS)

    async def delete_all_by_user(self, planet_id) -> None:
        email_documents: list[EmailDocument] = await EmailDocument.find(
            EmailDocument.planet == planet_id
        ).to_list()
        for email in email_documents:
            await email.delete(link_rule=DeleteRules.DELETE_LINKS)

        planet = await PlanetDocument.get(PydanticObjectId(planet_id))
        await planet.fetch_link(PlanetDocument.emails)
        planet.emails = []

        await planet.save_changes()

    async def get(self, email_id) -> Email:
        email = await EmailDocument.get(PydanticObjectId(email_id))
        return email


class EnergyDepositRepositoryAdapter(EnergyDepositRepositoryPort):
    async def get(self, id: str) -> EnergyDeposit | None:
        return await EnergyDepositDocument.find_one(
            EnergyDepositDocument.request_id == id
        )

    async def create_energy_deposit(
        self, energy_deposit: EnergyDeposit
    ) -> EnergyDeposit:
        energy_document = EnergyDepositDocument(
            planet_id=energy_deposit.planet_id,
            created_time=energy_deposit.created_time,
            energy_amount=energy_deposit.energy_amount,
        )
        await energy_document.save()
        return energy_document


class BKMDepositRepositoryAdapter(BKMDepositRepositoryPort):
    async def get(self, id: str) -> BKMTransaction | None:
        return await BKMTransactionDocument.find_one(
            BKMTransactionDocument.request_id == id
        )

    async def create_bkm_transaction(
        self, energy_deposit: BKMTransaction
    ) -> BKMTransaction:
        bkm_document = BKMTransactionDocument(
            request_id=energy_deposit.request_id,
            planet_id=energy_deposit.planet_id,
            was_recovered=energy_deposit.was_recovered,
            created_time=energy_deposit.created_time,
            token_amount=energy_deposit.token_amount,
            type=energy_deposit.type,
        )
        await bkm_document.save()
        return bkm_document


class BeaniCurrencyMarketOrderRepositoryAdapter(CurrencyMarketOrderRepositoryPort):
    async def delete(self, id: str):
        order = await CurrencyMarketOrderDocument.get(PydanticObjectId(id))
        await order.delete()

    async def get_by_id(self, id: str) -> CurrencyMarketOrder:
        return await CurrencyMarketOrderDocument.get(PydanticObjectId(id))

    async def my_open_orders_by_planet(
        self, market_code: str, planet_id: str
    ) -> list[CurrencyMarketOrder]:
        return (
            await CurrencyMarketOrderDocument.find(
                CurrencyMarketOrderDocument.market_code == market_code,
                CurrencyMarketOrderDocument.planet_id == planet_id,
                In(
                    CurrencyMarketOrderDocument.state,
                    ["not_filled", "partially_filled"],
                ),
            )
            .sort(
                +CurrencyMarketOrderDocument.price,
                +CurrencyMarketOrderDocument.created_time,
            )
            .to_list()
        )

    async def update(self, order: CurrencyMarketOrderDocument) -> CurrencyMarketOrder:
        await order.save_changes()
        return order

    async def find_matching_orders(
        self, market_code: str, trade_type: str, order_type: str, price: float
    ) -> list[CurrencyMarketOrder]:
        matching_orders = []

        if trade_type == "limit":
            if order_type == "buy":
                matching_orders = (
                    await CurrencyMarketOrderDocument.find(
                        CurrencyMarketOrderDocument.market_code == market_code,
                        CurrencyMarketOrderDocument.price <= price,
                        CurrencyMarketOrderDocument.order_type == "sell",
                        In(
                            CurrencyMarketOrderDocument.state,
                            ["not_filled", "partially_filled"],
                        ),
                    )
                    .sort(
                        +CurrencyMarketOrderDocument.price,
                        +CurrencyMarketOrderDocument.created_time,
                    )
                    .to_list()
                )
            elif order_type == "sell":
                matching_orders = (
                    await CurrencyMarketOrderDocument.find(
                        CurrencyMarketOrderDocument.market_code == market_code,
                        CurrencyMarketOrderDocument.price >= price,
                        CurrencyMarketOrderDocument.order_type == "buy",
                        In(
                            CurrencyMarketOrderDocument.state,
                            ["not_filled", "partially_filled"],
                        ),
                    )
                    .sort(
                        -CurrencyMarketOrderDocument.price,
                        +CurrencyMarketOrderDocument.created_time,
                    )
                    .to_list()
                )

        elif trade_type == "market":
            if order_type == "buy":
                matching_orders = (
                    await CurrencyMarketOrderDocument.find(
                        CurrencyMarketOrderDocument.market_code == market_code,
                        CurrencyMarketOrderDocument.order_type == "sell",
                        In(
                            CurrencyMarketOrderDocument.state,
                            ["not_filled", "partially_filled"],
                        ),
                    )
                    .sort(
                        +CurrencyMarketOrderDocument.price,
                        +CurrencyMarketOrderDocument.created_time,
                    )
                    .to_list()
                )
            elif order_type == "sell":
                matching_orders = (
                    await CurrencyMarketOrderDocument.find(
                        CurrencyMarketOrderDocument.market_code == market_code,
                        CurrencyMarketOrderDocument.order_type == "buy",
                        In(
                            CurrencyMarketOrderDocument.state,
                            ["not_filled", "partially_filled"],
                        ),
                    )
                    .sort(
                        -CurrencyMarketOrderDocument.price,
                        +CurrencyMarketOrderDocument.created_time,
                    )
                    .to_list()
                )

        return matching_orders

    async def open_orders_grouped_price(
        self, market_code: str
    ) -> tuple[list[OpenOrdersGroupedByPrice], list[OpenOrdersGroupedByPrice]]:
        def q(order):
            return [
                # limit before but in case of huge trading data
                # {
                #     "$limit": 500
                # },
                {"$sort": {"price": order}},
                {
                    "$group": {
                        "_id": "$price",
                        "order_type": {"$first": "$order_type"},
                        "grouped_price": {"$first": "$price"},
                        "sum_amount": {"$sum": "$amount"},
                        "sum_amount_filled": {"$sum": "$amount_filled"},
                    }
                },
                {
                    "$addFields": {
                        "sum_to_be_filled": {
                            "$subtract": ["$sum_amount", "$sum_amount_filled"]
                        },
                        "total_price": {
                            "$multiply": [
                                "$grouped_price",
                                {"$subtract": ["$sum_amount", "$sum_amount_filled"]},
                            ]
                        },
                    }
                },
                {"$sort": {"grouped_price": order}},
                {"$limit": 8},
            ]

        buy_group = (
            await CurrencyMarketOrderDocument.find(
                CurrencyMarketOrderDocument.market_code == market_code,
                In(
                    CurrencyMarketOrderDocument.state,
                    ["not_filled", "partially_filled"],
                ),
                CurrencyMarketOrderDocument.order_type == "buy",
            )
            .aggregate(q(-1), projection_model=OpenOrdersGroupedByPrice)
            .to_list()
        )

        sell_group = (
            await CurrencyMarketOrderDocument.find(
                CurrencyMarketOrderDocument.market_code == market_code,
                In(
                    CurrencyMarketOrderDocument.state,
                    ["not_filled", "partially_filled"],
                ),
                CurrencyMarketOrderDocument.order_type == "sell",
            )
            .aggregate(q(1), projection_model=OpenOrdersGroupedByPrice)
            .to_list()
        )

        return buy_group, sell_group

    async def create_order(
        self, order: CurrencyMarketOrder
    ) -> CurrencyMarketOrder | None:
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
            state=order.state,
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
            "1d": {
                "int": 1,
                "pre_date_format": "%Y-%m-",
                "interval_time_selector": "$dayOfMonth",
                "post_date_format": "T00:00:00.000000Z",
            },
        }

        return candle_time_frame_mapping[interval]

    async def last_24_info(self, market_code: str) -> Volume24Info:
        start = datetime.utcnow()
        start_str = start.strftime(f"%Y-%m-%dT00:00:00.000000Z")
        start_dt = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:00.000000Z")

        return (
            await CurrencyMarketTradeDocument.find(
                CurrencyMarketTradeDocument.market_code == market_code
            )
            .aggregate(
                [
                    {
                        "$match": {
                            "created_time": {"$gte": start_dt},
                        },
                    },
                    {
                        "$group": {
                            "_id": {
                                "date_formatted": {
                                    "$dateToString": {
                                        "format": "%Y-%m-%d",
                                        "date": "$created_time",
                                    }
                                }
                            },
                            "max_24": {"$max": "$price"},
                            "min_24": {"$min": "$price"},
                            "pair1_volume": {"$sum": "$amount"},
                            "pair2_volume": {
                                "$sum": {"$multiply": ["$amount", "$price"]}
                            },
                        },
                    },
                ],
                projection_model=Volume24Info,
            )
            .to_list()
        )

    async def price_candle_data_grouped_time_range(
        self, market_code: str, interval: str, time_start: datetime
    ) -> list[PriceCandleDataGroupedByTimeInterval]:

        interval_query_info = await self._beani_interval_query(interval)

        # https://stackoverflow.com/a/26814496
        return (
            await CurrencyMarketTradeDocument.find(
                CurrencyMarketTradeDocument.market_code == market_code
            )
            .aggregate(
                [
                    {
                        "$match": {
                            "created_time": {"$gte": time_start},
                        }
                    },
                    {"$sort": {"created_time": 1}},
                    {
                        "$group": {
                            "_id": {
                                "date_formatted": {
                                    "$dateToString": {
                                        "format": {
                                            "$concat": [
                                                interval_query_info["pre_date_format"],
                                                {
                                                    "$toString": {
                                                        "$cond": {
                                                            "if": {
                                                                "$lt": [
                                                                    {
                                                                        "$subtract": [
                                                                            {
                                                                                interval_query_info[
                                                                                    "interval_time_selector"
                                                                                ]: "$created_time"
                                                                            },
                                                                            {
                                                                                "$mod": [
                                                                                    {
                                                                                        interval_query_info[
                                                                                            "interval_time_selector"
                                                                                        ]: "$created_time"
                                                                                    },
                                                                                    interval_query_info[
                                                                                        "int"
                                                                                    ],
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                    10,
                                                                ]
                                                            },
                                                            "then": {
                                                                "$concat": [
                                                                    "0",
                                                                    {
                                                                        "$toString": {
                                                                            "$subtract": [
                                                                                {
                                                                                    interval_query_info[
                                                                                        "interval_time_selector"
                                                                                    ]: "$created_time"
                                                                                },
                                                                                {
                                                                                    "$mod": [
                                                                                        {
                                                                                            interval_query_info[
                                                                                                "interval_time_selector"
                                                                                            ]: "$created_time"
                                                                                        },
                                                                                        interval_query_info[
                                                                                            "int"
                                                                                        ],
                                                                                    ]
                                                                                },
                                                                            ]
                                                                        }
                                                                    },
                                                                ]
                                                            },
                                                            "else": {
                                                                "$subtract": [
                                                                    {
                                                                        interval_query_info[
                                                                            "interval_time_selector"
                                                                        ]: "$created_time"
                                                                    },
                                                                    {
                                                                        "$mod": [
                                                                            {
                                                                                interval_query_info[
                                                                                    "interval_time_selector"
                                                                                ]: "$created_time"
                                                                            },
                                                                            interval_query_info[
                                                                                "int"
                                                                            ],
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        },
                                                    }
                                                },
                                                interval_query_info["post_date_format"],
                                            ]
                                        },
                                        "date": "$created_time",
                                    }
                                },
                            },
                            # "date": {"$first": "$created_time"},
                            ## need to remove seconds from candle
                            # "date": {"$dateToString": {"$date": {"$first": "$created_time"}, "$format": "%Y-%m-%dT%H:%M"}},
                            "open": {"$first": "$price"},
                            "close": {"$last": "$price"},
                            "high": {"$max": "$price"},
                            "low": {"$min": "$price"},
                        }
                    },
                    {"$limit": 300},
                ],
                projection_model=PriceCandleDataGroupedByTimeInterval,
            )
            .to_list()
        )

    async def price_candle_data_grouped_time(
        self, market_code: str, time_start: datetime, interval: str
    ) -> list[PriceCandleDataGroupedByTimeInterval]:

        interval_query_info = await self._beani_interval_query(interval)

        # https://stackoverflow.com/a/26814496
        return (
            await CurrencyMarketTradeDocument.find(
                CurrencyMarketTradeDocument.market_code == market_code
            )
            .aggregate(
                [
                    {
                        "$match": {
                            "created_time": {"$gte": time_start},
                        }
                    },
                    {
                        "$group": {
                            "_id": {
                                "date_formatted": {
                                    "$dateToString": {
                                        "format": {
                                            "$concat": [
                                                interval_query_info["pre_date_format"],
                                                {
                                                    "$toString": {
                                                        "$cond": {
                                                            "if": {
                                                                "$lt": [
                                                                    {
                                                                        "$subtract": [
                                                                            {
                                                                                interval_query_info[
                                                                                    "interval_time_selector"
                                                                                ]: "$created_time"
                                                                            },
                                                                            {
                                                                                "$mod": [
                                                                                    {
                                                                                        interval_query_info[
                                                                                            "interval_time_selector"
                                                                                        ]: "$created_time"
                                                                                    },
                                                                                    interval_query_info[
                                                                                        "int"
                                                                                    ],
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                    10,
                                                                ]
                                                            },
                                                            "then": {
                                                                "$concat": [
                                                                    "0",
                                                                    {
                                                                        "$toString": {
                                                                            "$subtract": [
                                                                                {
                                                                                    interval_query_info[
                                                                                        "interval_time_selector"
                                                                                    ]: "$created_time"
                                                                                },
                                                                                {
                                                                                    "$mod": [
                                                                                        {
                                                                                            interval_query_info[
                                                                                                "interval_time_selector"
                                                                                            ]: "$created_time"
                                                                                        },
                                                                                        interval_query_info[
                                                                                            "int"
                                                                                        ],
                                                                                    ]
                                                                                },
                                                                            ]
                                                                        }
                                                                    },
                                                                ]
                                                            },
                                                            "else": {
                                                                "$subtract": [
                                                                    {
                                                                        interval_query_info[
                                                                            "interval_time_selector"
                                                                        ]: "$created_time"
                                                                    },
                                                                    {
                                                                        "$mod": [
                                                                            {
                                                                                interval_query_info[
                                                                                    "interval_time_selector"
                                                                                ]: "$created_time"
                                                                            },
                                                                            interval_query_info[
                                                                                "int"
                                                                            ],
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        },
                                                    }
                                                },
                                                interval_query_info["post_date_format"],
                                            ]
                                        },
                                        "date": "$created_time",
                                    }
                                },
                            },
                            "open": {"$first": "$price"},
                            "close": {"$last": "$price"},
                            "high": {"$max": "$price"},
                            "low": {"$min": "$price"},
                        }
                    },
                    {"$limit": 300},
                    {"$sort": {"_id.date_formatted": 1}},
                ],
                projection_model=PriceCandleDataGroupedByTimeInterval,
            )
            .to_list()
        )

    async def price_last_candle_data_grouped_time(
        self, market_code: str, interval: int
    ) -> list[PriceCandleDataGroupedByTimeInterval]:
        # https://stackoverflow.com/a/26814496
        return (
            await CurrencyMarketTradeDocument.find(
                CurrencyMarketTradeDocument.market_code == market_code
            )
            .aggregate(
                [
                    {
                        "$group": {
                            "_id": {
                                "minute": {"$minute": "$created_time"},
                                "date_formatted": {
                                    "$dateToString": {
                                        "format": "%Y-%m-%dT%H:%M:00.000000Z",
                                        "date": "$created_time",
                                    }
                                },
                                "interval": {
                                    "$subtract": [
                                        {"$minute": "$created_time"},
                                        {"$mod": [{"$minute": "$created_time"}, 1]},
                                    ]
                                },
                                "date_parsed": {
                                    "$dateFromString": {
                                        "dateString": {
                                            "$dateToString": {
                                                "format": "%Y-%m-%dT%H:%M:00",
                                                "date": "$created_time",
                                            }
                                        }
                                    }
                                },
                            },
                            # "date": {"$first": "$created_time"},
                            ## need to remove seconds from candle
                            # "date": {"$dateToString": {"$date": {"$first": "$created_time"}, "$format": "%Y-%m-%dT%H:%M"}},
                            "open": {"$first": "$price"},
                            "close": {"$last": "$price"},
                            "high": {"$max": "$price"},
                            "low": {"$min": "$price"},
                        }
                    },
                    {"$sort": {"_id.date_parsed": -1}},
                    {"$limit": 1},
                ],
                projection_model=PriceCandleDataGroupedByTimeInterval,
            )
            .to_list()
        )

    async def last(self, market_code: str) -> list[CurrencyMarketTradeDocument]:
        return (
            await CurrencyMarketTradeDocument.find(
                CurrencyMarketTradeDocument.market_code == market_code
            )
            .sort(-CurrencyMarketTradeDocument.created_time)
            .limit(2)
            .to_list()
        )

    async def last_from(
        self, market_code: str, starting_from: datetime
    ) -> list[CurrencyMarketTrade]:
        return (
            await CurrencyMarketTradeDocument.find(
                CurrencyMarketTradeDocument.market_code == market_code,
                CurrencyMarketTradeDocument.created_time <= starting_from,
            )
            .sort(-CurrencyMarketTradeDocument.created_time)
            .limit(1)
            .to_list()
        )

    async def all(self) -> list[CurrencyMarketTradeDocument] | None:
        return await CurrencyMarketTradeDocument.all().to_list()

    async def all_descending_limit_by_day(
        self, market_code: str
    ) -> list[CurrencyMarketTradeDocument] | None:
        start = datetime.strptime(
            datetime.utcnow().strftime("%Y-%m-%dT00:00:00.000000Z"),
            "%Y-%m-%dT%H:%M:00.000000Z",
        )

        return (
            await CurrencyMarketTradeDocument.find(
                CurrencyMarketTradeDocument.market_code == market_code,
                CurrencyMarketTradeDocument.created_time >= start,
            )
            .sort(+CurrencyMarketTradeDocument.created_time)
            .to_list()
        )

    async def create_trade(
        self, trade: CurrencyMarketTrade
    ) -> CurrencyMarketTrade | None:
        trade = CurrencyMarketTradeDocument(
            market_code=trade.market_code,
            price=trade.price,
            amount=trade.amount,
            created_time=datetime.utcnow(),
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

    async def by_position_range(
        self,
        galaxy: int,
        from_solar_system: int,
        to_solar_system: int,
        fetch_links=False,
    ) -> list[Planet]:

        planets = await PlanetDocument.find(
            PlanetDocument.galaxy == galaxy,
            PlanetDocument.solar_system >= from_solar_system,
            PlanetDocument.solar_system <= to_solar_system,
            fetch_links=fetch_links,
        ).to_list()

        return planets

    async def occupied_positions_by_range(
        self,
        galaxy: int,
        from_solar_system: int,
        to_solar_system: int,
    ) -> dict[str, bool]:

        planets = await PlanetDocument.find(
            PlanetDocument.galaxy == galaxy,
            PlanetDocument.solar_system >= from_solar_system,
            PlanetDocument.solar_system <= to_solar_system,
            fetch_links=False,
        ).to_list()

        re = {}
        for planet in planets:
            pos = f"{planet.galaxy}:{planet.solar_system}:{planet.position}"
            re[pos] = True

        return re

    async def all_user_planets(self, user_id: str, fetch_links=False) -> list[Planet]:
        planets = await PlanetDocument.find(
            PlanetDocument.user == user_id, fetch_links=fetch_links
        ).to_list()
        return planets

    async def update(self, planet: PlanetDocument) -> Planet:
        await planet.save_changes()
        return await self.get(str(planet.id))

    async def get_my_planet(
        self, user_id: str, planet_id: str, fetch_links=False
    ) -> Planet | None:
        # if fetch_links provided energy_deposits comes null?
        # @README: seems like fetch_link works with emails but not with energy_deposits, only difference is that
        # on energy deposit we set our own id.
        planet = await PlanetDocument.find_one(
            PlanetDocument.id == PydanticObjectId(planet_id),
            PlanetDocument.user == user_id,
            fetch_links=fetch_links,
        )

        return planet

    async def get(self, planet_id: str, fetch_links=False) -> Planet | None:
        planet = await PlanetDocument.find_one(
            PlanetDocument.id == PydanticObjectId(planet_id), fetch_links=fetch_links
        )
        return planet

    async def get_by_request_id(
        self, request_id: str, fetch_links=False
    ) -> Planet | None:
        planet = await PlanetDocument.find_one(
            PlanetDocument.request_id == request_id, fetch_links=fetch_links
        )
        return planet

    async def last_created_planet(self, fetch_links=False) -> Planet | bool:
        last_planet = (
            await PlanetDocument.all(fetch_links=fetch_links)
            .sort(-PlanetDocument.created_at)
            .limit(1)
            .to_list()
        )

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
            galaxy=planet_data.galaxy,
            solar_system=planet_data.solar_system,
            position=planet_data.position,
            user=user.wallet,
            claimable=planet_data.claimable,
            claimed=planet_data.claimed,
            tier=planet_tier,
            resources=planet_data.resources,
            resources_level=planet_data.resources_level,
            installation_level=planet_data.installation_level,
            research_level=planet_data.research_level,
            defense_items=planet_data.defense_items,
            pending_levelup_reward=[],
            energy_deposits=[],
        )

        await new_planet.save(link_rule=WriteRules.WRITE)
        user.planets.append(new_planet)
        await user.save(link_rule=WriteRules.WRITE)

        return new_planet
