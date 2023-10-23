class MovieGenres:
    @staticmethod
    def genre_list(genre_list):
        genres = [genre for genre in genre_list]
        genres.insert(0, MovieGenres.default_genre())
        return genres

    @staticmethod
    def default_genre():
        return "Any Genre"

    def __init__(self):
        self.title = ''
        self.genre = MovieGenres.default_genre()
