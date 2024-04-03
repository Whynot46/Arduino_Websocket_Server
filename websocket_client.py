import asyncio
import websockets

async def listen_server():
    async with websockets.connect("ws://192.168.1.10") as websocket:
        while True:
            response = await websocket.recv()
            print(response)


asyncio.get_event_loop().run_until_complete(listen_server())