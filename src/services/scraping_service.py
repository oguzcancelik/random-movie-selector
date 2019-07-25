from bs4 import BeautifulSoup


def extract_movies(content):
    return BeautifulSoup(content, 'html.parser').find_all('div', {"data-type": "movie"})


def extract_playlist(content):
    page = BeautifulSoup(content, 'html.parser')
    playlist_id = page.find('input', {'id': "list-id"})["value"]
    name = page.find('span', {"class": "emojis-supported"}).text
    return [playlist_id, name]
