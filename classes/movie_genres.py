from dataclasses import dataclass, field


@dataclass
class MovieGenres:
    @staticmethod
    def default_genre():
        return "Any Genre"

    title: str = ''
    genre: str = field(default=default_genre())
