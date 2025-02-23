import random


ANSI_RESET = "\u001b[0m"
ANSI_BLACK = "\u001b[30m"
ANSI_RED = "\u001b[31m"
ANSI_GREEN = "\u001b[32m"
ANSI_YELLOW = "\u001b[33m"
ANSI_BLUE = "\u001b[34m"
ANSI_PURPLE = "\u001b[35m"
ANSI_CYAN = "\u001b[36m"
ANSI_WHITE = "\u001b[37m"


def wrap_colour(colour, text):
    return colour + text + ANSI_RESET

# List of all colors
colors = [ANSI_BLACK, ANSI_RED, ANSI_GREEN, ANSI_YELLOW, ANSI_BLUE, ANSI_PURPLE, ANSI_CYAN, ANSI_WHITE]

def wrap_random_colour_per_character(text):
    result = ""
    for char in text:
        random_colour = random.choice(colors)  # Select a random color for each character
        result += random_colour + char + ANSI_RESET
    return result
