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
    "https://trakt.tv/users/ramazandro/lists/turkish-movies",
    "https://trakt.tv/users/lish408/lists/rotten-tomatoes-best-of-2019",
    "https://trakt.tv/users/philrivers/lists/reddit-top-250-2018-edition",
    "https://trakt.tv/users/giladg/lists/subreddit-selections",
    "https://trakt.tv/users/benfranklin/lists/underdog-stories",
    "https://trakt.tv/users/benfranklin/lists/interconnected-characters-stories",
    "https://trakt.tv/users/benfranklin/lists/based-on-a-true-story",
    "https://trakt.tv/users/benfranklin/lists/sport-nfl-movies",
    "https://trakt.tv/users/benfranklin/lists/let-s-talk-business-movies-4-entrepreneurs",
    "https://trakt.tv/users/donxy/lists/spy-films-1465050",
    "https://trakt.tv/users/listr/lists/500-essential-cult-movies-the-ultimate-guide-by-jennifer-eiss",
    "https://trakt.tv/users/movistapp/lists/war",
    "https://trakt.tv/users/felix66/lists/trakt-movie-decade-1990s",
    "https://trakt.tv/users/felix66/lists/trakt-movie-decade-2000s",
    "https://trakt.tv/users/felix66/lists/trakt-movie-decade-2010s",
    "https://trakt.tv/users/remontant/lists/apocalyptic-and-post-apocalyptic-movies",
    "https://trakt.tv/users/remontant/lists/dystopian-movies",
    "https://trakt.tv/users/lish408/lists/mindfuck",

]


def get_all_playlists():
    return URLS


def get_playlist(i):
    if i == 0:
        return random.choice(URLS)
    elif len(URLS) >= i:
        return URLS[i - 1]
    else:
        quit()
