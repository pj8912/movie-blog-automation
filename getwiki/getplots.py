import requests
from bs4 import BeautifulSoup
import threading

class Plot(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.plot=""
        
    def run(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        plot_start = soup.find("span", {"class":"mw-headline", "id":"Plot"})
        cast_start = soup.find("span", {"class":"mw-headline", "id":"Cast"})
        if plot_start and cast_start:
            # plot = ""
            next_sibling = plot_start.parent.find_next_sibling()
            while next_sibling and next_sibling != cast_start.parent:
                if next_sibling.string:
                    self.plot += next_sibling.string
                else:
                    for child in next_sibling.children:
                        if child.string:
                            self.plot += child.string
                next_sibling = next_sibling.find_next_sibling()
            return self.plot