from fastapi import APIRouter, WebSocket, WebSocketDisconnect
router = APIRouter()
connections = []

@router.websocket("/notifications")
async def notifications(ws: WebSocket):
    await ws.accept()
    connections.append(ws)
    try:
        while True:
            data = await ws.receive_text()
            # echo for demo
            for conn in list(connections):
                try:
                    await conn.send_text(data)
                except:
                    connections.remove(conn)
    except WebSocketDisconnect:
        if ws in connections:
            connections.remove(ws)
