import os

from colours import *


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.karma = 0
        self.health = 3
        with open("items.txt", "r") as f:
            self.inventory = {}
            for line in f:
                item = line.strip()
                if item in self.inventory:
                    self.inventory[item] + 1
                else:
                    self.inventory[item] = 1

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
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def remove_item_from_inventory(self, item):
        if item in self.inventory:
            self.inventory[item] -= 1
            if self.inventory[item] == 0:
                self.inventory.pop(item, None)
        else:
            print("Error: Item not in inventory")

    def got_items(self):
        return [item for item in self.inventory if self.inventory[item] >= 1]

    def get_current_room(self):
        return self.current_room

    def change_room(self, room):
        self.current_room = room

    def player_minus_health(self, damage=1):
        self.health -= damage
        if self.health <= 0:
            input(wrap_colour(ANSI_RED, "\n\nYOU DIED - PRESS ENTER TO CONTINUE"))
            os.system("cls" if os.name == "nt" else "clear")
            raise SystemExit
