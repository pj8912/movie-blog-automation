import requests

url = 'https://en.wikipedia.org/w/api.php'

# title = 'Python (programming language)'
title = 'Cube_(1997_film)'

params = {
    'action': 'query',
    'format': 'json',
    'titles': title,
    'prop': 'categories',
    'clshow': '!hidden',
    'cllimit': 500
}

response = requests.get(url, params=params)
data = response.json()

categories = list(data['query']['pages'].values())[0]['categories']

for category in categories:
    print(category['title'])
