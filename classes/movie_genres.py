from dataclasses import dataclass, field


@dataclass
class MovieGenres:
    @staticmethod
    def default_genre():
        return "Any Genre"

    @staticmethod
    def genre_list(genre_list):
        genres = [genre for genre in genre_list]
        genres.insert(0, MovieGenres.default_genre())
        return genres

    title: str = ''
    genre: str = field(default=default_genre())
