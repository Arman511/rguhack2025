import random
import sys
from boss_battle import boss_room
from challenge import challenge, random_event, item_draw
from shared import clear, typewriter
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
pygame.mixer.init()


def main():
    global player
    done_rooms = set()
    username = ""
    while not username:
        username = input("Enter your username: ")
        username = username.strip()
    player = Player(username)
    clear()

    typewriter(wrap_colour(ANSI_RED, "MISSION: FIX THE OIL RIG"))
    typewriter("The subarmarine is decending to the ocean floor and you are about to enter the oil rig.")
    typewriter("While you try to remember how to do your job you hear a tapping on the submarine window!")
    typewriter(wrap_colour(ANSI_YELLOW, "Hello there traveler, are you here to fix the ghost rig!") + " the angular fish blubs")
    time.sleep(1)
    agree = input("Are you here to fix the haunted oil rig? (Y/N): ")
    if agree == "Y" or agree == "y":
        typewriter(wrap_colour(ANSI_YELLOW, "Thank you so much!, ALL of my friends have been") + wrap_colour(ANSI_RED, " eaten ") + wrap_colour(ANSI_YELLOW, "by the ghosts so it's great to hear someone is coming to sort it!"))
    else:
        typewriter("Then buzz off!")
        typewriter("You turn the submarine around and hit the gas")
        time.sleep(3)
        pygame.mixer.Sound("music/bang.mp3").play()
        typewriter("The submarine implodes without you ever knowing it or why")
        player.player_minus_health(9999)
    typewriter(wrap_colour(ANSI_YELLOW, "I am the ghost of the rig and I will guide you through the rooms"))
    possible_actions = ["go", "inventory", "quit", "status", "help", "?"]

    while True:
        clear()
        current_room = rooms[player.get_current_room()]
        typewriter("Current room: " + wrap_colour(ANSI_RED, current_room.name))
        typewriter(current_room.description)

        if current_room.id in challenge_rooms:
            done_rooms.add(0)
            item_draw(player)
            random_event(player)
            passed = challenge(current_room.id, player)
            if not passed:
                player.player_minus_health()
                typewriter(
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
                typewriter(wrap_colour(ANSI_BLUE, "You got a key!"))

            done_rooms.add(current_room.id)
            input(
                wrap_colour(ANSI_PURPLE, "You SURVIVED") + "\n\nPRESS ENTER TO CONTINUE"
            )
            player.current_room = 2
            continue

        elif current_room.id == rooms[-1].id:
            boss_event.set()
            result = boss_room(player)
            if not result:
                input(wrap_colour(ANSI_RED, "\n\nYOU DIED - PRESS ENTER TO CONTINUE"))
            else:
                input(wrap_colour(ANSI_GREEN, "\n\nYOU WIN - PRESS ENTER TO CONTINUE"))
            os.system("cls" if os.name == "nt" else "clear")
            boss_event.clear()
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
            typewriter(wrap_colour(ANSI_BLUE, "Possible rooms: "))
            for room in possible_rooms.values():
                typewriter(room)
            direction = input("Which direction would you like to go? ").strip().lower()
            if not direction:
                typewriter("Invalid direction")
                continue
            if not direction.isdigit():
                typewriter("Invalid direction")
                continue
            direction = int(direction)
            if direction not in possible_rooms:
                typewriter("Invalid direction")
                continue
            player.change_room(direction)


musics = ["music/track1.mp3", "music/track2.mp3",
          "music/track3.mp3", "music/track4.mp3", "music/track5.mp3"]
stop_event = threading.Event()
boss_event = threading.Event()


if __name__ == "__main__":

    def play_music():
        try:
            while not stop_event.is_set():
                if boss_event.is_set():
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music/boss.mp3")
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() and not stop_event.is_set():
                        pygame.time.Clock().tick(10)
                track = random.choice(musics)
                pygame.mixer.music.load(track)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() and not stop_event.is_set():
                    pygame.time.Clock().tick(10)
        except Exception as e:
            pygame.mixer.music.stop()
            typewriter(e)

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

    pygame.mixer.music.stop()
    stop_event.set()
    music_thread.join()
    typewriter("Goodbye!")
    sys.exit(0)
