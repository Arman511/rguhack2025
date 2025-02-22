from colours import ANSI_RED, wrap_colour, ANSI_BLUE, ANSI_GREEN, ANSI_YELLOW
from utils.wordle import wordle_response

# import pandas as pd
import random
import time

with open("utils/data/all_answers.csv") as f:
    ANSWER_LIST = [line.strip() for line in f]

with open("utils/data/all_guess.csv") as f:
    GUESS_SET = {line.strip() for line in f}


def challenge(challenge_id):
    match challenge_id:
        case 3:
            console_challenge()
        case 4:
            riddle_challenge()
        case 5:
            hangman_challenge()
        case 6:
            wordle_challenge()
        case _:
            raise ValueError("Invalid challenge ID")


def console_challenge():
    operations = ["+", "-", "*"]
    num_questions = 3
    time_limit = 5  # seconds

    print(
        wrap_colour(
            ANSI_BLUE,
            "You step into the chamber of quick maths. A booming voice declares: 'Solve these problems swiftly, or face the wrath of the ancient guardians!'",
        )
    )

    for _ in range(num_questions):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        operation = random.choice(operations)

        if operation == "*":
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)

        question = f"{num1} {operation} {num2}"
        answer = eval(question)

        print(wrap_colour(ANSI_YELLOW, f"Solve: {question}"))
        start_time = time.time()
        user_answer = input("Your answer: ").strip()
        end_time = time.time()

        if end_time - start_time > time_limit:
            print(
                wrap_colour(
                    ANSI_RED,
                    "Time's up! The guardians awaken and you are engulfed in darkness.",
                )
            )
            return False

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(wrap_colour(ANSI_RED, "Invalid input! The guardians are displeased."))
            return False

        if user_answer != answer:
            print(
                wrap_colour(
                    ANSI_RED, "Wrong answer! The ground trembles as the guardians stir."
                )
            )
            return False

    print(
        wrap_colour(
            ANSI_BLUE,
            "Congratulations! You have appeased the guardians with your swift and accurate calculations. The path ahead is clear.",
        )
    )
    return True


class Riddle:
    riddle: str = ""
    answer: str = ""
    options: list[str] = []

    def __init__(self, riddle: str, answers: str, options: list[str]):
        self.riddle = riddle
        self.answers = answers
        self.options = options


