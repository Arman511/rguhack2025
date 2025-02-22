import requests
from client import key_not_in_room
from colours import wrap_colour, ANSI_BLUE


def challenge(challenge_id):
    match challenge_id:
        case 3:
            console_challenge()
        case 4:
            riddle_challenge()
        case 5:
            hangman_challenge()
        case 6:
            quick_maths_challenge()
        case _:
            raise ValueError("Invalid challenge ID")


def console_challenge():
    pass


def riddle_challenge():
    request = requests.get("https://riddles-api-eight.vercel.app/science")
    data = request.json()
    riddle = data["riddle"]
    answer = data["answer"].lower()
    print(
        wrap_colour(
            ANSI_BLUE,
            "You enter the riddle room, there is machine displaying a riddle, with  a laser pointing at your head, you hear the door lock behind you",
        )
    )
