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


playlists = get_all_playlists()

print()

for i, e in enumerate(playlists):
    print(i, '-', get_playlist_name(e).replace("-", " "))

print(len(playlists), '-', 'random playlist')

playlist_choice = input("\nPlaylist choice: ")
percentage_choice = input("\nMin Percentage: ")

if not percentage_choice:
    percentage_choice = 75
else:
    percentage_choice = int(percentage_choice)

playlist_url = get_playlist(int(playlist_choice))

playlist_name = get_playlist_name(playlist_url)

movies = check_list(playlist_name)

if not movies:
    page_content = get_list(playlist_url)
    movies = extract_movies(page_content)
    playlist_info = extract_playlist(page_content)
    movies = save_movies(movies, playlist_info, playlist_name)

movie_number = 5

print('\n' + movies[0][1].title() + '\n')

movies = list(filter(lambda x: percentage_choice <= int(x[3]) < 100, movies))

if not movies:
    print('No movies with more than', percentage_choice - 1, 'percentage in playlist.')
    quit()

random_movies = random.sample(movies, movie_number if len(movies) > movie_number else len(movies))
random_movies = sorted(random_movies, key=lambda x: x[3], reverse=True)

for i in random_movies:
    print('%{:2} | {:4} {:38} | {}'.format(i[3], i[4], i[6][:38], i[7]))
