from dataclasses import dataclass, field


@dataclass()
class MovieGenres:

    def filter_list(self):
        filters = []

        if self.genre != MovieGenres.default_genre():
            filters.append(lambda movie: self.genre.casefold() in movie.genre.casefold())

        if self.title:
            filters.append(lambda movie: self.title.casefold() in movie.title.casefold())

        return list((filter(lambda p: all(f(p) for f in filters), self.movie_list)))

    @staticmethod
    def default_genre():
        return "Any Genre"

    title: str = ''
    genre: str = field(default=default_genre())
    movie_list: tuple = field(default_factory=tuple)
