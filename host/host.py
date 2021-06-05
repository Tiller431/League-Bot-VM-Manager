import time
from websocket import create_connection
import os
baseIP = "192.168.1.216"
#baseIP = "127.0.0.1"
numofVMs = 20

debug = True

def log(message, debugmsg=False):
    hr = time.localtime().tm_hour
    minn = time.localtime().tm_min
    sec = time.localtime().tm_sec
    if debugmsg:
        print(f"[{hr}:{minn}:{sec}] (DEBUG)>> ", message)
    else:
        print(f"[{hr}:{minn}:{sec}]>> ", message)


def getAllIPs():
    ips = []
    
    firstEnding = int(baseIP.split('.')[3])
    
    for ip in range(firstEnding, (firstEnding + numofVMs)):
        ips.append(baseIP[:-len(baseIP.split('.')[3])] + str(ip))
    return ips


def remoteCmdAll(cmd):
    for ip in getAllIPs():
        sendCmd(cmd, ip)

def sendCmd(cmd, ip):
    uri = f"ws://{ip}:80/"
    try:
        ws = create_connection(uri)
    except:
        log(f"Couldn't connect to {ip}! Did not run '{cmd}'")

    ws.send(cmd)
    result =  ws.recv()
    ws.close()
    log(f"Ran command: ({cmd}) on {ip}")
    if debug:
        log(f"Output: {result}", debugmsg=True)

if __name__ == '__main__':
    while True:
        rsp = input("> ")
        if rsp.lower() == "help":
            print("help - Displays this help page.")
            print("runall - 'runall <command>' - Runs a command on ALL vms.")
            print("restartall - 'restartall' - Restarts ALL vms.")
            print("status - 'status' - Checks the status on all vms.")
            print("clear - Clears the screen")
            continue
        
        if rsp.startswith("clear"):
            os.system("cls")
            continue

        if rsp.lower().startswith("status"):
            for ip in getAllIPs():
                try:
                    uri = f"ws://{ip}:80/"
                    ws = create_connection(uri, timeout=0.5)
                    ws.close()
                    log(f"{ip} is UP!")
                except:
                    log(f"FAILED to connect to {ip}!")
            continue

        if rsp.lower().startswith("runall"):
            cmd = rsp[7:]
            for ip in getAllIPs():
                try:
                    uri = f"ws://{ip}:80/"
                    ws = create_connection(uri, timeout=0.1)
                    log(f"Sending command ({cmd}) to {ip}!")
                    ws.send(cmd)
                    result = ws.recv()
                    if debug:
                        log(f"Output: {result}", debugmsg=True)
                    ws.close()
                except:
                    log(f"FAILED to send command to {ip}")
                    ws.close()
            continue





        print("Command not found! Try doing 'help'")