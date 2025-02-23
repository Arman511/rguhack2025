import time
import random
from typing import Callable
from colours import (
    wrap_random_colour_per_character,
)
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
    print(wrap_random_colour_per_character("As you enter the room you notice a "))
    print(wrap_random_colour_per_character("h-h-hEllo friend... coMe closer I woUld like to geT a cLoser look at THOUTH formmMMM"), end=" ")
    print(wrap_random_colour_per_character("/'"), end=" ")
    answer = input(wrap_random_colour_per_character("PLEASE DO NOT BE AFRAID... I would like to ask a few questions to get to know you BETTER •ᴗ•"))
    time.sleep(1)
    clear()
    print(wrap_random_colour_per_character("What is your name?"))
    random.shuffle(challenges)
    

    for _ in range(3):  # Pick three challenges
        chal = challenges.pop()
        if not call_challenge(chal):
            return False

    return True

<<<<<<< HEAD
#TEST CODE
boss_room()
=======

# TEST CODE
# boss_room()
>>>>>>> 569bfc5c36c696e4afbe75b1b80a0ff5ba8b1f57
