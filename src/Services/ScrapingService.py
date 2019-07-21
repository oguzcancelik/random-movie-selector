from bs4 import BeautifulSoup


def extract_movies(content):
    return BeautifulSoup(content, 'html.parser').find_all('div', {"data-type": "movie"})
