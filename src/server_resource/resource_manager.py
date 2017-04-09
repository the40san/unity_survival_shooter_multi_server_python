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
        self.lock = threading.Lock()
        self.bots = set([])
        self.players = set([])
        self.latest_player_id = 0

    def add_player(self, new_player):
        self.lock.acquire()

        self.players.add(new_player)

        self.lock.release()

    def create_player_id(self):
        self.lock.acquire()

        self.latest_player_id += 1

        self.lock.release()
        return self.latest_player_id

    @classmethod
    def instance(cls):
        if cls.__instance == None:
            return cls()
        else:
            return cls.__instance
