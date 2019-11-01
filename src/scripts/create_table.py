import sqlite3


def create_table(table_name, columns):
    with connection:
        c.execute("CREATE TABLE " + table_name + columns)


connection = sqlite3.connect('../db.sqlite3')
c = connection.cursor()

create_table('playlist_movies', """ (playlist_id text, playlist_name text, playlist_url_name text, 
percentage int, release_year int, movie_id text, movie_name text, movie_url text, votes int)""")
