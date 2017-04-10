import threading
import socket
import queue
from client_handler.message_handler import MessageHandler
from server_resource.resource_manager import ResourceManager
from server_handler.broadcast_message import BroadcastMessage
from logger import Logger

class ClientThread(threading.Thread):
    def __init__(self, socket, server_thread_proxy):
        self.socket = socket
        self.message_handler = MessageHandler()
        self.client_id = ResourceManager.instance().create_client_id()
        self.broadcast_queue = queue.Queue()
        self.server_thread_proxy = server_thread_proxy
        threading.Thread.__init__(self)

    def run(self):
        self.socket.settimeout(10.0)

        while True:
            try:
                self.send_broadcast_to_client()
                msg = bytes(self.receive_message_from_socket())
            except OSError:
                Logger.log("socket receive timeout. closing")
                break
            except:
                Logger.error("someting wrong")
                break
            else:
                if len(msg) == 0:
                    # client disconnected
                    break
                else:
                    cl_request = self.message_handler.receive_request(msg)
                    self.handle_client_request(cl_request)

        self.disconnect()

    def handle_client_request(self, cl_request):
        if cl_request != None:
            try:
                cl_request.execute(self.client_id)
                self.send_message_to_socket(cl_request.response().payload())

                broadcast_message = cl_request.broadcast()
                if broadcast_message is not None:
                    self.server_thread_proxy.send_broadcast(BroadcastMessage(self.client_id, broadcast_message))

            except:
                Logger.error("error while processing: " + str(cl_request.payload))
        return


    def receive_message_from_socket(self):
        return self.socket.recv(4096)


    def send_message_to_socket(self, payload):
        self.socket.send(payload)
        Logger.log("sending " + str(self.client_id) + " :" + str(payload))
        return


    def add_broadcast_message(self, message):
        self.broadcast_queue.put(message)
        return


    def send_broadcast_to_client(self):
        if self.broadcast_queue.empty():
            return
        else:
            while not self.broadcast_queue.empty():
                message = self.broadcast_queue.get()
                self.send_message_to_socket(message.message.payload())
            return


    def disconnect(self):
        self.socket.close()
        Logger.log("disconnecting")
        return
