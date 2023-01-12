import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

transcript = soup.find("p", {"class": "caption-text"})
print(transcript)
