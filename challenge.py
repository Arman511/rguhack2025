import pygame
from colours import (
    ANSI_RED,
    wrap_colour,
    ANSI_BLUE,
    ANSI_GREEN,
    ANSI_YELLOW,
    ANSI_PURPLE,
)
from utils.wordle import wordle_response
from player import Player
import base64

# import pandas as pd
import random
import time

from shared import clear

# with open("utils/data/all_answers.csv") as f:
#     ANSWER_LIST = [line.strip() for line in f]
ANSWER_LIST = [
    "ocean",
]

with open("utils/data/all_guess.csv") as f:
    GUESS_SET = {line.strip() for line in f}

EVENT_CHANCES = {"type_fast": 0.4, "cat": 0.1, "dog": 0.1, "eldritch": 0.1}
ITEM_DROP = {"meat": 0.1, "Einstein's Dream": 0.05}


def item_draw(player: Player):
    print()
    items = list(ITEM_DROP.keys())
    probabilities = list(ITEM_DROP.values())
    probabilities.append(1 - sum(probabilities))  # probability for no item
    items.append("")  # no item

    chosen_item = random.choices(items, probabilities)[0]

    if chosen_item:
        if chosen_item == "meat":
            player.add_item_to_inventory(chosen_item)
            print(
                wrap_colour(
                    ANSI_GREEN,
                    f"You found a {chosen_item}! It has been added to your inventory.",
                )
            )
        elif chosen_item == "Einstein's Dream":
            print(
                wrap_colour(
                    ANSI_BLUE,
                    "You have an epiphany, you feel a surge of speed (+2s bonus time).",
                )
            )
            player.bonus_time += 1


def random_event(player: Player):
    print()
    events = list(EVENT_CHANCES.keys())
    events.append("nothing")
    probabilities = list(EVENT_CHANCES.values())
    probabilities.append(1 - (sum(probabilities)))  # nothing probability
    # print(events, probabilities)
    chosen_event = random.choices(events, probabilities)[0]
    if chosen_event == "nothing":
        return
    elif chosen_event == "type_fast":
        type_fast_event(player)
    elif chosen_event == "cat":
        cat_event(player)
    elif chosen_event == "dog":
        dog_event(player)
    elif chosen_event == "eldritch":
        eldritch_event(player)
    else:
        print(wrap_colour(ANSI_RED, "Error: Unknown event."))

    input("Press enter to continue...")
    clear()


def challenge(challenge_id, player: Player):
    match challenge_id:
        case 3:
            return console_challenge(player)
        case 4:
            return riddle_challenge(player)
        case 5:
            return hangman_challenge(player)
        case 6:
            return wordle_challenge(player)
        case _:
            raise ValueError("Invalid challenge ID")


def console_challenge(player: Player):
    operations = ["+", "-", "*"]
    num_questions = 3
    time_limit = 10 + player.bonus_time  # seconds

    print(
        wrap_colour(
            ANSI_BLUE,
            "You step into the chamber of quick maths. A booming voice declares: 'Solve these problems swiftly, or face the wrath of the ancient guardians!'",
        )
    )

    time.sleep(3)
    clear()

    for _ in range(num_questions):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        operation = random.choice(operations)

        if operation == "*":
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)

        question = f"{num1} {operation} {num2}"
        answer = eval(question)
        pygame.mixer.Sound("music/speed_timer_10s.mp3").play()
        print(wrap_colour(ANSI_YELLOW, f"Solve: {question}"))
        start_time = time.time()
        user_answer = input(
            "Your answer(type exit to return to the corridor): "
        ).strip()
        if user_answer.lower() == "exit":
            return "EXIT"
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
            user_answer_int = int(user_answer)
        except ValueError:
            print(wrap_colour(ANSI_RED, "Invalid input! The guardians are displeased."))
            return False

        if user_answer_int != answer:
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

    def __init__(self, riddle: str, answer: str, options: list[str]):
        self.riddle = riddle
        self.answer = answer
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


def riddle_challenge(player: Player, can_exit=True):
    riddle = random.choice(riddles)
    print(
        wrap_colour(
            ANSI_BLUE,
            "You enter the riddle room, there is machine displaying a riddle with a chest thats locked, with a laser pointing at your head",
        )
    )
    if can_exit:
        print(wrap_colour(ANSI_GREEN, "TYPE EXIT TO BACK TO CORRIDOR"))
    print(riddle.riddle)
    print("Options")
    shuffled = riddle.options[:]
    random.shuffle(shuffled)
    for i, option in enumerate(shuffled):
        print(f"{i} - {option}")
    ans = -1
    while ans < 0 or ans > len(shuffled) - 1:
        ans_text = input("Enter option: ").strip()
        if ans_text.lower() == "exit" and can_exit:
            return "EXIT"
        try:
            ans = int(ans_text)
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


