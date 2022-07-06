from datetime import datetime
from datetime import timedelta
from pydantic import BaseModel
from core.shared.models import CurrencyMarketOrder, CurrencyMarketTrade, OpenOrdersGroupedByPrice, \
    PriceCandleDataGroupedByTimeInterval, Volume24Info, AppBaseException, Planet
from core.shared.ports import ResponsePort, CurrencyMarketOrderRepositoryPort, CurrencyMarketTradeRepositoryPort, \
    PlanetRepositoryPort
from dataclasses import dataclass


class TradeRequest(BaseModel):
    trade_type: str = None  # limit/market ...
    user_id: str = None
    planet_id: str = None
    order_type: str = None  # 'buy' or 'sell'
    pair1: str = None  # metal/petrol
    pair2: str = None  # metal/petrol
    price_unit: float = None  # price to be paid in pair 2
    amount: float = None  # amount in pair 1 to be bought
    total: float = None  # total = price_unit * amount ; only used for limit orders


class TradeResponse(BaseModel):
    order: CurrencyMarketOrder
    executed_trades: list[CurrencyMarketTrade]


class FetchHistoricalData(BaseModel):
    last_trades: list[CurrencyMarketTrade]
    open_buy_orders: list[OpenOrdersGroupedByPrice]
    open_sell_orders: list[OpenOrdersGroupedByPrice]
    price_candle_data: dict[str, PriceCandleDataGroupedByTimeInterval|None]
    last_24_info: Volume24Info | None


class NotEnoughFundsException(AppBaseException):
    msg = "Level up has already been claimed"

    @staticmethod
    def from_resource_name(resource_name: str):
        ex = NotEnoughFundsException()
        ex.msg = f"Not holding enough {resource_name}"
        return ex


