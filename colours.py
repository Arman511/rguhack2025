import random


ANSI_RESET = "\u001b[0m"
ANSI_BLACK = "\u001b[1;30m"
ANSI_RED = "\u001b[1;31m"
ANSI_GREEN = "\u001b[1;32m"
ANSI_YELLOW = "\u001b[1;33m"
ANSI_BLUE = "\u001b[1;34m"
ANSI_PURPLE = "\u001b[1;35m"
ANSI_CYAN = "\u001b[1;36m"
ANSI_WHITE = "\u001b[37m"

ANSI_BG_BLACK = "\u001b[40m"
ANSI_BG_RED = "\u001b[41m"
ANSI_BG_GREEN = "\u001b[42m"
ANSI_BG_YELLOW = "\u001b[43m"
ANSI_BG_BLUE = "\u001b[44m"
ANSI_BG_PURPLE = "\u001b[45m"
ANSI_BG_CYAN = "\u001b[46m"
ANSI_BG_WHITE = "\u001b[47m"


def wrap_colour(colour, text):
    return colour + text + ANSI_RESET


# List of all colors
colors = [ANSI_RED, ANSI_BLUE, ANSI_PURPLE]


def wr(text):
    result = ""
    random_number = random.randint(1, 5)
    i = 0
    while i < len(text):
        random_number = random.randint(
            1, 5
        )  # Choose random length for each slice (1 or 2 or 3)
        random_colour = random.choice(colors)  # Select a random color
        result += random_colour + text[i: i + random_number] + ANSI_RESET
        i += random_number
    # for char in text:
    #     random_colour = random.choice(colors)  # Select a random color for each character
    #     result += random_colour + char + ANSI_RESET
    return result
