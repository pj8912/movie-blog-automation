#get title
from imdb import Cinemagoer
ia  = Cinemagoer()
movies = ia.get_top250_movies()
movie_list = [] #movie list that has the titles
for i in range(len(movies)):
    movie_list.append(movies[i]['title'])
    print(f'[{i}]', ':', movies[i]['title'])




#seacrh wikipedia, for the available results create url for each of them
import wikipedia
search_term = input("Search: ")
result = wikipedia.search(search_term, 10)
print(result)
print()
print('Their urls')
print()


def add_underscore(a):
    a1 = ""
    for i in range(len(a)):
        if a[i] == ' ':
            a1 = a1 + '_'
        else:
            a1 = a1 + a[i]
    return a1



print('\n-----------------\n')

for i in result:    # i is the title
    res = add_underscore(i)
    base_url = "https://en.wikipedia.org/wiki/"
    url = base_url+res
    print(url)






#check categories based on 'title'
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



#get plot of a movie in wikipedia
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Inception"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

plot_section = soup.find("span", {"class": "mw-headline", "id": "Plot"}).find_next("p")
print(plot_section.text)
for next_tag in plot_section.find_next_siblings():
    if next_tag.name == "p":
        print(next_tag.text)
    elif next_tag.name != "p":
        break

