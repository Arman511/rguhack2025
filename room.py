class Room:

    def __init__(self, name, description, id, previous_room=None):
        self.name = name
        self.description = description
        self.id = id
        self.previous_room = previous_room
        self.requirements = []

    def add_paths(self, paths):
        self.paths.update(paths)

    def can_enter_room(self, player):
        for requirement in self.requirements:
            if (
                requirement not in player.inventory
                and player.inventory[requirement] > 0
            ):
                return False
        if player.current_room == self.previous_room or self.previous_room is None:
            return True
        return False

    def add_requirment(self, item):
        self.requirements.append(item)
