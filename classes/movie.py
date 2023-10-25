from dataclasses import dataclass, field

from classes.helper import Helper


@dataclass
class Movie:
    title: str = ''
    duration: int = 0
    rating: str = ''
    genre: str = ''

    @staticmethod
    def movie_list(movies):
        movie_list = []
        for row in movies:
            title = row[0]
            duration = Helper.calc_duration(int(row[1]))
            rating = row[2]
            genre = row[3]
            movie_list.append(Movie(title, duration, rating, genre))
        return movie_list

    @staticmethod
    def columns():
        return [
            'Movie',
            'Duration',
            'Rating',
            'Genre'
        ]
