import os

from Constants.AppConstants import *
from Constants.PlaylistUrls import *
from Services.RequestService import get_list
from Services.ScrapingService import extract_movies
from Services.TraktService import save_movies


def get_playlist_name(url):
    if url[::-1].find('?') > -1:
        return url[-url[::-1].find('/'):-url[::-1].find('?') - 1]
    else:
        return url[-url[::-1].find('/'):]


playlists = get_all_playlists()

print()

for i, e in enumerate(playlists):
    print(i, '-', get_playlist_name(e).replace("-", " "))

print(len(playlists), '-', 'Random Playlist')

user_choice = input("\nYour choice: ")

playlist_url = get_playlist(int(user_choice))

playlist_name = get_playlist_name(playlist_url)

file_name = PlaylistPath.replace(PlaylistName, playlist_name)

if os.path.isfile(file_name):
    with open(file_name) as f:
        movies = f.read().splitlines()
else:
    page_content = get_list(playlist_url)
    movies = extract_movies(page_content)
    movies = save_movies(movies, file_name)

print('\n' + playlist_name.replace("-", " ").title())
print('\n' + '\n'.join(random.sample(movies, 5 if len(movies) > 5 else len(movies))))
