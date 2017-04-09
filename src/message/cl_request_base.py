import struct

class ClRequestBase:
    def __init__(self, payload):
        self.message_id = struct.unpack("<B", payload[0:1])[0]
        self.message_unique_id = struct.unpack("<H", payload[1:3])[0]
        self.payload = payload
        self.parse()

    def parse(self):
        """ OVERRIDE THIS TO IMPLEMENT """
        raise

    def execute(self):
        """ OVERRIDE THIS TO IMPLEMENT """
        raise

    def response(self):
        """ OVERRIDE THIS TO IMPLEMENT """
        raise
        return