riddles = [
    Riddle(
        "I have keys but open no locks. I have space but no room. You can enter, but you can’t go outside. What am I?",
        "Keyboard",
        ["Keyboard", "Safe", "Puzzle Box", "Server"],
    ),
    Riddle(
        "The more you take from me, the bigger I become. What am I?",
        "Memory Leak",
        ["Memory Leak", "Hard Drive", "Database", "Cache"],
    ),
    Riddle(
        "I can be solid, liquid, or gas, but I’m not a state of matter. In tech, I can crash, but I’m not a car. What am I?",
        "Cloud",
        ["Cloud", "RAM", "Binary", "Algorithm"],
    ),
    Riddle(
        "I speak without a mouth, but I am heard. I am stored, but I take up no space. What am I?",
        "Data",
        ["Data", "Echo", "Soundwave", "Electricity"],
    ),
    Riddle(
        "I can be inserted but never removed. I grow but never shrink. What am I?",
        "Blockchain",
        ["Blockchain", "USB Drive", "Memory Stick", "Log File"],
    ),
    Riddle(
        "I follow you everywhere on the internet, yet I leave no footprints. What am I?",
        "Cookie",
        ["Cookie", "VPN", "IP Address", "Incognito Mode"],
    ),
    Riddle(
        "I have an eye but cannot see. I help store memories but have no mind. What am I?",
        "Camera",
        ["Camera", "RAM", "Hard Drive", "Sensor"],
    ),
    Riddle(
        "You can fill me with numbers, words, or even colors, but I always have rows and columns. What am I?",
        "Spreadsheet",
        ["Spreadsheet", "Database", "Chart", "Code Editor"],
    ),
    Riddle(
        "I start at zero and count up, but only as long as you need me. What am I?",
        "Loop",
        ["Loop", "Index", "Counter", "Function"],
    ),
    Riddle(
        "I get shorter as I grow older, but I’m not alive. What am I?",
        "Battery",
        ["Battery", "Timer", "Cache", "Stack"],
    ),
    Riddle(
        "I come in packets, but I’m not food. I travel fast, but I have no legs. What am I?",
        "Data",
        ["Data", "Email", "Electricity", "VPN"],
    ),
    Riddle(
        "I disappear the moment you say my name. What am I?",
        "Silence",
        ["Silence", "Bug", "Echo", "Error"],
    ),
    Riddle(
        "I connect billions of people, yet I am invisible. What am I?",
        "Internet",
        ["Internet", "Wi-Fi", "Bluetooth", "Satellite"],
    ),
    Riddle(
        "I can be high or low, but I always come in bits. What am I?",
        "Bandwidth",
        ["Bandwidth", "Bitrate", "Resolution", "Signal Strength"],
    ),
    Riddle(
        "I can be found in phones, cars, and even fridges. I help things run, but I don’t have legs. What am I?",
        "Operating System",
        ["Operating System", "AI", "Processor", "Battery"],
    ),
    Riddle(
        "I can have bugs but not be alive. I can be updated but never grow. What am I?",
        "Software",
        ["Software", "Code", "App", "Hardware"],
    ),
    Riddle(
        "I may have a spine but no bones. You can read me, but I have no voice. What am I?",
        "Book",
        ["Book", "Server Rack", "Database", "Archive"],
    ),
    Riddle(
        "I am used to make calls but have no voice. I can crash but not break. What am I?",
        "App",
        ["App", "Phone", "VoIP", "Signal"],
    ),
    Riddle(
        "I travel the world while staying in one spot. What am I?",
        "Website",
        ["Website", "Wi-Fi Router", "Satellite", "Email"],
    ),
    Riddle(
        "I have windows but no glass. I sometimes crash but I’m not a car. What am I?",
        "Operating System",
        ["Operating System", "Browser", "Monitor", "Server"],
    ),
    Riddle(
        "I can be physical or virtual, but I always help you get from one place to another. What am I?",
        "Router",
        ["Router", "Map", "Cable", "Server"],
    ),
    Riddle(
        "I store knowledge, but I’m not a library. I can be searched, but I’m not the internet. What am I?",
        "Database",
        ["Database", "Cloud", "Hard Drive", "Dictionary"],
    ),
    Riddle(
        "I go up, but I never come down. In tech, people always want me higher. What am I?",
        "Uptime",
        ["Uptime", "Bandwidth", "Ping", "Stock Price"],
    ),
    Riddle(
        "I can be found in games and code, but I am not alive. I’m something developers try to remove. What am I?",
        "Bug",
        ["Bug", "Glitch", "Easter Egg", "Patch"],
    ),
    Riddle(
        "I travel at the speed of light but can be stopped by walls. What am I?",
        "Wi-Fi",
        ["Wi-Fi", "Fiber Optics", "Bluetooth", "Electricity"],
    ),
    Riddle(
        "I exist in ones and zeros, but I can create entire worlds. What am I?",
        "Binary Code",
        ["Binary Code", "AI", "Algorithm", "Quantum Computer"],
    ),
    Riddle(
        "I can be moved forward, backward, or deleted, but I never physically exist. What am I?",
        "Cursor",
        ["Cursor", "File", "Process", "Memory"],
    ),
    Riddle(
        "I can be phishing but never in the water. I can be spam but never eaten. What am I?",
        "Cyber Attack",
        ["Cyber Attack", "Hacker", "Firewall", "Trojan"],
    ),
    Riddle(
        "I get weaker the farther I travel, but I carry information everywhere. What am I?",
        "Signal",
        ["Signal", "Battery", "Sound Wave", "Ping"],
    ),
    Riddle(
        "You can hear me but never see me. I can be a phone, a speaker, or a notification. What am I?",
        "Sound",
        ["Sound", "Radio", "Mic", "Alarm"],
    ),
    Riddle(
        "I always listen but never speak. I can wake up when you call my name. What am I?",
        "Smart Assistant",
        ["Smart Assistant", "Microphone", "Server", "AI"],
    ),
    Riddle(
        "I can control many devices but have no physical form. I help turn things on but can’t hold anything. What am I?",
        "Remote Control",
        ["Remote Control", "Bluetooth", "Wi-Fi", "Cloud"],
    ),
    Riddle(
        "I have a head and a tail but no body. What am I?",
        "Coin",
        ["Coin", "Bit", "Pointer", "Queue"],
    ),
    Riddle(
        "I can crash, but I am not a plane. I can freeze, but I am not ice. What am I?",
        "Computer",
        ["Computer", "Software", "Server", "Game"],
    ),
    Riddle(
        "I help you reach new places, but I don’t move. I make connections but have no emotions. What am I?",
        "Network",
        ["Network", "Browser", "Cable", "AI"],
    ),
]