def hangman_challenge(player: Player, can_exit=True, is_boss_event=False):
    from room_manager import OIL_RIG_HANGMAN_ROOM

    if not is_boss_event:
        # you find a dead body on the gallows add meat to inventory
        player.add_item_to_inventory("meat")
        print(
            wrap_colour(
                ANSI_GREEN,
                "You find a dead body hanging from the gallows. 'Free meat' you think to yourself.",
            ),
            wrap_colour(ANSI_BLUE, "(Meat has been added to your inventory)"),
        )
    room = OIL_RIG_HANGMAN_ROOM
    stages = [
        """
                
                
                
                
                
                
          =========
        """,
        """
                |
                |
                |
                |
                |
                |
          =========
        """,
        """
                +
                |
                |
                |
                |
                |
          =========
        """,
        """
            +---+
                |
                |
                |
                |
                |
          =========
        """,
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
        """
            +---+
            |   |
           [O]  |
           /|\\  |
           / \\  |
                |
          =========
        """,
        """
            +---+
            |   |
           [O]  |
          _/|\\  |
           / \\  |
                |
          =========
        """,
        """
            +---+
            |   |
           [O]  |
          _/|\\_ |
           / \\  |
                |
          =========
        """,
    ]

    secret = random.choice(ANSWER_LIST).upper()
    guessed = set()
    mistakes = 0
    mistakes_list: list[str] = []

    print(
        wrap_colour(
            ANSI_BLUE,
            "You find yourself in a dark room with a noose hanging from the ceiling. A voice echoes: 'Guess the word or face the gallows!'",
        )
    )
    input()
    while mistakes < len(stages) - 1:
        clear()
        print("Current room:", wrap_colour(ANSI_RED, room.name))
        print(room.description)
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
        print(wrap_colour(ANSI_YELLOW, "Mistakes: " + " ".join(mistakes_list)))
        guess = input(
            wrap_colour(ANSI_YELLOW, "Guess a letter(Press exit to exit): ")
        ).upper()
        if guess.lower() == "exit" and can_exit:
            return "EXIT"
        if len(guess) != 1 or not guess.isalpha():
            print(wrap_colour(ANSI_RED, "Invalid guess, try again"))
            continue
        if guess in guessed or guess in mistakes_list:
            print(wrap_colour(ANSI_RED, f"You already guessed {guess}"))
            continue
        if guess in secret:
            guessed.add(guess)
        else:
            mistakes += 1
            mistakes_list.append(guess)

    print(wrap_colour(ANSI_RED, stages[mistakes]))
    print(wrap_colour(ANSI_RED, "Word: " + secret))
    print(
        wrap_colour(
            ANSI_RED, "You got hanged! The noose tightens and everything goes dark."
        )
    )
    return False


def wordle_challenge(player: Player, can_exit=True):
    # pick a random wordle answer
    from client import clear
    from room_manager import OIL_RIG_WORDLE_ROOM

    room = OIL_RIG_WORDLE_ROOM
    answer = random.choice(ANSWER_LIST)
    attempts_remaining = 6
    clear()
    print("Current room:", wrap_colour(ANSI_RED, room.name))
    print(room.description)
    print(
        wrap_colour(
            ANSI_BLUE,
            "You enter the wordle chamber, a mystical voice echoes: 'Guess the secret word or face the consequences!'",
        )
    )
    user_words: list[str] = []

    for attempt in range(6):
        if user_words:
            print(wrap_colour(ANSI_YELLOW, "Previous guesses:"))
        for word in user_words[:-1]:
            print(word)
        print(f"Guesses remaining: {attempts_remaining}")
        if can_exit:
            user_guess = (
                input("Enter your guess(type exit to return to the corridor): ")
                .strip()
                .lower()
            )
        else:
            user_guess = input("Enter your guess: ").strip().lower()
        clear()
        if not user_guess:
            print(wrap_colour(ANSI_RED, "Invalid guess, try again"))
            attempt -= 1
            continue
        if user_guess == "exit" and can_exit:
            return "EXIT"
        if user_guess not in GUESS_SET:
            print(wrap_colour(ANSI_RED, "Invalid guess, try again"))
            continue
        response = wordle_response(answer, user_guess)
        print("Result: ", end="")
        ans = ""
        for i, char in zip(response, user_guess):
            if i == "0":
                ans += wrap_colour(ANSI_RED, char.upper()) + " "
                print(wrap_colour(ANSI_RED, char.upper()), end=" ")
            elif i == "1":
                ans += wrap_colour(ANSI_YELLOW, char.upper()) + " "
                print(wrap_colour(ANSI_YELLOW, char.upper()), end=" ")
            elif i == "2":
                ans += wrap_colour(ANSI_GREEN, char.upper()) + " "
                print(wrap_colour(ANSI_GREEN, char.upper()), end=" ")
        print()
        user_words.append(ans)
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


