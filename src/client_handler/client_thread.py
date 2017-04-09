import threading
import socket
from client_handler.message_handler import MessageHandler
from logger import Logger

class ClientThread(threading.Thread):
    def __init__(self, socket):
        self.socket = socket
        self.message_handler = MessageHandler()
        threading.Thread.__init__(self)

    def run(self):
        self.socket.settimeout(10.0)

        while True:
            try:
                msg = bytes(self.receive_message_from_socket())
            except OSError:
                Logger.log("socket receive timeout. closing")
                self.disconnect()
                break
            except:
                Logger.log("someting wrong")
                break
            else:
                if len(msg) == 0:
                    # no message.
                    continue
                else:
                    cl_request = self.message_handler.receive_request(msg)
                    self.handle_client_request(cl_request)

    def handle_client_request(self, cl_request):
        if cl_request != None:
            try:
                cl_request.execute()
                self.send_message_to_socket(cl_request.response().payload())
            except:
                import traceback
                traceback.print_exc()
                Logger.log("error while processing: " + str(cl_request.payload))
        return

    def receive_message_from_socket(self):
        return self.socket.recv(4096)

    def send_message_to_socket(self, payload):
        self.socket.send(payload)
        return

    def disconnect(self):
        self.socket.close()
        return
