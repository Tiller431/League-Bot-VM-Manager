import asyncio
from re import sub
import websockets
import subprocess
import urllib

version = "0.0.1"

#either the github or a webserver that leads to the vm folder
githubURL = "https://raw.githubusercontent.com/Tiller431/League-Bot-VM-Manager/main/"

def checkUpdate():
    LatestVersionURL = githubURL + "version"
    newSctiptURL = githubURL + "dist/vm.exe"

    try:
        with urllib.request.urlopen(LatestVersionURL) as response:
            latestVersion = response.read().decode('utf-8')
            if latestVersion == version:
                print("You are up to date!")
            else:
                print("You are not up to date!")
                print("Downloading new version...")
                with urllib.request.urlopen(newSctiptURL) as response:
                    newScript = response.read()
                    #delete old exe
                    subprocess.getoutput("del vm.exe")
                    #write new exe
                    with open("vm.exe", "wb") as f:
                        f.write(newScript)
                    print("Done updating!\n Restarting VM...")
                    #restart windows
                    subprocess.run("shutdown -r -t 0")

    except:
        print("Failed to check for updates!")





async def shell(websocket, path):
    while True:
        cmd = await websocket.recv()
        print(f"Running: {cmd}")
        output = subprocess.getoutput(cmd) + '\n'
        await websocket.send(output)
        


if __name__ == '__main__':
    checkUpdate()
    start_shell = websockets.serve(shell, "0.0.0.0", 80)

    asyncio.get_event_loop().run_until_complete(start_shell)
    asyncio.get_event_loop().run_forever()
