from message.sv_response_base import SvResponseBase
from server_resource.resource_manager import ResourceManager
import struct

class SvPlayerJoin(SvResponseBase):
    def __init__(self, cl_request):
        super(SvAck, self).__init__(cl_request)
        self.message_id = 201

    def payload(self):
        new_message_id = ResourceManager.instance().create_new_message_id()
        return struct.pack("<BHH", self.message_id, new_message_id, cl_request.new_player_id)