def type_fast_event(player: Player):
    actions = ["duck", "hide", "hit", "jump", "guard"]
    action_dialogues = {
        "duck": {
            "problem": f"{wrap_colour(ANSI_BLUE, 'Arrows whiz overhead! Type')} '{wrap_colour(ANSI_PURPLE, 'duck')}' {wrap_colour(ANSI_BLUE, 'to avoid them!')}",
            "success": "You duck just in time, and the arrows harmlessly pass above you!",
            "failure": "You tried to {action}, but an arrow pierces you because you needed to duck!",
        },
        "hide": {
            "problem": f"{wrap_colour(ANSI_BLUE, 'A patrol is closing in! Type')} '{wrap_colour(ANSI_PURPLE, 'hide')}' {wrap_colour(ANSI_BLUE, 'to stay unseen!')}",
            "success": "You melt into the shadows, escaping their notice!",
            "failure": "You tried to {action}, but you're spotted because you needed to hide!",
        },
        "hit": {
            "problem": f"{wrap_colour(ANSI_BLUE, 'A goblin rushes at you! Type')} '{wrap_colour(ANSI_PURPLE, 'hit')}' {wrap_colour(ANSI_BLUE, 'to strike first!')}",
            "success": "You land a swift blow and the goblin collapses!",
            "failure": "You tried to {action}, but the goblin lands a hit on you first!",
        },
        "jump": {
            "problem": f"{wrap_colour(ANSI_BLUE, 'The ground crumbles beneath you! Type')} '{wrap_colour(ANSI_PURPLE, 'jump')}' {wrap_colour(ANSI_BLUE, 'to leap to safety!')}",
            "success": "You jump just in time and avoid the collapsing floor!",
            "failure": "You tried to {action}, but you plunge down because you needed to jump!",
        },
        "guard": {
            "problem": f"{wrap_colour(ANSI_BLUE, 'An arrow speeds your way! Type')} '{wrap_colour(ANSI_PURPLE, 'guard')}' {wrap_colour(ANSI_BLUE, 'to defend!')}",
            "success": "You raise your shield in the nick of time, deflecting the arrow!",
            "failure": "You tried to {action}, leaving you wide open! The arrow strikes you down!",
        },
    }
    time_limit = 10 + player.bonus_time  # seconds
    chosen_action = random.choice(actions)
    print(wrap_colour(ANSI_BLUE, action_dialogues[chosen_action]["problem"]))

    pygame.mixer.Sound("music/speed_timer_10s.mp3").play()
    start_time = time.time()
    user_action = input("Your action: ").strip().lower()
    end_time = time.time()

    if end_time - start_time > time_limit:
        print(
            wrap_colour(ANSI_RED, "Too slow! You fail to react, and disaster strikes.")
        )
        player.player_minus_health()
    elif user_action == chosen_action:
        print(wrap_colour(ANSI_BLUE, action_dialogues[chosen_action]["success"]))
    else:
        print(
            wrap_colour(
                ANSI_RED,
                action_dialogues[chosen_action]["failure"].format(action=user_action),
            )
        )
        player.player_minus_health()


def cat_event(player: Player):
    print(
        wrap_colour(
            ANSI_BLUE, "A small cat appears, meowing softly. Will you pet the cat?"
        )
    )
    choice = input("Pet the cat? (yes/no/exit): ").lower().strip()
    if choice == "exit":
        return "EXIT"
    elif choice == "yes":
        player.health += 1
        print(
            wrap_colour(
                ANSI_GREEN,
                "You pet the cat, it purrs contentedly, and you feel slightly healthier (+1 health).",
            )
        )
    else:
        print(wrap_colour(ANSI_RED, "The cat scampers away, leaving you as you were."))


