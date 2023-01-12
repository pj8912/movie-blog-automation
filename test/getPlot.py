from imdb import Cinemagoer
ia = Cinemagoer()

ia.get_movie_infoset()
movie = ia.get_movie('0133093')
print(movie.infoset2keys['plot'][0])

# print(movie.current_info.plot)
