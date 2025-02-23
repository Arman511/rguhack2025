import os
import time
import random
from typing import Callable
from colours import ANSI_RED, wr, wrap_colour
from inspect import signature
import getpass


from challenge import (
    console_challenge,
    riddle_challenge,
    wordle_challenge,
    hangman_challenge,
    cipher_challenge,
)

challenges: list[Callable[[], bool]] = [
    console_challenge,
    riddle_challenge,
    wordle_challenge,
    hangman_challenge,
    cipher_challenge,
]


def call_challenge(challenge_func):
    params = signature(challenge_func).parameters
    if "can_exit" in params:
        return challenge_func(can_exit=False)
    return challenge_func()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def boss_room():
    print("As you enter the room, you notice a ", end="")
    print(wr("strange silvery creature made of many hands"), wrap_colour(ANSI_RED, "SS"), wr(", grasping the coolant pipes for the engine."), end=" ")
    print("You know from experience that this", end=" ")
    print(wr("anomaly from between the cracks is the BOSS of this place."))

    print(wr("\nThe creature speaks in a voice that sounds like a thousand whispers..."))
    time.sleep(4)
    clear()
    print(wr("h-h-hEllo friend... coMe closer I woUld like to geT a cLoser look at THOUTH formmMMM"))
    print(wr("PLEASE DO NOT BE AFRAID... I would like to ask a few questions to get to know you BETTER •ᴗ•, (Y/y): "))
    time.sleep(10)
    clear()
    print(wr("What is your name?"))
    time.sleep(2)
    clear()
    print(wr("What is your"), wrap_colour(ANSI_RED, "BLOOD"), wr("type?"))
    time.sleep(0.75)
    clear()
    input(wr("What is your name? "))
    print(wr("is that your final answer?"))
    time.sleep(2)
    print(wr(f"Should it not be {getpass.getuser().capitalize()}"))
    time.sleep(3)
    print(wr("..."))
    time.sleep(2)
    clear()
    print(wr("Actually where are you hehe?"))

    random.shuffle(challenges)

    print(wr("I have a few challenges for you..."))
    time.sleep(2)
    print(wr("If you can complete them, I will let you pass..."))
    print(wr("But if you fail... :D"))
    time.sleep(2)
    clear()
    for _ in range(100):
        print(wr("THE WALLS HAVE EYES THAT WATCH YOUR EVERY MOVE"), end=" ")
        print(wr("THE FLOOR IS ALIVE WITH WRITHING TENTACLES"), end=" ")
        print(wr("THE CEILING DRIPS WITH A THICK, BLACK ICHOR"))
        time.sleep(0.05)
    clear()
    for _ in range(3):  # Pick three challenges
        chal = challenges.pop()
        if not call_challenge(chal):
            lose()
            return False
        
    win()
    return True


def win():
    print()
    print(wr("THE ROOM TREMBLES AS THE ENTITY SHRIEKS IN DEFEAT"))
    time.sleep(2)
    print(wr("THE COUNTLESS HANDS RELEASE THEIR GRIP, RECOILING INTO THE VOID"))
    time.sleep(2)
    print("THE AIR, ONCE THICK WITH MALEVOLENCE, BEGINS TO CLEAR")
    time.sleep(2)
    print(wr("A DOOR, WHICH WAS NEVER THERE BEFORE, NOW STANDS OPEN BEFORE YOU"))
    time.sleep(2)
    print(wr("THE ENTITY WHISPERS ITS FINAL WORDS..."))
    time.sleep(3)
    print(wr("\"...wE shaLl mEEt AgAiN...\""))
    time.sleep(3)
    print("YOU STEP FORWARD, LEAVING THIS PLACE BEHIND... FOR NOW")
    time.sleep(2)
    print("CONGRATULATIONS, YOU HAVE CLEANSED THIS PLACE OF CHAOS")
    time.sleep(2)
    print("THE OIL MUST FLOW")


def lose():
    for _ in range(1000):
        print(wr("THE AIR  G R O W S  THICK WITH A  C R I M S O N  MIST,"), end=" ")
        print(wr("A CHORUS OF VOICES  S C R E A M S  FROM BEYOND THE VEIL,"), end=" ")
        print(wr("YOUR  F L E S H  WRITHES AS COUNTLESS HANDS REACH FROM THE VOID,"), end=" ")
        print(wr("YOU FEEL YOURSELF UNRAVELING, THREAD BY THREAD, INTO THE  N O T H I N G N E S S ,"), end=" ")
        print(wr("THE ENTITY  L A U G H S , A SOUND THAT SPLITS YOUR MIND LIKE GLASS,"), end=" ")
        print(wr("YOUR SOUL IS  F O R F E I T ... IT HAS BEEN SWALLOWED BY THE VOID"))
        time.sleep(0.02)
    print(wr("YOU HAVE LOST"))
    time.sleep(2)
    print(wr("GAME OVER"))
    time.sleep(2)


# TEST CODE
# boss_room()
