from imdb import Cinemagoer
import wikipedia


ia  = Cinemagoer()
movies = ia.get_top250_movies()
movie_list = []
for i in range(len(movies)):
    movie_list.append(movies[i]['title'])



url_list = []


for i in movie_list:
    # title = add_underscore(i)
    # title_list.append(title)
    res = add_underscore(i)
    base_url = "https://en.wikipedia.org/wiki/"
    url = base_url+res
    url_list.append(url)