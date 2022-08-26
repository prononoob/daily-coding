import requests
from bs4 import BeautifulSoup


#InPost response demo

class InPost:
	def __init__(self):
		self.lin1 = 'https://inpost.pl/sledzenie-przesylek?number='

	def genProperlink(self, inpID):
		self.inpID = inpID
		self.properlink = self.lin1 + str(self.inpID)

	def findData(self):
		self.r = requests.get(self.properlink)
		soup = BeautifulSoup(self.r.content, 'html.parser')
		soup = str(soup)
		self.pos1 = soup.find('paczkomacie]')
		self.shorttxt = soup[self.pos1:self.pos1+800]
		self.pos1 = self.shorttxt.find('title')+8
		self.shorttxt = self.shorttxt[self.pos1:self.pos1+50]

	def analState(self, data):
		self.data = data.split('","')[0]

def statusPaczki(inpID):
	f = InPost()
	f.genProperlink(inpID)
	f.findData()
	f.analState(f.shorttxt)
	print('Status paczki: ', f.data)


# Wpisz numer paczki w nawiasie
statusPaczki()