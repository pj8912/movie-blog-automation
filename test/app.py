import wikipediaapi

wiki = wikipediaapi.Wikipedia(
        language = 'en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
        
)


movie_name = "Inception"
page = wiki.page(movie_name)

if page.exists():
    plot_summary = page.summary[:]
    print(plot_summary)

else:
    print("Page - {} does not exist!".format(movie_name))






