# WEB Scraping
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.markup = requests.get(url).text

    def parse(self):
        soup = BeautifulSoup(self.markup, 'html.parser')
        links = soup.findAll('h3')
        new_links = [str(link).replace('<h3>', '').replace('</h3>', '') for link in links]
        for link in enumerate(new_links, 1):
            print(link)

if __name__ == '__main__':
    s = Scraper('https://kathmandupost.com/sports')
    s.parse()