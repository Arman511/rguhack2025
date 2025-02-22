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
    "You are in an oil rig corridor. It is dark and damp. You can hear the sound of water dripping.",
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
    "You are in the oil rig riddle room. It is dark and damp. You can hear the sound of water dripping.",
    4,
    previous_room=2,
)

OIL_RIG_HANGMAN_ROOM = Room(
    "Oil Rig Hangman Room",
    "You are in the oil rig hangman room. It is dark and damp. You can hear the sound of water dripping.",
    5,
    previous_room=2,
)
OIL_RIG_WORDLE_ROOM = Room(
    "Oil Rig Wordle Room",
    "You are in the oil rig engine room. It is dark and damp. You can hear the sound of water dripping.",
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
