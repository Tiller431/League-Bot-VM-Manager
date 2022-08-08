import time
import websockets
import asyncio
import os
from logger import log
baseIP = "10.0.0.2"
#baseIP = "127.0.0.1"
numofVMs = 1

debug = True


def getAllIPs():
    ips = []
    firstEnding = int(baseIP.split('.')[3])
    
    #get all IPs of VMs
    for ip in range(firstEnding, (firstEnding + numofVMs)):
        ips.append(baseIP[:-len(baseIP.split('.')[3])] + str(ip))
    
    return ips


async def remoteCmdAll(cmd):
    for ip in getAllIPs():
        await sendCmd(cmd, ip)

async def sendCmd(cmd, ip):
    async with websockets.connect(f"ws://{ip}:80") as websocket:
        await websocket.send(cmd)
        resp = await websocket.recv()
        await websocket.close()
        return resp

async def main():
    os.system("cls")
    while True:
        rsp = input("> ").lower()
        if rsp.lower() == "help":
            log.info("help - Displays this help page.")
            log.info("runall - 'runall <command>' - Runs a command on ALL vms.")
            log.info("restartall - 'restartall' - Restarts ALL vms.")
            log.info("status - 'status' - Checks the status on all vms.")
            log.info("clear - Clears the screen")
            continue
        
        if rsp.startswith("clear"):
            os.system("cls")
            continue

        if rsp.startswith("status"):
            for ip in getAllIPs():
                try:
                    resp = await sendCmd("ipconfig", ip)
                    log.info(log.Color.GREEN + "Connected to {}".format(ip) + log.Color.RESET)
                except:
                    log.error(f"FAILED to connect to {ip}!")
            continue

        if rsp.startswith("runall"):
            cmd = rsp[7:]
            for ip in getAllIPs():
                try:
                    log.debug(f"Sending command ({cmd}) to {ip}!")
                    resp = await sendCmd(cmd, ip)
                    log.info(f"{ip} - {resp}")


                except:
                    log.error(f"FAILED to send command to {ip}")
            continue
        


            




        log.info("Command not found! Try doing 'help'")
    
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().run_forever()
    asyncio.get_event_loop().close()