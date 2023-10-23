class MovieGenres:
    @staticmethod
    def default_genre():
        return "Any Genre"

    def __init__(self):
        self.title = ''
        self.genre = MovieGenres.default_genre()

