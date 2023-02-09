import requests

def check_category(title):
    url = 'https://en.wikipedia.org/w/api.php'
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
    try:
        categories = list(data['query']['pages'].values())[0]['categories']
    except KeyError:
        return 0
    for category in categories:
        if 'film' in category['title']:
            return 1
    return 0