
from colours import ANSI_RED, wrap_colour, ANSI_BLUE, ANSI_GREEN, ANSI_YELLOW
from utils.wordle import wordle_response
# import pandas as pd
import random
import time

with open("rguhack2025/utils/data/all_answers.csv") as f:
    ANSWER_LIST = [line.strip() for line in f]

with open("rguhack2025/utils/data/all_guess.csv") as f:
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
            quick_maths_challenge()
        case _:
            raise ValueError("Invalid challenge ID")


def console_challenge():
    pass


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
        "Why did the Microsoft Java developer need glasses?",
        "C#",
        ["C#", "Java", "Python", "Ruby"],
    ),
    Riddle(
        "I am a data structure that follows First-In-First-Out (FIFO). What am I?",
        "Queue",
        ["Stack", "Queue", "Heap", "Tree"],
    ),
    Riddle(
        "Which computer science term is also the name of a crime?",
        "Hacking",
        ["Phishing", "Hacking", "DDoS", "Brute Force"],
    ),
    Riddle(
        "I can store a lot of information, but I forget everything when the power is off. What am I?",
        "RAM",
        ["RAM", "SSD", "HDD", "Cache"],
    ),
    Riddle(
        "Which sorting algorithm repeatedly divides the list into smaller parts?",
        "Merge Sort",
        ["Bubble Sort", "Quick Sort", "Merge Sort", "Selection Sort"],
    ),
    Riddle(
        "Which programming language is named after a comedy group?",
        "Python",
        ["Java", "C++", "Python", "Ruby"],
    ),
    Riddle(
        "I translate high-level code into machine code. What am I?",
        "Compiler",
        ["Compiler", "Interpreter", "Assembler", "Debugger"],
    ),
    Riddle(
        "What does HTML stand for?",
        "HyperText Markup Language",
        [
            "HyperText Markup Language",
            "High Tech Machine Learning",
            "HyperText Management Language",
            "HyperTransfer Markup Language",
        ],
    ),
    Riddle(
        "Which programming language is used for developing Android apps?",
        "Java",
        ["C#", "Python", "Java", "Swift"],
    ),
    Riddle(
        "Which is faster: O(1) or O(n)?",
        "O(1)",
        ["O(1)", "O(n)", "O(n^2)", "O(log n)"],
    ),
    Riddle(
        "Which HTTP status code represents 'Not Found'?",
        "404",
        ["200", "403", "404", "500"],
    ),
    Riddle(
        "I am the father of the C programming language. Who am I?",
        "Dennis Ritchie",
        ["Dennis Ritchie", "James Gosling", "Bjarne Stroustrup", "Guido van Rossum"],
    ),
    Riddle(
        "Which symbol is commonly used to indicate a pointer in C?",
        "*",
        ["*", "&", "->", "#"],
    ),
    Riddle(
        "What does SQL stand for?",
        "Structured Query Language",
        [
            "Structured Query Language",
            "Simple Query Logic",
            "Standard Query Layout",
            "System Query Language",
        ],
    ),
    Riddle(
        "I am a loop that never stops. What am I called?",
        "Infinite Loop",
        ["Infinite Loop", "For Loop", "While Loop", "Recursion"],
    ),
    Riddle(
        "Which Boolean operator returns True if both inputs are True?",
        "AND",
        ["AND", "OR", "XOR", "NOT"],
    ),
    Riddle(
        "Which data structure works based on Last-In-First-Out (LIFO)?",
        "Stack",
        ["Queue", "Stack", "Heap", "Graph"],
    ),
    Riddle(
        "Which protocol is used to send emails?",
        "SMTP",
        ["HTTP", "FTP", "SMTP", "IMAP"],
    ),
    Riddle(
        "Which company created the Java programming language?",
        "Sun Microsystems",
        ["Sun Microsystems", "Microsoft", "Google", "Apple"],
    ),
    Riddle(
        "Which programming language is known for its indentation-based syntax?",
        "Python",
        ["Python", "Java", "C++", "Swift"],
    ),
    Riddle(
        "Which algorithm is used to find the shortest path in a graph?",
        "Dijkstra’s Algorithm",
        [
            "Dijkstra’s Algorithm",
            "Binary Search",
            "Depth-First Search",
            "Prim’s Algorithm",
        ],
    ),
    Riddle(
        "Which logic gate returns True only if both inputs are different?",
        "XOR",
        ["AND", "OR", "NAND", "XOR"],
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
    print(wrap_colour(ANSI_RED, "The laser fires and you die"))
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
            print(wrap_colour(ANSI_BLUE, "You survived! The noose disappears and the door unlocks."))
            return True
        guess = input(wrap_colour(ANSI_YELLOW, "Guess a letter: ")).upper()
        if guess in secret:
            guessed.add(guess)
        else:
            mistakes += 1

    print(wrap_colour(ANSI_RED, stages[mistakes]))
    print(wrap_colour(ANSI_RED, "Word: " + secret))
    print(wrap_colour(ANSI_RED, "You got hanged! The noose tightens and everything goes dark."))
    return False



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
    operations = ['+', '-', '*']
    num_questions = 5
    time_limit = 5  # seconds

    print(wrap_colour(ANSI_BLUE, "You step into the chamber of quick maths. A booming voice declares: 'Solve these problems swiftly, or face the wrath of the ancient guardians!'"))

    for _ in range(num_questions):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        operation = random.choice(operations)
        
        if operation == '*':
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)
        
        question = f"{num1} {operation} {num2}"
        answer = eval(question)

        print(wrap_colour(ANSI_YELLOW, f"Solve: {question}"))
        start_time = time.time()
        user_answer = input("Your answer: ").strip()
        end_time = time.time()

        if end_time - start_time > time_limit:
            print(wrap_colour(ANSI_RED, "Time's up! The guardians awaken and you are engulfed in darkness."))
            return False

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(wrap_colour(ANSI_RED, "Invalid input! The guardians are displeased."))
            return False

        if user_answer != answer:
            print(wrap_colour(ANSI_RED, "Wrong answer! The ground trembles as the guardians stir."))
            return False

    print(wrap_colour(ANSI_BLUE, "Congratulations! You have appeased the guardians with your swift and accurate calculations. The path ahead is clear."))
    return True
