import struct
from logger import Logger

class ClRequestBase:
    def __init__(self, payload):
        self.message_id = struct.unpack("<B", payload[0:1])[0]
        self.message_unique_id = struct.unpack("<H", payload[1:3])[0]
        self.payload = payload
        Logger.log("processing: " + type(self).__name__)
        self.parse()

    def parse(self):
        """ OVERRIDE THIS TO IMPLEMENT """
        raise

    def execute(self, client_id):
        """ OVERRIDE THIS TO IMPLEMENT """
        raise

    def response(self):
        """ OVERRIDE THIS TO IMPLEMENT """
        raise

    def broadcast(self):
        """ OVERRIDE THIS TO IMPLEMENT """
        return None
