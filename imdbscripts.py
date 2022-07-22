import requests
from bs4 import BeautifulSoup


class Scraper():
    def __init__(self):
        print('Script Initialized!')
    def searchtitle(self, imID):
        
        properlink = 'https://www.imdb.com/title/' + imID +'/'
        headers = {"Accept-Language": "en-US,en;q=0.5"}
        r = requests.get(properlink, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        print(str(soup.title)[7:-15])

