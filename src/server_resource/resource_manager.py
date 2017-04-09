import threading

class ResourceManager:
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            cls.__instance.initialize()
        return cls.__instance

    def __init__(self):
        pass

    def initialize(self):
        self.lock_for_resource = threading.Lock()
        self.lock_for_message = threading.Lock()
        self.bots = set([])
        self.players = set([])
        self.latest_player_id = 0
        self.latest_message_id = 1

    def add_player(self, new_player):
        self.lock_for_resource.acquire()

        self.players.add(new_player)

        self.lock_for_resource.release()

    def create_player_id(self):
        self.lock_for_resource.acquire()

        self.latest_player_id += 1

        self.lock_for_resource.release()
        return self.latest_player_id

    def create_new_message_id(self, num = 1):
        self.lock_for_message.acquire()

        begin = self.latest_message_id + 1
        self.latest_message_id += num

        self.lock_for_message.release()
        return begin

    @classmethod
    def instance(cls):
        if cls.__instance == None:
            return cls()
        else:
            return cls.__instance
