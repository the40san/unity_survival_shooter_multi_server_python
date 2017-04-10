from message.sv_response_base import SvResponseBase
from server_resource.resource_manager import ResourceManager
import struct

class SvNewPlayer(SvResponseBase):
    def __init__(self, cl_request):
        super(SvNewPlayer, self).__init__(cl_request)
        self.message_id = 202

    def payload(self):
        new_message_id = ResourceManager.instance().create_new_message_id()
        player = self.cl_request.player

        return struct.pack("<BHIfffH",
                self.message_id,
                new_message_id,
                player.id,
                player.x,
                player.y,
                player.z,
                player.health)
