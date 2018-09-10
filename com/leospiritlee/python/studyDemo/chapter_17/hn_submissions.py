import requests

from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

resp = requests.get(url)

print('Status code:', resp.status_code)