def dog_event(player: Player):
    print(
        wrap_colour(
            ANSI_BLUE, "A large dog appears, growling softly. Will you pet the dog?"
        )
    )
    choice = input("Pet the dog? (yes/no/exit): ").lower().strip()
    if choice == "exit":
        return "EXIT"
    elif choice == "yes":
        if "meat" in [item.lower() for item in player.inventory]:
            player.remove_item_from_inventory("meat")
            player.health += 2
            print(
                wrap_colour(
                    ANSI_GREEN,
                    "You offer the dog some meat, it wags its tail happily, and you feel much healthier (+2 health).",
                )
            )
        else:
            player.player_minus_health()
            print(
                wrap_colour(
                    ANSI_RED,
                    "The dog bites you as you have no meat to offer (-1 health).",
                )
            )
    else:
        print(
            wrap_colour(ANSI_RED, "The dog growls and leaves, leaving you as you were.")
        )
    return True


def eldritch_event(player: Player):
    # eldritch horror man stuck in the wall RPG diaglogue
    print(
        wrap_colour(
            ANSI_BLUE,
            "You find yourself in a dimly lit chamber, the walls are covered in strange runes and symbols. A figure appears before you, its form shifting and writhing as if it were made of shadows and mist.",
        )
    )
    print(
        wrap_colour(
            ANSI_RED,
            "The fates control all. As will I. Shall we see what yours beholds?",
        )
    )
    print(wrap_colour(ANSI_BLUE, "The figure offers you a choice: 'Heads or Tails?'"))
    while True:
        choice = input("Choose heads or tails: ").strip().lower()
        if choice in ["heads", "tails"]:
            break
        print(wrap_colour(ANSI_RED, "Invalid choice! The figure frowns."))

    flip_result = random.choice(["heads", "tails"])
    print(wrap_colour(ANSI_YELLOW, f"The coin flips... It lands on {flip_result}."))

    if choice == flip_result:
        print(
            wrap_colour(
                ANSI_GREEN,
                "The figure nods slowly, and the shadows around it begin to dissipate. 'You have chosen wisely. The Fates have taken liking to you. (You double your health)'",
            )
        )
        player.health *= 2
        return
    else:
        print(
            wrap_colour(
                ANSI_RED,
                "The figure's eyes glow with a malevolent light. 'You are a pathetic worm. Suffer your puny existence. (Your health is halved)'",
            )
        )
        result = player.health // 2
        if result < 1:
            player.health = 1
        else:
            player.health = result
        player.player_minus_health(damage=0)
        return


def base64_cipher(text):
    encoded = base64.b64encode(text.encode()).decode()
    return encoded


def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result


def binary_cipher(text):
    return " ".join(format(ord(char), "08b") for char in text)


def morse_cipher(text):
    morse_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/",
    }
    return " ".join(morse_dict[char] for char in text.upper() if char in morse_dict)


def cipher_challenge(player: Player, can_exit=False):
    ciphers = ["Base64", "Caesar Shift", "Binary", "Morse Code"]
    chosen_cipher = random.choice(ciphers)
    message = random.choice(ANSWER_LIST)
    encoded_message = ""
    print(
        wrap_colour(
            ANSI_BLUE,
            "You step into a dimly lit chamber. Runes cover the walls, and a glowing inscription appears before you: 'Decipher the code to proceed!'",
        )
    )

    if chosen_cipher == "Base64":
        encoded_message = base64_cipher(message)
        print(
            wrap_colour(
                ANSI_GREEN, f"The inscription is encoded in Base64: {encoded_message}"
            )
        )
    elif chosen_cipher == "Caesar Shift":
        encoded_message = caesar_cipher(message)
        print(
            wrap_colour(
                ANSI_GREEN,
                f"The inscription is written in a shifted alphabet: {encoded_message}",
            )
        )
    elif chosen_cipher == "Binary":
        encoded_message = binary_cipher(message)
        print(
            wrap_colour(
                ANSI_GREEN,
                f"The inscription consists of only 0s and 1s: {encoded_message}",
            )
        )
    elif chosen_cipher == "Morse Code":
        encoded_message = morse_cipher(message)
        print(
            wrap_colour(
                ANSI_GREEN, f"Dots and dashes form the inscription: {encoded_message}"
            )
        )
    if can_exit:
        print(
            wrap_colour(
                ANSI_YELLOW, "Can you decode the message in time(type exit to exit)?"
            )
        )
    else:
        print(wrap_colour(ANSI_YELLOW, "Can you decode the message in time?"))

    answer = input("Enter the decoded message: ").strip()
    if answer.lower() == "exit" and can_exit:
        return "EXIT"
    if answer == message:
        print(
            wrap_colour(
                ANSI_BLUE,
                "The runes glow brightly, and the chamber door opens before you.",
            )
        )
        return True

    print(
        wrap_colour(
            ANSI_RED,
            "The runes flicker and fade, and the walls enclode",
        )
    )
    return False
