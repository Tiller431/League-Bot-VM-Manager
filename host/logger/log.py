
import os
import time


debugConf = True

class Color:
    #console colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    DARKGREY = "\033[90m"
    RESET = "\033[0m"



def info(msg):
    #time - [INFO] - msg
    print(Color.CYAN + "{} - [INFO] - {}".format(time.strftime("%H:%M:%S"), msg) + Color.RESET)

def error(msg):
    #time - [ERROR] - msg
    print(Color.RED + "{} - [ERROR] - {}".format(time.strftime("%H:%M:%S"), msg) + Color.RESET)

def debug(msg):
    #time - [DEBUG] - msg
    if debugConf:
        print(Color.MAGENTA + "{} - [DEBUG] - {}".format(time.strftime("%H:%M:%S"), msg) + Color.RESET)