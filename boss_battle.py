import time
import random
from typing import Callable
from colours import wr, wrap_colour
from inspect import signature


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
    import os

    os.system("cls" if os.name == "nt" else "clear")


def boss_room():
    print("As you enter the room you notice a ", end="")
    print(wr("""strange silvery creture made of many handss, grasping coolant pipe for the engine"""), end=" ")
    print("You know from experice that this", end=" ")
    print(        wr(
            "anomaly from between the walls is the BOSS of this place"
        ),
    )
    print(
        wr(
            "h-h-hEllo friend... coMe closer I woUld like to geT a cLoser look at THOUTH formmMMM"
        ),
        end=" ",
    )
    print(wr("/'"), end=" ")
    input(
        wr(
            "PLEASE DO NOT BE AFRAID... I would like to ask a few questions to get to know you BETTER •ᴗ•"
        )
    )
    time.sleep(1)
    clear()
    print(wr("What is your name?"))
    random.shuffle(challenges)

    for _ in range(3):  # Pick three challenges
        chal = challenges.pop()
        if not call_challenge(chal):
            return False

    return True


# TEST CODE
# boss_room()
