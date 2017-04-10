from server_handler.broadcast_message import BroadcastMessage

class ServerThreadProxy:
    def __init__(self, server_thread):
        self.server_thread = server_thread

    def send_broadcast(self, broadcast_message):
        self.server_thread.add_broadcast(broadcast_message)
