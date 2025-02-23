import os
import time
import random
import getpass
import sys
from typing import Callable
from colours import ANSI_GREEN, ANSI_PURPLE, ANSI_RED, ANSI_YELLOW, wr, wrap_colour
from inspect import signature
from challenge import (
    console_challenge,
    riddle_challenge,
    wordle_challenge,
    hangman_challenge,
    cipher_challenge,
)

# Define constants
CHALLENGES: list[Callable[[], bool]] = [
    console_challenge,
    riddle_challenge,
    wordle_challenge,
    hangman_challenge,
    cipher_challenge,
]
TEXT_SPEED = 0.02  # Typing effect speed


def call_challenge(challenge_func):
    params = signature(challenge_func).parameters
    if "can_exit" in params:
        return challenge_func(can_exit=False)
    return challenge_func()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def typewriter(text, speed=TEXT_SPEED, end="\n"):
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # time.sleep(0)
        time.sleep(speed)
    print(end, flush=True)


def boss_dialogue():
    """Handles the eerie introduction from the boss."""
    typewriter("As you enter the room, you notice a...", 0.03)
    typewriter(wr("strange silvery creature made of many hands")+wrap_colour(ANSI_RED, "SS,"))
    typewriter(wr("grasping the coolant pipes for the engine."))
    typewriter(wr("You know from experience that this anomaly is the BOSS of this place."))

    time.sleep(2)
    clear()
    typewriter(wr("h-h-hEllo friend... coMe closer I woUld like to geT a cLoser look at THOUTH formmMMM"))
    time.sleep(1.5)
    typewriter(wr("PLEASE DO NOT BE AFRAID... I would like to ask a few questions to get to know you BETTER •ᴗ•, (Y/y): "))
    time.sleep(1)
    clear()

    typewriter(wr("What is your name?"))
    time.sleep(1)
    clear()
    typewriter(wr("CAn I hAve yOUr"), 0.04)
    typewriter(wrap_colour(ANSI_RED, "BLOOD"), 0.08)
    time.sleep(0.75)
    clear()

    input(wr("What is your name? "))
    typewriter(wr("is that your final answer?"))
    time.sleep(2)
    typewriter(wr(f"should it not be {getpass.getuser().capitalize()}?"))
    time.sleep(2)
    clear()

    typewriter(wr("Actually... where are you? Hehe..."))
    time.sleep(2)


def boss_room():
    """Main boss battle sequence."""
    boss_dialogue()
    random.shuffle(CHALLENGES)

    typewriter(wr("I have a few  C H A L L E N G E S  for you..."))
    time.sleep(1)
    typewriter(wr("If you can complete them, I will let you pass..."))
    typewriter(wr("But if you fail... :D"))
    time.sleep(2)

    clear()
    for _ in range(100):
        print(wr("THE WALLS HAVE EYES THAT WATCH YOUR EVERY MOVE THE FLOOR IS ALIVE WITH WRITHING TENTACLES THE CEILING DRIPS WITH A THICK, BLACK ICHOR"))
        time.sleep(0.02)
    clear()
    typewriter(wr("You have 2 minutes..."))
    now_time = time.time()
    for _ in range(3):  # Pick three challenges
        clear()
        challenge = CHALLENGES.pop()
        if not call_challenge(challenge):
            lose()
            return False
    fin_time = time.time()

    if fin_time - now_time > 120:
        lose()
        return False
    win()
    return True


def win():
    """Handles the victory sequence."""
    typewriter(wr("THE ROOM TREMBLES AS THE ENTITY SHRIEKS IN DEFEAT"))
    time.sleep(1.5)
    typewriter(wr("THE COUNTLESS HANDS RELEASE THEIR GRIP, RECOILING INTO THE VOID"))
    time.sleep(1.5)
    typewriter("THE AIR, ONCE THICK WITH MALEVOLENCE, BEGINS TO CLEAR")
    time.sleep(1.5)
    typewriter(wr("A DOOR, WHICH WAS NEVER THERE BEFORE, NOW STANDS OPEN BEFORE YOU"))
    time.sleep(2)

    typewriter(wr("The entity whispers its final words..."))
    time.sleep(2)
    typewriter(wr("'...wE shaLl mEEt AgAiN...'"))
    time.sleep(2)

    typewriter(wrap_colour(ANSI_PURPLE, "YOU STEP FORWARD, LEAVING THIS PLACE BEHIND... FOR NOW"))
    time.sleep(2)
    typewriter(wrap_colour(ANSI_GREEN, "CONGRATULATIONS, YOU HAVE CLEANSED THIS PLACE OF CHAOS"))
    time.sleep(2)
    typewriter(wrap_colour(ANSI_YELLOW, "THE OIL MUST FLOW"))


def lose():
    """Handles the losing sequence."""
    clear()
    typewriter(wr("THE AIR GROWS THICK WITH A CRIMSON MIST..."), 0.03)
    time.sleep(1)
    typewriter(wr("A CHORUS OF VOICES SCREAMS FROM BEYOND THE VEIL..."), 0.03)
    time.sleep(1)
    typewriter(wr("YOUR SOUL IS FORFEIT. IT HAS BEEN SWALLOWED BY THE VOID."), 0.04)
    time.sleep(2)

    typewriter(wrap_colour(ANSI_RED, "YOU HAVE LOST"), 0.06)
    time.sleep(1.5)
    typewriter(wrap_colour(ANSI_RED, "GAME OVER"), 0.08)
    time.sleep(2)


# Uncomment to test
boss_room()
