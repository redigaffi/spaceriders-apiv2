import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# Info, seems like this need to be at the top, also some have src before and others not (maybe due to relationship?)
from adapters.shared.beanie_models_adapter import UserDocument, EnergyDepositDocument, PlanetDocument, EmailDocument, \
    ResourceExchangeDocument, TokenConversionsDocument, CurrencyMarketOrderDocument, \
    CurrencyMarketTradeDocument

from decouple import config
from beanie import init_beanie
import motor.motor_asyncio
import apps.websockets.dependencies as dependencies

app = FastAPI()


@app.on_event("startup")
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        host=config('DB_URL'),
    )

    db = client[config('DB_NAME')]
    await init_beanie(database=db,
                      document_models=[UserDocument,
                                       TokenConversionsDocument,
                                       ResourceExchangeDocument,
                                       EnergyDepositDocument,
                                       PlanetDocument,
                                       EmailDocument,
                                       CurrencyMarketOrderDocument,
                                       CurrencyMarketTradeDocument]
    )

    ws_entry_point = await dependencies.ws_entry_point()
    app.add_api_websocket_route(path="/ws", endpoint=ws_entry_point)

    async def health():
        return {}

    app.router.add_api_route(path=r"/health", endpoint=health)

if __name__ == "__main__":
    uvicorn.run("__main__:app", port=8011, host='0.0.0.0', reload=True, workers=1, debug=True)