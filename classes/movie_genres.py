from dataclasses import dataclass, field


@dataclass()
class MovieGenres:

    def is_default_genre(self):
        return self.genre == MovieGenres.default_genre()

    def filter_list(self):
        filters = (
            lambda p: self.title.casefold() in p.title.casefold() if self.title else [''],
            lambda p: self.genre.casefold() in p.genre.casefold() if not self.is_default_genre() else ['']
        )
        return list((filter(lambda p: all(f(p) for f in filters), self.movie_list)))

    @staticmethod
    def default_genre():
        return "Any Genre"

    title: str = ''
    genre: str = field(default=default_genre())
    movie_list: tuple = field(default_factory=tuple)
