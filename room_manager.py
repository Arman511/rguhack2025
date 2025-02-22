from room import Room

SUMBARINE_MAIN_ROOM = Room(
    "Submarine",
    "You are in a submarine. It is dark and damp. You can hear the sound of water dripping.",
    0,
)

SUMBARINE_TOILET = Room(
    "Submarine Toilet",
    "You are in the submarine toilet. It is dark and damp. You can hear the sound of water dripping.",
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
    "You are in the oil rig console room. It is dark and damp. You can hear the sound of water dripping.",
    3,
    previous_room=2,
)

OIL_RIG_RIDDLE_ROOM = Room(
    "Oil Rig Riddle Room",
    "You are in the oil rig riddle room. Guess the word while gaining hints from your wrong answers.",
    4,
    previous_room=2,
)

OIL_RIG_HANGMAN_ROOM = Room(
    "Oil Rig Hangman Room",
    "You are in the oil rig hangman room. Guess the word before the human dies.",
    5,
    previous_room=2,
)
OIL_RIG_WORDLE_ROOM = Room(
    "Oil Rig Wordle Room",
    "You are in the oil rig engine room. Guess the word while gaining hints from your wrong answers.",
    6,
    previous_room=2,
)

OIL_RIG_ENGINE_ROOM = Room(
    "Oil Rig Engine Room",
    "You are in the oil rig engine room. It is dark and damp. You can hear the sound of water dripping.",
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
