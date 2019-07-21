import os
import random

from Constants.PlaylistUrls import get_random_playlist
from Services.RequestService import get_list
from Services.ScrapingService import extract_movies
from Services.TraktService import save_movies

url = get_random_playlist()

if url[::-1].find('?') > -1:
    playlist_name = url[-url[::-1].find('/'):-url[::-1].find('?') - 1]
else:
    playlist_name = url[-url[::-1].find('/'):]

file_name = 'Lists/' + playlist_name + '.txt'

if os.path.isfile(file_name):
    with open(file_name) as f:
        movies = f.read().splitlines()
else:
    page_content = get_list(url)
    movies = extract_movies(page_content)
    movies = save_movies(movies, file_name)

print('\n' + playlist_name.replace("-", " ").title())
print('\n' + '\n'.join(random.sample(movies, 5 if len(movies) > 5 else len(movies))))
