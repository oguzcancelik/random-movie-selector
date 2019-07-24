import random

URLS = [

    "https://trakt.tv/users/oguzcan/watchlist?display=movie&sort=rank,asc",
    "https://trakt.tv/users/justin/lists/imdb-top-rated-movies?sort=rank,asc",
    "https://trakt.tv/users/marzipan-pie/lists/inspiring-films",
    "https://trakt.tv/users/bmonomad/lists/organized-crime",
    "https://trakt.tv/users/xilfneps/lists/all-of-these-films-are-worth-seeing-1400-titles?sort=percentage,asc",
    "https://trakt.tv/users/m4milo/lists/empire-s-500-greatest-movies-of-all-time?sort=rank,asc",
    "https://trakt.tv/users/blazer380/lists/underrated-movies?sort=rank,asc",
    "https://trakt.tv/users/ohuaithnin/lists/imdb-top-250-movies-1996-2019?sort=title,asc",
    "https://trakt.tv/users/movistapp/lists/animation?sort=rank,asc",
    "https://trakt.tv/users/captainnapalm/lists/1001-greatest-movies-of-all-time",
    "https://trakt.tv/users/xilfneps/lists/genre-drama-4700-titles-1970-2013",
    "https://trakt.tv/users/xilfneps/lists/genre-adventure-1250-titles-1970-2013",

]


def get_all_playlists():
    return URLS


def get_playlist(i):
    if len(URLS) == i:
        return random.choice(URLS)
    return URLS[i]
