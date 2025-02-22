from colours import (
    wrap_colour,
    ANSI_RED,
    # ANSI_RESET,
    # ANSI_BLACK,
    # ANSI_GREEN,
    # ANSI_YELLOW,
    # ANSI_BLUE,
    # ANSI_PURPLE,
    # ANSI_CYAN,
    # ANSI_WHITE,
)

from player import Player

player = None


def main():
    print(wrap_colour(ANSI_RED, "MISSION: FIX OIL RIG"))

    username = ""
    global player
    while not username:
        username = input("Enter your username: ")
        username = username.strip()

    player = Player(username)
    print(player)
    print(player.inventory)


if __name__ == "__main__":
    main()
