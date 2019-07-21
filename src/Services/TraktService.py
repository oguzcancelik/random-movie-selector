from Constants.TraktConstants import TraktMovieUrl


def save_movies(movies, file_name):
    movies = ['{:3} | {:4} {:38} | {}'.format("%" + i["data-percentage"], i["data-released"][:4],
                                              i["data-title"][:-6][:38], TraktMovieUrl + i["data-movie-id"])
              for i in movies if int(i["data-percentage"]) > 74]

    with open(file_name, "w") as f:
        for i in movies:
            f.write(i + "\n")

    return movies
