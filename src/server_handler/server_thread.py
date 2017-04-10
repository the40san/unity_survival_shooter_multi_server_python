import threading
import socket
import queue
from logger import Logger
from server_handler.broadcast_message import BroadcastMessage

class ServerThread(threading.Thread):
    def __init__(self):
        self.client_threads = set([])
        self.shutting_down = False
        self.broadcast_queue = queue.Queue(256)
        threading.Thread.__init__(self)

    def run(self):
        while not self.shutting_down:
            self.broadcast_message_to_client()

    def add_client(self, client_thread):
        self.client_threads.add(client_thread)

    def remove_client(self, client_thread):
        self.client_threads.remove(client_thread)

    def add_broadcast(self, broadcast_message):
        Logger.log("adding broadcast")
        self.broadcast_queue.put(broadcast_message)

    def broadcast_message_to_client(self):
        if self.broadcast_queue.empty():
            return
        else:
            message = self.broadcast_queue.get()
            for cl in self.client_threads:
                if cl.client_id != message.client_id:
                    cl.add_broadcast_message(message)

    def shutdown(self):
        self.shutting_down = True
