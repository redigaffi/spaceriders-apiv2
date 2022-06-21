from dataclasses import dataclass
from core.currency_market import CurrencyMarket, TradeRequest


@dataclass
class WebsocketController:
    trading_use_case: CurrencyMarket

    async def trade(self, req: TradeRequest):
        return await self.trading_use_case.trade(req)

    async def trade_fetch_historical_data(self, market_code: str, candle_time_frame: str):
        return await self.trading_use_case.fetch_historical_data(market_code, candle_time_frame)

    async def trade_fetch_order_book_data(self, market_code: str):
        return await self.trading_use_case.fetch_order_book_data(market_code)

    async def trade_fetch_current_candle(self, market_code: str, candle_time_frame: str):
        return await self.trading_use_case.fetch_current_candle_data(market_code, candle_time_frame)
