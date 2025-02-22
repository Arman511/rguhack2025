import random
from colours import ANSI_RED, wrap_colour, ANSI_BLUE


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
    riddles = [("Why did the microsoft java dev need glasses", "C#"), ("", [])]
    riddle = random.choice(riddles)
    riddle = riddle[0]
    answer = riddle[1]
    print(
        wrap_colour(
            ANSI_BLUE,
            "You enter the riddle room, there is machine displaying a riddle, with  a laser pointing at your head, you hear the door lock behind you",
        )
    )
    print(riddle)
    user_answer = input("What is your answer? ").strip().lower()
    if user_answer == answer or user_answer in answer:
        print(wrap_colour(ANSI_BLUE, "The laser turns off and the door unlocks"))
        return True
    else:
        print(wrap_colour(ANSI_RED, "The laser fires and you die"))
        return False


def hangman_challenge():
    pass


def quick_maths_challenge():
    pass
