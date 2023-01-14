from imdb import Cinemagoer
ia  = Cinemagoer()
movies = ia.get_top250_movies()
movie_list = []
for i in range(len(movies)):
    movie_list.append(movies[i]['title'])
    # print(f'[{i}]', ':', movies[i]['title'])



for i in movie_list:
    print(i)

# asd = ['ads','ad','gfg','fg','gt','gtd']

# for i in range(len(asd)):
#     print(f'[{i}]', ':', asd[i])