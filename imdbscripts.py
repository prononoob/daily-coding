import requests
from bs4 import BeautifulSoup


class Scraper():
    #Setting english headers
    global headers, z, movies
    headers, z, movies = {"Accept-Language": "en-US,en;q=0.5"}, False, {}

    def __init__(self):
        print('Script Initialized!')
         
    #Search for title based on imID
    def searchtitle(self, imID):
        global tit
        properlink = 'https://www.imdb.com/title/' + imID +'/'
        r = requests.get(properlink, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        tit = str(soup.title)[7:-15]
        print(tit)
        if z == True:
            movies[tit] = 0


    #Search for rating based on imID 
    def searchrating(self, imID):
        global rev
        properlink = 'https://www.imdb.com/title/' + imID +'/'
        r = requests.get(properlink, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        longtxt = str(soup).find('"@type":"AggregateRating"')
        shorttxt = str(soup)[longtxt+70:longtxt+110]
        stars = shorttxt.find('ratingValue')
        if shorttxt[stars+14] == '.':
            rev = float(shorttxt[stars+13:stars+16])
            print(rev)
            if z == True:
                movies[tit] = rev
        else:
            rev = shorttxt[stars+13]
            print(rev)
            if z == True:
                movies[tit] = rev

    #Find all titles and ratings in top 250
    #and write them to top250.txt
    def findall(self):
        global z
        z = True
        mainlink = 'https://www.imdb.com/chart/top/'
        m = requests.get(mainlink, headers = headers)
        soup = BeautifulSoup(m.content, 'html.parser')
        numba = soup.find_all(class_='titleColumn')
        for i in range(250):
            tits = str(numba).find('href') #+13
            numba = str(numba)[tits:]
            tite = str(numba).find('title=') #-3
            imID = str(numba)[13:tite-3]
            f.searchtitle(imID)
            f.searchrating(imID)
            numba = numba[100:]
        file = open('top250.txt', 'w')
        for i in movies:
            dicline = i + ' ' + str(movies[i]) + "\n"
            file.write(dicline)
        #print(movies)


f = Scraper()
f.findall()
