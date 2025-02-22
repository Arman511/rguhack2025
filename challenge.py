import requests
from colours import ANSI_RED, wrap_colour, ANSI_BLUE, ANSI_GREEN, ANSI_YELLOW
from utils.wordle import wordle_response
# import pandas as pd
import random

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
    print(riddle)
    user_answer = input("What is your answer? ").strip().lower()
    if user_answer == answer:
        print(wrap_colour(ANSI_BLUE, "The laser turns off and the door unlocks"))
        return True
    else:
        print(wrap_colour(ANSI_RED, "The laser fires and you die"))
        return False


def hangman_challenge():
    pass


def wordle_challenge():
    # get the wordle data from utils/all_answers.csv and all_guess.csv
    with open("rguhack2025/utils/data/all_answers.csv") as f:
        answer_list = [line.strip() for line in f]

    with open("rguhack2025/utils/data/all_guess.csv") as f:
        guess_set = {line.strip() for line in f}

    # pick a random wordle answer
    answer = random.choice(answer_list)
    attempts_remaining = 6

    print(
        wrap_colour(
            ANSI_BLUE,
            "You enter the wordle chamber, a mystical voice echoes: 'Guess the secret word or face the consequences!'",
        )
    )

    for attempt in range(6):
        print(f"Guesses remaining: {attempts_remaining}")
        user_guess = input("Enter your guess: ").strip().lower()
        if user_guess not in guess_set:
            print(wrap_colour(ANSI_RED, "Invalid guess, try again"))
            continue
        response = wordle_response(answer, user_guess)
        for i, char in zip(response, user_guess):
            if i == "0":
                print(wrap_colour(ANSI_RED, char.upper()), end=" ")
            elif i == "1":
                print(wrap_colour(ANSI_YELLOW, char.upper()), end=" ")
            elif i == "2":
                print(wrap_colour(ANSI_GREEN, char.upper()), end=" ")
        print()
        if response == "22222":
            print(wrap_colour(ANSI_BLUE, "Success! The mystical voice booms: 'You have guessed the correct word.'"))
            return True
        attempts_remaining -= 1

    print(wrap_colour(ANSI_RED, "You failed. The mystical voice whispers: 'The correct answer was:'"), wrap_colour(ANSI_GREEN, answer.upper()))
    return False


def quick_maths_challenge():
    pass
