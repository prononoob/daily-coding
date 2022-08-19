import requests
from bs4 import BeautifulSoup


class Scraper():
    #Setting english headers
    global headers
    headers = {"Accept-Language": "en-US,en;q=0.5"}

    def __init__(self):
        print('Script Initialized!')
         
    #Search for title based on imID
    def searchtitle(self, imID):
        properlink = 'https://www.imdb.com/title/' + imID +'/'
        r = requests.get(properlink, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        print(str(soup.title)[7:-15])

    #Search for rating based on imID 
    def searchrating(self, imID):
        properlink = 'https://www.imdb.com/title/' + imID +'/'
        r = requests.get(properlink, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        longtxt = str(soup).find('"@type":"AggregateRating"')
        shorttxt = str(soup)[longtxt+70:longtxt+110]
        stars = shorttxt.find('ratingValue')
        if shorttxt[stars+14] == '.':
            print(shorttxt[stars+13:stars+16])
        else:
            print(shorttxt[stars+13])
