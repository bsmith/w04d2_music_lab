class Artist:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Artist({self.name!r}, id={self.id!r})"