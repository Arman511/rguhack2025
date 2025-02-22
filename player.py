class Player:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Player, cls).__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, "initialized"):
            self.name = name
            self.score = 0
            self.karma = 0
            self.initialized = True

    def add_score(self, score):
        self.score += score

    def __str__(self):
        return f"{self.name} has {self.score} points"

    def get_karma(self):
        return self.karma

    def add_karma(self, karma):
        self.karma += karma

    def remove_karma(self, karma):
        self.karma -= karma
