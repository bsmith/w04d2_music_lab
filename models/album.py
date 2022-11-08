class Album:
    def __init__(self, title, genre, artist, id=None):
        self.title = title
        self.genre = genre
        self.artist = artist
        self.id = id

    def __repr__(self):
        return f"Album({self.title!r}, {self.genre!r}, {self.artist!r}, id={self.id!r})"