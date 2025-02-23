from room import Room

SUMBARINE_MAIN_ROOM = Room(
    "Submarine",
    "You are in a submarine. It is dark and damp. You can hear the sound of water dripping.",
    0,
    # {"apple": ("you pick up the apple", "pickup"), "banana": ("you pick up the banana", "pickup"), "rat": ("loose apple")},
)

SUMBARINE_TOILET = Room(
    "Submarine Toilet",
    "You are in the submarine toilet. your legs submerged in the ice-cold water. Trudging through the water you walk and walk but only a dark hollow path can be seen ahead but you don’t give up. All efforts in vain as you end up back in the beginning of your journey.",
    1,
    previous_room=0,
)


OIL_RIG_CORRIDOR = Room(
    "Oil Rig Corridor",
    "You are now entering the oil rig console. The air begins to feel stuffy, a pungent smell violating your senses making you feel lightheaded. You encounter these odd rooms which identify themselves as different challenges, which one do you dare to enter?",
    2,
    previous_room=0,
)

OIL_RIG_CONSOLE_ROOM = Room(
    "Oil Rig Console Room",
    "You are in the oil rig console room. Foreign, dark symbols plastered over the walls, unable to cypher. As if the symbols are missing a part of them but feels so familiar. The room starts to glow as if it sensed your presence, you are then suddenly faced with simple arithmetic questions which you must solve within 5 seconds.",
    3,
    previous_room=2,
)

OIL_RIG_RIDDLE_ROOM = Room(
    "Oil Rig Riddle Room",
    "You are in the oil rig riddle room. The room is crowded by colourful boxes and decorations, filled with awe by the beauty of the room you became distracted by the train of words appearing one by one before your eyes which eventually leading to a question and it’s four choices placed underneath, one of them being the answer to the question.",
    4,
    previous_room=2,
)

OIL_RIG_HANGMAN_ROOM = Room(
    "Oil Rig Hangman Room",
    "You are in the oil rig hangman room. You are faced with a dark room. The only light comes from a single bulb hanging from the ceiling. In the middle of the room, there is a table with a glowing letter engraved in it. There is a drawing of a stick figure hanging from a gallows. Underneath the drawing, there are a series of blank spaces. You realize that you are in a game of hangman. You must guess the word that is hidden in the blank spaces. If you guess the wrong letter, a part of the stick figure will be drawn. If you guess the wrong letter too many times, the stick figure will be complete, and you will lose the game.",
    5,
    previous_room=2,
)
OIL_RIG_WORDLE_ROOM = Room(
    "Oil Rig Wordle Room",
    "You are in the oil rig engine room. You enter a blank room, all white, expressionless leaving you thoughtless and confused. Completely silent all you can hear is your own breathing. The room starts to glow as if you it sensed your presence, 5 boxes suddenly appear in front of you, you are then faced with the challenge to guess the random 5-letter word while gaining hints from your wrong answers.",
    6,
    previous_room=2,
)

OIL_RIG_ENGINE_ROOM = Room(
    "Oil Rig Engine Room",
    "You are in the oil rig engine room. You must face the final challenge.",
    7,
    previous_room=2,
)

OIL_RIG_ENGINE_ROOM.add_requirment("Key 1")
OIL_RIG_ENGINE_ROOM.add_requirment("Key 2")
OIL_RIG_ENGINE_ROOM.add_requirment("Key 3")


def get_rooms():
    return [
        SUMBARINE_MAIN_ROOM,
        SUMBARINE_TOILET,
        OIL_RIG_CORRIDOR,
        OIL_RIG_CONSOLE_ROOM,
        OIL_RIG_RIDDLE_ROOM,
        OIL_RIG_HANGMAN_ROOM,
        OIL_RIG_WORDLE_ROOM,
        OIL_RIG_ENGINE_ROOM,
    ]
