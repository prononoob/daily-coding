import requests
from bs4 import BeautifulSoup


class Scraper():
    global headers
    headers = {"Accept-Language": "en-US,en;q=0.5"}

    def __init__(self):
        print('Script Initialized!')
         
    def searchtitle(self, imID):
        properlink = 'https://www.imdb.com/title/' + imID +'/'
        r = requests.get(properlink, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        print(str(soup.title)[7:-15])

    def searchrating(self, imID):
        properlink = 'https://www.imdb.com/title/' + imID +'/'
        r = requests.get(properlink, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        longtxt = soup.script
        stars = str(longtxt).find('contentRating')
        if str(longtxt)[stars-5] == '.':
            print(str(longtxt)[stars-6:stars-3])
        else:
            print(str(longtxt)[stars-4])
