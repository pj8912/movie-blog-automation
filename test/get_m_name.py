import requests
from bs4 import BeautifulSoup

movie_name = "Titanic"
url = f"https://www.imdb.com/find?q={movie_name}&s=tt"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

first_result = soup.find("td", class_="result_text")
if first_result:
    first_result = first_result.a
    if first_result:
        # construct the movie page url
        movie_url = f"https://www.imdb.com{first_result['href']}"
        # get the movie page content
        response = requests.get(movie_url)
        soup = BeautifulSoup(response.content, "html.parser")
        # find the plot
        plot = soup.find("span", { "class" : "sc-16ede8a-1 jVOMyL" })
        if plot:
            print(plot.text)
        else:
            print("Plot not found.")
    else:
        print("Movie not found.")
else:
    print("Movie not found.")
