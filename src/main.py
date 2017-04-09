from server_main_loop import ServerMainLoop
from server_resource.resource_manager import ResourceManager
from logger import Logger

import signal
import os
import time
import sys

def signal_handler(signum, stack):
    Logger.log("signal received: " + str(signum))
    sys.exit()

def main():
    signal.signal(signal.SIGINT, signal_handler)
    main_loop = ServerMainLoop()
    main_loop.exec()

if __name__ == '__main__':
    main()
