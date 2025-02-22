from player import Player


def main():
    print("Hello World!")

    username = ""
    while not username:
        username = input("Enter your username: ")
        username = username.strip()

    player = Player(username)
    print(player)


if __name__ == "__main__":
    main()
