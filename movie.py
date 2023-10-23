class Movie:
    @staticmethod
    def calc_duration(minutes=90):
        h = minutes // 60
        m = minutes % 60
        return f'{h}:{m}'
    @staticmethod
    def getMovieList(movie_data):
        # return [Movie(title=row[0], duration=int(row[1]), rating=row[2], genres='/'.join(row[3])) for row in movie_data]
        return [Movie(title=row[0], duration=Movie.calc_duration(row[1]), rating=row[2], genres=row[3].split('/')) for row in
                movie_data]

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


    @staticmethod
    def get_data():
        return (
            ("Spiderman 3", "2:20", "15", "Action"),
            ("Child's Play ", "90:00", "18", "Horror/Thriller"),

        )


    @staticmethod
    def get_movie_data():
        return {
            'movie': {
                'title': "Spiderman 3",
                'duration': 220,
                'rating': '15',
                'genres': ['Action']
            },
            'movie2': {
                'title': "Child's Play",
                'duration': 90,
                'rating': '18',
                'genres': ['Horror', 'Thriller']
            }
        }
