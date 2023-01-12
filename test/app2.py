import requests
from bs4 import BeautifulSoup

movie_name = input("Movie Name: ")


url = f"https://en.wikipedia.org/wiki/{movie_name}"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

plot = soup.find("p", text=lambda t: t and len(t) > 10)

if plot:
    print("Plot:")
    print(plot.text)
else:
    print("Plot not found")


