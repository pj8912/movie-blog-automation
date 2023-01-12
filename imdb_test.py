from imdb import Cinemagoer
ia  = Cinemagoer()
movies = ia.get_top250_movies()
for i in range(len(movies)):
    print(f'[{i}]', ':', movies[i]['title'])

# asd = ['ads','ad','gfg','fg','gt','gtd']

# for i in range(len(asd)):
#     print(f'[{i}]', ':', asd[i])