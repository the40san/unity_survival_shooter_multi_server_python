from message.sv_response_base import SvResponseBase
import struct

class SvAck(SvResponseBase):
    def __init__(self, cl_request):
        super(SvAck, self).__init__(cl_request)
        self.message_id = 200

    def payload(self):
        return struct.pack("<BH", self.message_id, self.cl_request.message_unique_id)
