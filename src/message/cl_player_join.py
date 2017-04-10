from message.cl_request_base import ClRequestBase
from message.sv_player_join import SvPlayerJoin
from message.sv_new_player import SvNewPlayer
from server_resource.model.player import Player
from server_resource.resource_manager import ResourceManager
from logger import Logger
import struct

class ClPlayerJoin(ClRequestBase):
    def __init__(self, payload):
        super(ClPlayerJoin, self).__init__(payload)

    def parse(self):
        pass

    def execute(self, client_id):
        self.player = Player(client_id, 0, 0, 0, 100)
        ResourceManager.instance().add_player(self.player)

    def response(self):
        return SvPlayerJoin(self)

    def broadcast(self):
        return SvNewPlayer(self)
