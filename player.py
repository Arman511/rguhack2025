class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.karma = 0
        with open("items.txt", "r") as f:
            self.inventory = {line.strip(): 0 for line in f}

        self.current_room = 0

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

    def add_item_to_inventory(self, item):
        self.inventory[item] = 1

    def remove_item_from_inventory(self, item):
        del self.inventory[item]

    def got_items(self):
        return [item for item in self.inventory if self.inventory[item] == 1]

    def get_current_room(self):
        return self.current_room

    def change_room(self, room):
        self.current_room = room