def riddle_challenge():
    riddle = random.choice(riddles)
    print(
        wrap_colour(
            ANSI_BLUE,
            "You enter the riddle room, there is machine displaying a riddle, with  a laser pointing at your head, you hear the door lock behind you",
        )
    )
    print(riddle.riddle)
    print("Options")
    shuffled = riddle.options[:]
    random.shuffle(shuffled)
    for i, option in enumerate(shuffled):
        print(f"{i} - {option}")
    ans = -1
    while ans < 0 or ans > len(shuffled) - 1:
        ans = input("Enter option: ").strip()
        try:
            ans = int(ans)
        except Exception:
            print(wrap_colour(ANSI_RED, "INVALID INPUT"))
            ans = -1
            continue
        if ans < 0 or ans > len(shuffled) - 1:
            print(wrap_colour(ANSI_RED, "INVALID INPUT"))
            ans = -1
            continue

    if riddle.answer == shuffled[ans]:
        print(wrap_colour(ANSI_BLUE, "The laser turns off and the door unlocks"))
        return True
    print(wrap_colour(ANSI_RED, "The laser fires..."))
    return False


def hangman_challenge():
    stages = [
        """
            +---+
            |   |
                |
                |
                |
                |
            =========
        """,
        """
            +---+
            |   |
            O   |
                |
                |
                |
            =========
        """,
        """
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
        """,
        """
            +---+
            |   |
            O   |
            /|   |
                |
                |
            =========
        """,
        """
            +---+
            |   |
            O   |
            /|\\  |
                |
                |
            =========
        """,
        """
            +---+
            |   |
            O   |
            /|\\  |
            /    |
                |
            =========
        """,
        """
            +---+
            |   |
            O   |
            /|\\  |
            / \\  |
                |
            =========
        """,
    ]

    secret = random.choice(ANSWER_LIST).upper()
    guessed = set()
    mistakes = 0

    print(
        wrap_colour(
            ANSI_BLUE,
            "You find yourself in a dark room with a noose hanging from the ceiling. A voice echoes: 'Guess the word or face the gallows!'",
        )
    )

    while mistakes < len(stages) - 1:
        display = [c if c in guessed else "_" for c in secret]
        print(wrap_colour(ANSI_YELLOW, stages[mistakes]))
        print(wrap_colour(ANSI_GREEN, "Word: " + " ".join(display)))
        if "_" not in display:
            print(
                wrap_colour(
                    ANSI_BLUE,
                    "You survived! The noose disappears and the door unlocks.",
                )
            )
            return True
        guess = input(wrap_colour(ANSI_YELLOW, "Guess a letter: ")).upper()
        if guess in secret:
            guessed.add(guess)
        else:
            mistakes += 1

    print(wrap_colour(ANSI_RED, stages[mistakes]))
    print(wrap_colour(ANSI_RED, "Word: " + secret))
    print(
        wrap_colour(
            ANSI_RED, "You got hanged! The noose tightens and everything goes dark."
        )
    )
    return False


def wordle_challenge():

    # pick a random wordle answer
    answer = random.choice(ANSWER_LIST)
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
        if user_guess not in GUESS_SET:
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
            print(
                wrap_colour(
                    ANSI_BLUE,
                    "Success! The mystical voice booms: 'You have guessed the correct word.'",
                )
            )
            return True
        attempts_remaining -= 1

    print(
        wrap_colour(
            ANSI_RED,
            "You failed. The mystical voice whispers: 'The correct answer was:'",
        ),
        wrap_colour(ANSI_GREEN, answer.upper()),
    )
    return False
