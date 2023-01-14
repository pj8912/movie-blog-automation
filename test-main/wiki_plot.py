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
