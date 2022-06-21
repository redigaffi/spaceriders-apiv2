from dataclasses import dataclass
from fastapi import WebSocket

@dataclass
class WebsocketController:

    @staticmethod
    async def trade(websocket: WebSocket, wallet_id: str = None):
        print(f"ASD {wallet_id}")
        pass
