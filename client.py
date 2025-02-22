import random
from colours import (
    wrap_colour,
    ANSI_RED,
    # ANSI_RESET,
    # ANSI_BLACK,
    # ANSI_GREEN,
    # ANSI_YELLOW,
    # ANSI_BLUE,
    # ANSI_PURPLE,
    # ANSI_CYAN,
    # ANSI_WHITE,
)

from player import Player
from room_manager import get_rooms

player = None

rooms = get_rooms()
key_not_in_room = random.choice([3, 4, 5, 6])


def main():
    print(wrap_colour(ANSI_RED, "MISSION: FIX OIL RIG"))

    username = ""
    global player
    while not username:
        username = input("Enter your username: ")
        username = username.strip()

    player = Player(username)
    possible_actions = ["go", "look", "inventory", "quit"]

    while True:
        print("\n")
        current_room = rooms[player.get_current_room()]
        print("Current room: ", wrap_colour(ANSI_RED, current_room.name))
        print(current_room.description)

        if current_room.id == key_not_in_room:
            print(wrap_colour(ANSI_RED, "You found a key!"))
            player.add_item_to_inventory("Key 1")

        action = input("What would you like to do? ").strip().lower()

        if action not in possible_actions:
            print("Invalid action")
            continue

        if action == "quit":
            print("Goodbye!")
            break

        if action == "inventory":
            print(player.got_items())
            continue

        if action == "look":
            print(current_room.description)
            continue

        if action == "go":
            direction = input("Which direction would you like to go? ").strip().lower()
            next_room = current_room.go(direction)
            if next_room:
                if next_room.can_enter_room(player):
                    player.change_room(next_room.id)
                else:
                    print("You cannot enter this room")
            else:
                print("Invalid direction")


if __name__ == "__main__":
    main()
