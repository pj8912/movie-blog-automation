#get title
from imdb import Cinemagoer
import wikipedia
import requests
from bs4 import BeautifulSoup




ia  = Cinemagoer()
movies = ia.get_top250_movies()
movie_list = [] #movie list that has the titles
for i in range(len(movies)):
    movie_list.append(movies[i]['title'])
    # print(f'[{i}]', ':', movies[i]['title'])


title_list = []

for i in movie_list:
    search_term = i
    result = wikipedia.search(search_term, 10)
    for x in result:
        title = add_underscore(x)
        title_list.append(title)


checked_list = []

for i in title_list:
    if check_cat(i) == 0:
        break
    if check_cat(i) == 1:
        checked_list.append(i)


#create url for titles in checked list to fetch the 'Plot' 
movie_urls = []
base_url = "https://en.wikipedia.org/wiki/"
for i in checked_list:
    url = base_url+i
    movie_urls.append(url)
    

#fetching the 'PLOT'
#assuming that we find one or more than title's that have one or more 'film' category
#eventhough we want to find imdb = wikipedia match

plots = []
for i in movie_urls:
    response = requests.get(i)
    soup = BeautifulSoup(response.content, "html.parser")
    plot_section = soup.find("span", {"class": "mw-headline", "id": "Plot"}).find_next("p")
    movie_plot = []
    first_p = plot_section.text
    movie_plot.append(first_p)
    for next_tag in plot_section.find_next_siblings():
    if next_tag.name == "p":
        # print(next_tag.text)
        movie_plot.append(next_tag.text)
        plots.append(movie_plot)
        del(movie_plot) 
    elif next_tag.name != "p":
        break
    # ......


        

#check category 
def check_cat(title):
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
    categories = list(data['query']['pages'].values())[0]['categories']
    film_check = 0 #check if any 'film' category status: 1 -> yes, 0-> no
    for category in categories:
        if 'film' in category['title']:
            film_check = 1
        else:
            film_check = 0
    return film_check  #return status








#add underscore in white spaces same as wikipedia queries
def add_underscore(a):
    a1 = ""
    for i in range(len(a)):
        if a[i] == ' ':
            a1 = a1 + '_'
        else:
            a1 = a1 + a[i]
    return a1





#seacrh wikipedia, for the available results create url for each of them
# import wikipedia
# search_term = input("Search: ")
result = wikipedia.search(search_term, 10)
for i in result:
    title = add_underscore(i)
    title_list.append(title)

