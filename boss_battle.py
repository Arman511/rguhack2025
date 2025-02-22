import random
from player import Player
from colours import wrap_colour, ANSI_RED, ANSI_PURPLE
from challenge import (
    console_challenge,
    riddle_challenge,
    wordle_challenge,
    hangman_challenge,
    cipher_challenge,
)


challenges = [
    console_challenge,
    riddle_challenge,
    wordle_challenge,
    hangman_challenge,
    cipher_challenge,
]


def boss_room(player: Player):
    print(wrap_colour(ANSI_PURPLE, "As you enter the room you notice"))
    random.shuffle(challenges)

    chal1 = challenges.pop()

    pass
