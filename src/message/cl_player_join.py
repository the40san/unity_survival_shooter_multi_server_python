from message.cl_request_base import ClRequestBase
from message.sv_ack import SvAck
from server_resource.model.player import Player
from logger import Logger
import struct

class ClPlayerJoin(ClRequestBase):
    def __init__(self, payload):
        super(ClPlayerJoin, self).__init__(payload)

    def parse(self):
        pass

    def execute(self, client_id):
        player = Player(client_id, 0, 0, 0, 100)
        ResourceManager.instance().add_player(player)

    def response(self):
        return SvAck(self)
