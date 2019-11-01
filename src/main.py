from constants.default_values import *
from constants.playlist_urls import *
from services.request_service import get_list
from services.scraping_service import *
from services.trakt_service import *


def get_playlist_name(url):
    reverse_url = url[::-1]
    if reverse_url.find('?') > -1:
        return url[-reverse_url.find('/'):-reverse_url.find('?') - 1]
    else:
        return url[-reverse_url.find('/'):]


def get_default(choice, value):
    if not choice:
        return value
    return int(choice)


def list_playlists():
    print('\n0 - random playlist')

    for j, e in enumerate(playlists, start=1):
        print(j, '-', get_playlist_name(e).replace("-", " "))


def run():
    playlist_choice = input("\nPlaylist choice ({} is default): ".format(DefaultPlaylist))
    percentage_choice = input("\nMin Percentage ({} is default): ".format(DefaultPercentage))
    year_choice = input("\nAfter Year ({} is default): ".format(DefaultYear))

    playlist_choice = get_default(playlist_choice, DefaultPlaylist)
    percentage_choice = get_default(percentage_choice, DefaultPercentage)
    year_choice = get_default(year_choice, DefaultYear)

    playlist_url = get_playlist(playlist_choice)

    playlist_name = get_playlist_name(playlist_url)

    movies = check_list(playlist_name)

    if not movies:
        page_content = get_list(playlist_url)
        movies = extract_movies(page_content)
        playlist_info = extract_playlist(page_content)
        movies = save_movies(movies, playlist_info, playlist_name)

    print('\n' + movies[0][1].title() + '\n')

    movies = list(filter(lambda x: percentage_choice <= int(x[3]) < 100 and year_choice <= int(x[4]), movies))

    if not movies:
        print('No movies with more than', percentage_choice - 1, 'percentage in playlist.')
        quit()

    movie_number = 10

    random_movies = random.sample(movies, movie_number if len(movies) > movie_number else len(movies))
    random_movies = sorted(random_movies, key=lambda x: x[3], reverse=True)

    for i in random_movies:
        print('%{:2} | {:4} {:38} | {}'.format(i[3], i[4], i[6][:38], i[7]))


playlists = get_all_playlists()

while True:
    list_playlists()
    run()
    user_choice = input("\nPress enter to continue:  ")
    if user_choice:
        print("\nProgram terminated.\n")
        break
    print("\n")
