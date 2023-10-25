import sqlite3

from classes.movie_genres import MovieGenres


class Database:
    def __init__(self):
        self.__conn = sqlite3.connect('cinema.db')
        self.__cur = self.__conn.cursor()

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
        if not movie_genre.is_default_genre():
            sql += " HAVING genre_list LIKE :genre"
            params['genre'] = f'%{genre}%'

        return self.__cur.execute(sql, params)

    def show_movie_list_fp(self):
        return self.__cur.execute("""
                   SELECT
                        m.title,
                        m.duration,
                        r.rating,
                        GROUP_CONCAT(g.genre, '/') genre_list
                    FROM
                        MovieGenres mg
                    JOIN Movies m ON
                        mg.movie_id = m.movie_id
                    JOIN genres g ON
                        mg.genre_id = g.genre_id
                    JOIN Ratings r ON
                        m.rating_id = r.rating_id
                    GROUP BY
                        m.movie_id
           """)

    def fetch_genres(self):
        self.__cur.execute("""
                    SELECT  DISTINCT g.genre
            FROM MovieGenres mg
            JOIN Genres g on g.genre_id = mg.genre_id
            ORDER by g.genre
        """)
        return self.__cur.fetchall()

    def __del__(self):
        self.__conn.close()
