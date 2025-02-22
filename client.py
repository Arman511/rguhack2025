import random
import challenge
from colours import (
    wrap_colour,
    ANSI_RED,
    # ANSI_RESET,
    # ANSI_BLACK,
    # ANSI_GREEN,
    # ANSI_YELLOW,
    ANSI_BLUE,
    ANSI_PURPLE,
    # ANSI_CYAN,
    # ANSI_WHITE,
)

from player import Player
from room_manager import get_rooms

player = None

rooms = get_rooms()
challenge_rooms = [3, 4, 5, 6]
key_not_in_room = random.choice(challenge_rooms)
keys = [f"Key {i}" for i in range(1, 4)]


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

        if current_room.id in challenge_rooms:
            passed = challenge(current_room)
            if not passed:
                print(wrap_colour(ANSI_RED, "You died"))
                player.current_room = 0
                continue

            if current_room.id != key_not_in_room:
                player.add_item(keys.pop())
                print(wrap_colour(ANSI_BLUE, "You got a key!"))

            print(wrap_colour(ANSI_PURPLE, "You SURVIVED"))
            player.current_room = 2

        action = input("What would you like to do? ").strip().lower()

        if action not in possible_actions:
            print("Invalid action")
            continue

        if action == "quit":
            print("Goodbye!")
            return 0

        if action == "inventory":
            print(player.got_items())
            continue

        if action == "look":
            print(current_room.description)
            continue

        if action == "go":
            possible_rooms = {
                room.room_id: f"{room.room_id} - {room.name}"
                for room in rooms
                if room.can_enter_room(player)
            }
            print(wrap_colour(ANSI_BLUE, "Possible rooms: "))
            for room in possible_rooms.values():
                print(room)
            direction = input("Which direction would you like to go? ").strip().lower()
            if not direction:
                print("Invalid direction")
                continue
            if not direction.isdigit():
                print("Invalid direction")
                continue
            direction = int(direction)
            if direction not in possible_rooms:
                print("Invalid direction")
                continue
            player.change_room(direction)


if __name__ == "__main__":
    main()
