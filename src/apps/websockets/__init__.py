from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# Info, seems like this need to be at the top, also some have src before and others not (maybe due to relationship?)
from adapters.shared.beanie_models_adapter import UserDocument, EnergyDepositDocument, PlanetDocument, EmailDocument, \
    LevelUpRewardClaimsDocument, ResourceExchangeDocument, TokenConversionsDocument

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
                      document_models=[UserDocument, TokenConversionsDocument, ResourceExchangeDocument, EnergyDepositDocument, PlanetDocument, EmailDocument, LevelUpRewardClaimsDocument]
    )

    ws_controller = await dependencies.ws_controller()
    app.add_api_websocket_route(path="/ws/{wallet_id}", endpoint=ws_controller.trade)
