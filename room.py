class Room:

    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.paths = {}
        self.requirements = []

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
