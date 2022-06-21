from datetime import datetime
from datetime import timedelta
from pydantic import BaseModel

from core.shared.models import CurrencyMarketOrder, CurrencyMarketTrade, OpenOrdersGroupedByPrice, \
    PriceCandleDataGroupedByTimeInterval
from core.shared.ports import ResponsePort, CurrencyMarketOrderRepositoryPort, CurrencyMarketTradeRepositoryPort
from dataclasses import dataclass


class TradeRequest(BaseModel):
    trade_type: str = None  # limit/market ...
    user_id: str = None
    planet_id: str = None
    order_type: str = None  # 'buy' or 'sell'
    pair1: str = None  # metal/petrol
    pair2: str = None  # metal/petrol
    price: float = None  # price to be paid in pair 2
    amount: float = None  # amount in pair 1 to be bought


class TradeResponse(BaseModel):
    order: CurrencyMarketOrder
    executed_trades: list[CurrencyMarketTrade]


class FetchHistoricalData(BaseModel):
    last_trades: list[CurrencyMarketTrade]
    open_buy_orders: list[OpenOrdersGroupedByPrice]
    open_sell_orders: list[OpenOrdersGroupedByPrice]
    price_candle_data: dict[str, PriceCandleDataGroupedByTimeInterval|None]


@dataclass
class CurrencyMarket:
    currency_market_order_repository: CurrencyMarketOrderRepositoryPort
    currency_market_trade_repository: CurrencyMarketTradeRepositoryPort
    response_port: ResponsePort

    async def _format_price_candle_data(self, price_candle_data):
        price_candle_tmp = {}
        for p in price_candle_data:
            price_candle_tmp[p.id['date_formatted']] = p

        # amount of bars
        day1ago = datetime.utcnow() - timedelta(minutes=30)
        now = datetime.utcnow()
        previous_price = None
        prices = {}

        # if len(price_candle_data) > 0:
        #     first_candle_date = datetime.strptime(price_candle_data[0].id['date_formatted'], "%Y-%m-%dT%H:%M:00.000000Z")
        #     if now > first_candle_date:
        #         last_candle = price_candle_data[len(price_candle_data)-1]
        #         minute = day1ago.strftime("%M")
        #
        #         previous_price = PriceCandleDataGroupedByTimeInterval(_id={
        #             "minute": minute,
        #             "date_formatted": now.strftime("%Y-%m-%dT%H:%M:00.000000Z"),
        #             "interval": minute
        #         }, open=last_candle.close, close=last_candle.close, high=last_candle.close,
        #             low=last_candle.close)

        while day1ago < now:
            date_formatted = day1ago.strftime("%Y-%m-%dT%H:%M:00.000000Z")
            minute = day1ago.strftime("%M")

            if date_formatted in price_candle_tmp:
                previous_price = price_candle_tmp[date_formatted]
            else:
                if previous_price is not None:
                    previous_price = PriceCandleDataGroupedByTimeInterval(_id={
                        "minute": minute,
                        "date_formatted": date_formatted,
                        "interval": minute
                    }, open=previous_price.close, close=previous_price.close, high=previous_price.close,
                        low=previous_price.close)

            if previous_price is not None:
                prices[date_formatted] = previous_price

            day1ago += timedelta(minutes=1)

        return prices

    async def fetch_current_candle_data(self, market_code: str):
        start = datetime.utcnow()
        start_str = start.strftime("%Y-%m-%dT%H:%M:00.000000Z")
        start_dt = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:00.000000Z")

        end = start_dt + timedelta(minutes=1)
        end_str = end.strftime("%Y-%m-%dT%H:%M:00.000000Z")
        end_dt = datetime.strptime(end_str, "%Y-%m-%dT%H:%M:00.000000Z")

        # remove seconds ad leave minute only

        price_candle_data = await self.currency_market_trade_repository.price_candle_data_grouped_time_range(market_code, 1, start_dt, end_dt)
        tmp = None
        if len(price_candle_data) > 0:
            tmp = price_candle_data[0]

        price_candle_data_formatted = {
            start_str: tmp
        }
        return FetchHistoricalData(last_trades=[],
                                   open_buy_orders=[],
                                   open_sell_orders=[],
                                   price_candle_data=price_candle_data_formatted)

    # Fetch all data for trading
    async def fetch_historical_data(self, market_code: str):
        buy_group, sell_group = await self.currency_market_order_repository.open_orders_grouped_price(market_code)
        last_trades = await self.currency_market_trade_repository.all_descending_limit(market_code, 50)
        price_candle_data = await self.currency_market_trade_repository.price_candle_data_grouped_time(market_code, 1)
        prices = await self._format_price_candle_data(price_candle_data)
        # a = await self.fetch_last_candle_data(market_code)

        return FetchHistoricalData(last_trades=last_trades,
                                   open_buy_orders=buy_group,
                                   open_sell_orders=sell_group[::-1],
                                   price_candle_data=prices)

    async def fetch_order_book_data(self, market_code: str):
        buy_group, sell_group = await self.currency_market_order_repository.open_orders_grouped_price(market_code)
        return FetchHistoricalData(last_trades=[], open_buy_orders=buy_group, open_sell_orders=sell_group[::-1], price_candle_data=[])

    async def trade(self, req: TradeRequest):
        market_code = f"{req.pair1.upper()}_{req.pair2.upper()}"

        matching_orders = await self.currency_market_order_repository.find_matching_orders(market_code,
                                                                                           req.order_type,
                                                                                           req.price)

        amount_left = req.amount
        completed_trades = []

        last_price = None

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

        now = datetime.timestamp(datetime.now())
        order = CurrencyMarketOrder(
            order_type=req.order_type,
            user_id=req.user_id,
            planet_id=req.planet_id,
            created_time=now,
            updated_time=now,
            market_code=market_code,
            price=req.price,
            amount=req.amount,
            amount_filled=req.amount - amount_left,
            state=state
        )

        await self.currency_market_order_repository.create_order(order)
        trade_response = TradeResponse(order=order, executed_trades=completed_trades)
        return await self.response_port.publish_response(trade_response)
