import requests
from bs4 import BeautifulSoup
   
import threading



class WikiImage(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.image_url = None
    
    def run(self):
        response = requests.get(self.url)  
        soup = BeautifulSoup(response.content, "html.parser")
        image_tag = soup.find("a", class_="image")
        images = soup.find_all("img", class_="thumbborder")
        self.image_url = "https:" + image_tag.img["src"]
        return self.image_url