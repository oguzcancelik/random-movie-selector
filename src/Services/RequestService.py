import requests


def get_list(url):
    return requests.get(url).content
