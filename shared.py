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
        time.sleep(speed)
    print(end, flush=True)


def typewriter_rtl(text, speed=TEXT_SPEED, end="\n"):
    """Prints text with a typewriter effect, right-aligned."""
    terminal_width = os.get_terminal_size().columns
    padding = terminal_width - len(text)
    formatted_text = " " * max(padding, 0) + text

    for char in formatted_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != " ":
            time.sleep(speed)
    print(end, flush=True)
