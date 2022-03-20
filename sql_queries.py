from distutils.util import execute


class CreateTables(object):
    """
    This is a blueprint for creating tables in the database.
    """
    def __init__(self, db_name):
        self.database_name = db_name

    def create_movies_tbl(self, conn, cur):
        """
        This method creates movies table in the database.
        """
        
        # drop the table if already exists
        cur.execute("DROP TABLE IF EXISTS movies")

        # create 'movies' table
        cur.execute("CREATE TABLE mdb.movies("
                    "movie_id INT,"
                    "budget INT,"
                    "homepage VARCHAR(1000),"
                    "original_language VARCHAR(100),"
                    "original_title VARCHAR(100),"
                    "overview VARCHAR(2000),"
                    "popularity FLOAT,"
                    "release_date VARCHAR(100),"
                    "revenue BIGINT,"
                    "runtime INT,"
                    "status VARCHAR(100),"
                    "tagline VARCHAR(2000),"
                    "title VARCHAR(100),"
                    "vote_average FLOAT,"
                    "vote_count INT,"
                    "PRIMARY KEY(movie_id)"
                    ")"
                    )
        cur.close()
        conn.close()

    def create_genre_tbl(self,conn, cur):
        """
        This method creates genre table in the database.
        """

        # drop the table if already exists
        cur.execute("DROP TABLE IF EXISTS genre")

        # create 'genre' table
        cur.execute("CREATE TABLE genre("
                    "genre_id INT,"
                    "name_genre VARCHAR(100),"
                    "PRIMARY KEY(genre_id)"
                    ")"
                    )

        cur.close()
        conn.close()