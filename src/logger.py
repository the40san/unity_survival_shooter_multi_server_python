import traceback
from datetime import datetime

class Logger:

    @staticmethod
    def log(msg):
        print("[" + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "]: " + msg)


    @staticmethod
    def error(msg):
        Logger.log(msg)
        traceback.print_exc()


