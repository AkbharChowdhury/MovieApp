import sqlite3

from movie_genres import MovieGenres


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('cinema.db')
        self.__cur = self.conn.cursor()

    def show_movie_list(self, movie_genre: MovieGenres):
        genre = movie_genre.genre
        params = {'title': f'%{movie_genre.title}%'}

        sql = """
                SELECT m.title,
                       m.duration,
                       r.rating,
                       Group_concat(g.genre, '/') genre_list
                FROM   MovieGenres mg
                       JOIN Movies m
                         ON mg.movie_id = m.movie_id
                       JOIN genres g
                         ON mg.genre_id = g.genre_id
                       JOIN Ratings r
                         ON m.rating_id = r.rating_id
                         WHERE title LIKE :title
                          
                GROUP BY m.movie_id
        """
        if genre.casefold() != MovieGenres.default_genre().casefold():
            sql += " HAVING genre_list LIKE :genre"
            params['genre'] = f'%{genre}%'

        return self.__cur.execute(sql, params)

    def fetch_genres(self):
        self.__cur.execute("""
                    SELECT  DISTINCT g.genre
            FROM MovieGenres mg
            JOIN Genres g on g.genre_id = mg.genre_id
            ORDER by g.genre
        """)
        return self.__cur.fetchall()

    def __del__(self):
        self.conn.close()
