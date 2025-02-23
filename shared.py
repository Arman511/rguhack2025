

import os
import sys
import time


TEXT_SPEED = 0.02  # Typing effect speed


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
