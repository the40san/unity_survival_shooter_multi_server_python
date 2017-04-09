from message.cl_player_join import ClPlayerJoin

class MessageHandler:
    message_class_list = {
        100: ClPlayerJoin
    }

    def __init__(self):
        pass

    def receive_request(self, payload):
        # the first 1 byte is message type
        message_id = payload[0]
        if message_id in self.message_class_list:
            return self.message_class_list[message_id](payload)
        else:
            return None
