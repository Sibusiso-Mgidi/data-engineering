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

    def create_movie_keyword_tbl(self, conn, cur):
        """
        This method creates the movie_keyword table
        """

        # drop the table if already exists
        cur.execute("DROP TABLE IF EXISTS movie_keyword")

        # create 'movie_genre' table
        cur.execute("CREATE TABLE movie_genre("
                "movie_genre_id INT,"
                "movie_id INT,"
                "genre_id INT,"
                "PRIMARY KEY(movie_genre_id),"
                "FOREIGN KEY(movie_id) REFERENCES mdb.movies(movie_id),"
                "FOREIGN KEY(genre_id) REFERENCES mdb.genre(genre_id)"
                ")"
                )

        cur.close()
        conn.close()


    def create_keyword_tbl(self, conn, cur):
        """
        This method creates the keyworde table
        """
        
        # drop the table if already exists
        cur.execute("DROP TABLE IF EXISTS keyword")

        # create 'keyword' table
        cur.execute("CREATE TABLE mdb.keyword("
                "keyword_id INT,"
                "keyword_name VARCHAR(100),"
                "PRIMARY KEY(keyword_id)"
                ")"
                )

        cur.close()
        conn.close()


    def create_production_companies_tbl(self, conn, cur):
        """
        This method creates movie companies table.
        """
        # drop the table if already exists
        cur.execute("DROP TABLE IF EXISTS production_companies")

        # create 'production_companies' table
        cur.execute("CREATE TABLE production_companies("
                "company_id INT,"
                "company_name VARCHAR(100),"
                "PRIMARY KEY(company_id)"
                ")"
                )

        cur.close()
        conn.close()

    def create_movie_companies_tbl(self, conn, cur):
        """
        This method creates movies companies table.
        """

        # drop the table if already exists.
        cur.execute("DROP TABLE IF EXISTS movie_companies")
        
        # Create 'movie_companies' table
        cur.execute("CREATE TABLE movie_companies("
                "movie_companies_id INT,"
                "movie_id INT,"
                "company_id INT,"
                "PRIMARY KEY(movie_companies_id),"
                "FOREIGN KEY(movie_id) REFERENCES mdb.movies(movie_id),"
                "FOREIGN KEY(company_id) REFERENCES mdb.production_companies(company_id)"
                ")"
                )

        cur.close()
        conn.close()

    def create_production_countries_tbl(self, conn, cur):
        """
        This method creates production countries table.
        """

        # drop the table if already exists.
        cur.execute("DROP TABLE IF EXISTS production_countries")
    
        # Create 'production_countries' table
        cur.execute("CREATE TABLE production_countries("
                "country_id VARCHAR(10),"
                "country_name VARCHAR(100),"
                "PRIMARY KEY(country_id)"
                ")"
                )

        cur.close()
        conn.close()

    
    def create_movies_countries_tbl(self, conn, cur):
        """
        This method creates movies countries table.
        """

        # drop the table if already exists.
        cur.execute("DROP TABLE IF EXISTS movies_countries")
    
        # create 'movie_countries' table
        cur.execute("CREATE TABLE movie_countries("
                "movie_country_id INT,"
                "movie_id INT,"
                "country_id VARCHAR(10),"
                "PRIMARY KEY(movie_country_id),"
                "FOREIGN KEY(movie_id) REFERENCES mdb.movies(movie_id),"
                "FOREIGN KEY(country_id) REFERENCES mdb.production_countries(country_id)"
                ")"
                )

        cur.close()
        conn.close()

    
    def create_spoken_language_tbl(self, conn, cur):
        """
        This method creates spoken language table.
        """

        # drop the table if already exists.
        cur.execute("DROP TABLE IF EXISTS spoken_languages")
    
        # create 'spoken_languages' table
        cur.execute("CREATE TABLE spoken_languages("
                    "language_id VARCHAR(10),"
                    "language_name VARCHAR(100),"
                    "PRIMARY KEY(language_id)"
                    ")"
                    )

        cur.close()
        conn.close()


    def create_movie_languages_tbl(self, conn, cur):
        """
        This method creates movies language table.
        """

        # drop the table if already exists
        cur.execute("DROP TABLE IF EXISTS movie_languages")


        # create 'movie_languages' table
        cur.execute("CREATE TABLE movie_languages("
                "movie_lang_id INT,"
                "movie_id INT,"
                "language_id VARCHAR(10),"
                "PRIMARY KEY(movie_lang_id),"
                "FOREIGN KEY(movie_id) REFERENCES mdb.movies(movie_id),"
                "FOREIGN KEY(language_id) REFERENCES mdb.spoken_languages(language_id)"
                ")"
                )

        cur.close()
        conn.close()