from pydantic import BaseModel
from typing import List, Union
from fastapi import WebSocket, WebSocketDisconnect

class Item(BaseModel):
    index: Union[int, None]
    items: Union[List[int], None]

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_text(message)