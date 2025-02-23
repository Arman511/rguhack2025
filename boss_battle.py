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


def boss_room():
    print(wrap_random_colour_per_character("As you enter the room you notice"), end=" ")
    input("Press enter to continue...")
    random.shuffle(challenges)

    for _ in range(3):  # Pick three challenges
        chal = challenges.pop()
        if not call_challenge(chal):
            return False

    return True
