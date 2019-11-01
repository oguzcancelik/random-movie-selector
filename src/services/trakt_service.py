import sqlite3

from constants.trakt_constants import TraktMovieUrl

connection = sqlite3.connect('../db.sqlite3')
c = connection.cursor()


def check_list(playlist_url_name):
    with connection:
        c.execute("""SELECT * FROM playlist_movies WHERE playlist_url_name like ?""", (playlist_url_name,))
    result = c.fetchall()
    if result:
        return [list(i) for i in result]
    return None


def save_movies(movies, list_info, playlist_url_name):
    insert_tracks = [[list_info[0], list_info[1], playlist_url_name, i["data-percentage"], i["data-released"][:4],
                      i["data-movie-id"], i["data-title"][:-7], TraktMovieUrl + i["data-movie-id"], i["data-votes"]]
                     for i in movies]
    with connection:
        c.executemany("""INSERT INTO playlist_movies VALUES (?,?,?,?,?,?,?,?,?)""", insert_tracks)
    return insert_tracks
