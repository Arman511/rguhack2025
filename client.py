import random
from boss_battle import boss_room
from challenge import challenge, random_event
from colours import (
    wrap_colour,
    ANSI_RED,
    # ANSI_RESET,
    # ANSI_BLACK,
    ANSI_GREEN,
    # ANSI_YELLOW,
    ANSI_BLUE,
    ANSI_PURPLE,
    # ANSI_CYAN,
    # ANSI_WHITE,
)

from menus import menus
from player import Player
from room_manager import get_rooms
import os

player = None

rooms = get_rooms()
challenge_rooms = [3, 4, 5, 6]
key_not_in_room = random.choice(challenge_rooms)
keys = [f"Key {i}" for i in range(1, 4)]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    print(wrap_colour(ANSI_RED, "MISSION: FIX OIL RIG"))

    username = ""
    global player
    done_rooms = set()
    while not username:
        username = input("Enter your username: ")
        username = username.strip()

    player = Player(username)
    possible_actions = ["go", "look", "inventory", "quit", "status", "help"]

    while True:
        print("\n")
        current_room = rooms[player.get_current_room()]
        print("Current room:", wrap_colour(ANSI_RED, current_room.name))
        print(current_room.description)

        if current_room.id in challenge_rooms:
            done_rooms.add(0)
            random_event(player)
            passed = challenge(current_room.id)
            if not passed:
                player.player_minus_health()
                print(
                    wrap_colour(
                        ANSI_PURPLE,
                        "In the last second you escape with your life and the room reset mysteriously",
                    )
                )
                input(
                    wrap_colour(
                        ANSI_RED, "\n\nYOU LOST A LIFE POINT - PRESS ENTER TO CONTINUE"
                    )
                )
                continue

            elif passed == "EXIT":
                player.current_room = 2
                continue

            if current_room.id != key_not_in_room:
                player.add_item(keys.pop())
                print(wrap_colour(ANSI_BLUE, "You got a key!"))

            done_rooms.add(current_room.id)
            print(wrap_colour(ANSI_PURPLE, "You SURVIVED"))
            player.current_room = 2

        elif current_room.id == rooms[-1].id:
            result = boss_room(player)

            if not result:
                input(wrap_colour(ANSI_RED, "\n\nYOU DIED - PRESS ENTER TO CONTINUE"))
                os.system("cls" if os.name == "nt" else "clear")
                player = Player(username)
                player.current_room = 0
                continue
            input(wrap_colour(ANSI_GREEN, "\n\nYOU WIN - PRESS ENTER TO CONTINUE"))
            ans = ""
            while True:
                ans = input("Do you wanna play again (Y/n)").strip().lower()
                os.system("cls" if os.name == "nt" else "clear")
                player = Player(username)
                player.current_room = 0
                if ans == "n":
                    break
                if not ans or ans == "Y":
                    ans = "Y"
                    break
                input(wrap_colour(ANSI_RED, "Invalid action - ENTER TO CONTINUE"))

            if ans == "Y":
                continue
            else:
                return

        action = input("What would you like to do? ").strip().lower()

        if action in possible_actions:
            if not action == "go":
                menus.main_actions(action, player, current_room)

        if action not in possible_actions:
            input(wrap_colour(ANSI_RED, "Invalid action - ENTER TO CONTINUE"))
            continue

        if action == "go":
            possible_rooms = {
                room.id: f"{room.id} - {room.name}"
                for room in rooms
                if room.can_enter_room(player)
                and player.current_room != room.id
                and room.id not in done_rooms
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
    while True:
        try:
            main()
        except SystemExit:
            ans = input("Enter Y to play again: ")
            if ans.lower() != "y":
                break

    print("Goodbye!")
