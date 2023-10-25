from dataclasses import dataclass, field


@dataclass
class MovieGenres:
    def __default_genres(self):
        return MovieGenres.default_genre()

    def filter_list(self):
        filters = []
        if self.title:
            filters.append(lambda p: self.title.casefold() in p.title.casefold())
        if self.genre != "Any Genre":
            filters.append(lambda p: p.genre in self.genre)
        try:
            return list((filter(lambda p: all(f(p) for f in filters), self.movie_list)))
        except StopIteration:
            return None

    @staticmethod
    def default_genre():
        return "Any Genre"

    title: str = ''
    genre: str = field(default=default_genre())
    movie_list: list = field(default_factory=list)
