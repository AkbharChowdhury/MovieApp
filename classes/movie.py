class Movie:

    def __init__(self, title, duration, rating, genres):
        self.title = title
        self.duration = duration
        self.rating = rating
        self.genres = genres

    def __str__(self):
        return f'{self.title}, {self.duration}, {self.rating}, {self.genres}'

    @staticmethod
    def columns():
        return [
            'Movie',
            'Duration',
            'Rating',
            'Genre'
        ]
