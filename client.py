import random
import sys
from boss_battle import boss_room
from challenge import challenge, random_event, item_draw
from colours import (
    wrap_colour,
    ANSI_RED,
    # ANSI_RESET,
    # ANSI_BLACK,
    ANSI_GREEN,
    ANSI_YELLOW,
    ANSI_BLUE,
    ANSI_PURPLE,
    # ANSI_CYAN,
    # ANSI_WHITE,
)
import pygame


from menus import menus
from player import Player
from room_manager import get_rooms
import os
import threading
import time

player = None

rooms = get_rooms()
challenge_rooms = [3, 4, 5, 6]
key_not_in_room = random.choice(challenge_rooms)
keys = [f"Key {i}" for i in range(1, 4)]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clear()
    print(wrap_colour(ANSI_RED, "MISSION: FIX THE OIL RIG"))
    print("The subarmarine is decending to the ocean floor and you are about to enter the oil rig.")
    print("While you try to remember how to do your job you hear a tapping on the window!")
    print(wrap_colour(ANSI_YELLOW, "Hello there traveler, are you here to fix the ghost rig!"), " the angular fish blubs")
    time.sleep(1)
    agree = input("Are you here to fix the haunted oil rig? (Y/N): ")
    if agree == "Y" or agree == "y":
        print(wrap_colour(ANSI_YELLOW, "Thank you so much!, ALL of my friends have been"), wrap_colour(ANSI_RED, "eaten"), wrap_colour(ANSI_YELLOW, "by the ghosts so it's great to hear someone is coming to sort it!"))
    else:
        print("Then buzz off!")
        print("You turn the submarine around")
    print(wrap_colour(ANSI_YELLOW, "I am the ghost of the rig and I will guide you through the rooms"))

    username = ""
    global player
    done_rooms = set()
    while not username:
        username = input("Enter your username: ")
        username = username.strip()

    player = Player(username)
    possible_actions = ["go", "inventory", "quit", "status", "help", "?"]

    while True:
        clear()
        current_room = rooms[player.get_current_room()]
        print("Current room:", wrap_colour(ANSI_RED, current_room.name))
        print(current_room.description)

        if current_room.id in challenge_rooms:
            done_rooms.add(0)
            item_draw(player)
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
            input(
                wrap_colour(ANSI_PURPLE, "You SURVIVED") + "\n\nPRESS ENTER TO CONTINUE"
            )
            player.current_room = 2
            continue

        elif current_room.id == rooms[-1].id:
            result = boss_room()

            if not result:
                input(wrap_colour(ANSI_RED, "\n\nYOU DIED - PRESS ENTER TO CONTINUE"))
            else:
                input(wrap_colour(ANSI_GREEN, "\n\nYOU WIN - PRESS ENTER TO CONTINUE"))
            os.system("cls" if os.name == "nt" else "clear")
            raise SystemExit

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


musics = ["music/track1.mp3", "music/track2.mp3",
          "music/track3.mp3", "music/track4.mp3", "music/track5.mp3"]
stop_event = threading.Event()


if __name__ == "__main__":

    def play_music():
        try:
            pygame.mixer.init()
            while not stop_event.is_set():
                track = random.choice(musics)
                pygame.mixer.music.load(track)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() and not stop_event.is_set():
                    pygame.time.Clock().tick(10)
            pygame.mixer.music.stop()
        except Exception as e:
            pygame.mixer.music.stop()
            print(e)

    music_thread = threading.Thread(target=play_music, daemon=True)
    music_thread.start()
    while True:
        try:
            main()
        except SystemExit:
            ans = input("Enter Y to play again: ")
            if ans.lower() != "y":
                stop_event.set()
                break
        except KeyboardInterrupt:
            stop_event.set()
            break

    stop_event.set()
    music_thread.join()
    print("Goodbye!")
    sys.exit(0)