# @TODO: Add index to created time
# @TODO: Add index to price?
@dataclass
class CurrencyMarket:
    planet_repository: PlanetRepositoryPort
    currency_market_order_repository: CurrencyMarketOrderRepositoryPort
    currency_market_trade_repository: CurrencyMarketTradeRepositoryPort
    response_port: ResponsePort

    async def _price_candle_data(self, market_code: str, candle_time_frame: str):
        # @TODO: ADD caching
        # @TODO: Created time index
        # amount of bars
        now = datetime.utcnow()
        day1ago_1 = now - timedelta(minutes=120)
        day1ago_str = day1ago_1.strftime("%Y-%m-%dT%H:00:00.000000Z")
        day1ago = datetime.strptime(day1ago_str, "%Y-%m-%dT%H:00:00.000000Z")

        candle_time_frame_mapping = {
            "1m": dict(minutes=1),
            "15m": dict(minutes=15),
            "1h": dict(hours=1),
        }

        price_candle_data = await self.currency_market_trade_repository.price_candle_data_grouped_time(market_code,
                                                                                                       day1ago,
                                                                                                       candle_time_frame)

        price_candle_tmp = {}
        for p in price_candle_data:
            price_candle_tmp[p.id['date_formatted']] = p

        current_price = None
        if not len(price_candle_data):
            last_trade_arr = await self.currency_market_trade_repository.last()
            if len(last_trade_arr) > 0:
                last_trade = last_trade_arr[0]
                minute = day1ago.strftime("%M")
                current_price = PriceCandleDataGroupedByTimeInterval(_id={
                    "minute": minute,
                    "date_formatted": now.strftime("%Y-%m-%dT%H:%M:00.000000Z"),
                    "interval": minute
                }, open=last_trade.price, close=last_trade.price, high=last_trade.price,
                    low=last_trade.price)

        prices = {}
        while day1ago <= now:
            date_formatted = day1ago.strftime("%Y-%m-%dT%H:%M:00.000000Z")
            minute = day1ago.strftime("%M")

            if date_formatted in price_candle_tmp:
                current_price = price_candle_tmp[date_formatted]
            elif current_price is not None:
                current_price = PriceCandleDataGroupedByTimeInterval(_id={
                    "minute": minute,
                    "date_formatted": date_formatted,
                    "interval": minute
                }, open=current_price.close, close=current_price.close, high=current_price.close,
                    low=current_price.close)

            if current_price is not None:
                prices[date_formatted] = current_price

            day1ago += timedelta(**candle_time_frame_mapping[candle_time_frame])

        return prices

    async def fetch_current_candle_data(self, market_code: str, candle_time_frame: str):
        candle_time_frame_mapping = {
            "1m": 1,
            "15m": 15,
            "1h": 1,
        }

        def min_date_parser(start):
            m = int(start.strftime("%M"))
            range = int(m - m % candle_time_frame_mapping[candle_time_frame])
            if range < 10:
                range = f"0{range}"

            return start.strftime(f"%Y-%m-%dT%H:{range}:00.000000Z")

        def hour_date_parser(start):
            h = int(start.strftime("%H"))
            range = int(h - h % candle_time_frame_mapping[candle_time_frame])
            if range < 10:
                range = f"0{range}"
            return start.strftime(f"%Y-%m-%dT{range}:00:00.000000Z")

        candle_time_frame_func_mapping = {
            "1m": min_date_parser,
            "15m": min_date_parser,
            "1h": hour_date_parser
        }

        start = datetime.utcnow()

        start_str = candle_time_frame_func_mapping[candle_time_frame](start)
        start_dt = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%S.000000Z")

        price_candle_data = await self.currency_market_trade_repository.price_candle_data_grouped_time_range(market_code,
                                                                                                             candle_time_frame,
                                                                                                             start_dt)

        tmp = None
        if len(price_candle_data) == 1:
            tmp = price_candle_data[0]

        price_candle_data_formatted = {
            start_str: tmp
        }

        last_24_info = await self.currency_market_trade_repository.last_24_info(market_code)
        last_24_info = last_24_info[0] if len(last_24_info) > 0 else None

        return FetchHistoricalData(last_trades=[],
                                   open_buy_orders=[],
                                   open_sell_orders=[],
                                   price_candle_data=price_candle_data_formatted,
                                   last_24_info=last_24_info)

    async def fetch_historical_data(self, market_code: str, candle_time_frame: str):
        buy_group, sell_group = await self.currency_market_order_repository.open_orders_grouped_price(market_code)
        last_trades = await self.currency_market_trade_repository.all_descending_limit_by_day(market_code)
        #price_candle_data = await self.currency_market_trade_repository.price_candle_data_grouped_time(market_code, 1)
        prices = await self._price_candle_data(market_code, candle_time_frame)
        last_24_info = await self.currency_market_trade_repository.last_24_info(market_code)
        last_24_info = last_24_info[0] if len(last_24_info) > 0 else None

        # a = await self.fetch_last_candle_data(market_code)

        return FetchHistoricalData(last_trades=last_trades,
                                   open_buy_orders=buy_group,
                                   open_sell_orders=sell_group[::-1],
                                   price_candle_data=prices,
                                   last_24_info=last_24_info)

    async def fetch_order_book_data(self, market_code: str):
        buy_group, sell_group = await self.currency_market_order_repository.open_orders_grouped_price(market_code)
        return FetchHistoricalData(last_trades=[],
                                   open_buy_orders=buy_group,
                                   open_sell_orders=sell_group[::-1],
                                   price_candle_data=[],
                                   last_24_info=None)

    async def _order_complete_transfer_balance(self, pair1: str, pair2: str, planet: Planet, order: CurrencyMarketOrder) -> Planet:
        if order.order_type == "buy":
            pair1_qty_available = getattr(planet.resources, pair1)
            pair1_qty_available += order.amount
            setattr(planet.resources, pair1, pair1_qty_available)

        elif order.order_type == "sell":
            pair2_qty_available = getattr(planet.resources, pair2)
            pair2_qty_available += order.amount*order.price
            setattr(planet.resources, pair2, pair2_qty_available)
        return planet

    async def _limit_order_trade(self, req: TradeRequest, market_code: str, matching_orders: list[CurrencyMarketOrder]):
        amount_left = req.amount
        completed_trades = []

        planet = await self.planet_repository.get_my_planet(req.user_id, req.planet_id)

        if req.order_type == "buy":
            total_price = req.amount*req.price_unit
            pair2_qty_available = getattr(planet.resources, req.pair2.lower())
            if total_price > pair2_qty_available:
                raise NotEnoughFundsException.from_resource_name(req.pair2)

            pair2_qty_available -= total_price
            setattr(planet.resources, req.pair2.lower(), pair2_qty_available)
        elif req.order_type == "sell":
            pair1_qty = getattr(planet.resources, req.pair1.lower())
            if req.amount > pair1_qty:
                raise NotEnoughFundsException.from_resource_name(req.pair1)

            pair1_qty -= req.amount
            setattr(planet.resources, req.pair1.lower(), pair1_qty)

        planet = await self.planet_repository.update(planet)
        planet = await self.planet_repository.get_my_planet(req.user_id, req.planet_id)


        # We can match buy/sell offers
        for matching_order in matching_orders:
            to_be_filled = matching_order.to_be_filled()
            now = datetime.timestamp(datetime.now())
            dt = datetime.utcnow()

            amount_traded = 0
            if amount_left >= to_be_filled:
                matching_order.amount_filled += to_be_filled
                amount_traded = to_be_filled
                amount_left -= to_be_filled

            elif amount_left < to_be_filled:
                matching_order.amount_filled += amount_left
                amount_traded = amount_left
                amount_left = 0

            completed_trade = CurrencyMarketTrade(
                market_code=market_code,
                price=matching_order.price,
                amount=amount_traded,
                created_time=dt
            )

            matching_order.update_state()
            matching_order.updated_time = now

            if matching_order.state == "fully_filled":
                matched_order_planet = await self.planet_repository.get(matching_order.planet_id)
                matched_order_planet = await self._order_complete_transfer_balance(req.pair1.lower(),
                                                            req.pair2.lower(),
                                                            matched_order_planet,
                                                            matching_order)
                await self.planet_repository.update(matched_order_planet)

            await self.currency_market_order_repository.update(matching_order)
            await self.currency_market_trade_repository.create_trade(completed_trade)
            completed_trades.append(completed_trade)

            if amount_left <= 0:
                break

        state = "not_filled"
        if 0 < amount_left < req.amount:
            state = "partially_filled"
        elif amount_left == 0:
            state = "fully_filled"

            if req.order_type == "buy":
                pair1_amt = getattr(planet.resources, req.pair1.lower())
                pair1_amt += req.amount
                setattr(planet.resources, req.pair1.lower(), pair1_amt)
                #await self.planet_repository.update(planet)

            elif req.order_type == "sell":
                pair2_amt = getattr(planet.resources, req.pair2.lower())
                pair2_amt += req.amount*req.price_unit
                setattr(planet.resources, req.pair2.lower(), pair2_amt)
                #await self.planet_repository.update(planet)

        now = datetime.timestamp(datetime.now())
        order = CurrencyMarketOrder(
            order_type=req.order_type,
            user_id=req.user_id,
            planet_id=req.planet_id,
            created_time=now,
            updated_time=now,
            market_code=market_code,
            price=req.price_unit,
            amount=req.amount,
            amount_filled=req.amount - amount_left,
            state=state
        )

        await self.planet_repository.update(planet)
        return order, completed_trades

    async def _market_order_trade(self, req: TradeRequest, market_code: str, matching_orders: list[CurrencyMarketOrder]):
        # Weighted average calculation
        # ((quantity 1 * price 1) + (quantity 2 * price 2)) / (quantity 1 + quantity 2)
        planet = await self.planet_repository.get_my_planet(req.user_id, req.planet_id)

        if req.order_type == "buy":
            pair2_qty_available = getattr(planet.resources, req.pair2.lower())
            if req.total > pair2_qty_available:
                raise NotEnoughFundsException.from_resource_name(req.pair2)

        elif req.order_type == "sell":
            pair1_qty = getattr(planet.resources, req.pair1.lower())
            if req.total > pair1_qty:
                raise NotEnoughFundsException.from_resource_name(req.pair1)

        total_left = req.total
        completed_trades = []

        total_cost = 0
        total_amount = 0

        for matching_order in matching_orders:
            to_be_filled = matching_order.to_be_filled()
            to_be_filled_price = to_be_filled * matching_order.price

            now = datetime.timestamp(datetime.now())
            dt = datetime.utcnow()

            amount_traded = 0
            if total_left >= to_be_filled_price:
                matching_order.amount_filled += to_be_filled
                amount_traded = to_be_filled
                total_left -= to_be_filled_price

                total_cost += to_be_filled*matching_order.price
                total_amount += to_be_filled

            elif total_left < to_be_filled_price:
                amount = total_left/matching_order.price
                matching_order.amount_filled += amount
                amount_traded = amount
                total_left = 0

                total_cost += amount*matching_order.price
                total_amount += amount

            completed_trade = CurrencyMarketTrade(
                market_code=market_code,
                price=matching_order.price,
                amount=amount_traded,
                created_time=dt
            )

            matching_order.update_state()
            matching_order.updated_time = now

            if matching_order.state == "fully_filled":
                matched_order_planet = await self.planet_repository.get(matching_order.planet_id)
                matched_order_planet = await self._order_complete_transfer_balance(req.pair1.lower(),
                                                            req.pair2.lower(),
                                                            matched_order_planet,
                                                            matching_order)
                await self.planet_repository.update(matched_order_planet)

            await self.currency_market_order_repository.update(matching_order)
            await self.currency_market_trade_repository.create_trade(completed_trade)
            completed_trades.append(completed_trade)

            if total_left <= 0:
                break


        order = None
        if total_left < req.total:
            now = datetime.timestamp(datetime.now())
            order = CurrencyMarketOrder(
                order_type=req.order_type,
                user_id=req.user_id,
                planet_id=req.planet_id,
                created_time=now,
                updated_time=now,
                market_code=market_code,
                price=round(total_cost/total_amount, 2),
                amount=total_amount,
                amount_filled=total_amount,
                state="fully_filled"
            )

            if req.order_type == "buy":
                pair1_amt = getattr(planet.resources, req.pair1.lower())
                pair1_amt += total_amount
                setattr(planet.resources, req.pair1.lower(), pair1_amt)

                pair2_amt = getattr(planet.resources, req.pair2.lower())
                pair2_amt -= total_cost
                setattr(planet.resources, req.pair2.lower(), pair2_amt)

            elif req.order_type == "sell":
                pair1_amt = getattr(planet.resources, req.pair1.lower())
                pair1_amt -= total_amount
                setattr(planet.resources, req.pair1.lower(), pair1_amt)

                pair2_amt = getattr(planet.resources, req.pair2.lower())
                pair2_amt += total_cost
                setattr(planet.resources, req.pair2.lower(), pair2_amt)

            await self.planet_repository.update(planet)

        return order, completed_trades

    async def trade(self, req: TradeRequest):
        market_code = f"{req.pair1.upper()}_{req.pair2.upper()}"

        matching_orders = await self.currency_market_order_repository.find_matching_orders(market_code,
                                                                                           req.trade_type,
                                                                                           req.order_type,
                                                                                           req.price_unit)
        order, completed_trades = None, None
        if req.trade_type == "limit":
            order, completed_trades = await self._limit_order_trade(req, market_code, matching_orders)
        elif req.trade_type == "market":
            order, completed_trades = await self._market_order_trade(req, market_code, matching_orders)

        if order:
            order = await self.currency_market_order_repository.create_order(order)

        return await self.response_port.publish_response(TradeResponse(order=order,
                                                                       executed_trades=completed_trades))