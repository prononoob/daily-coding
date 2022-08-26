import requests
from bs4 import BeautifulSoup


class InPost:
	def __init__(self):
		self.lin1 = 'https://inpost.pl/sledzenie-przesylek?number='

	def genProperlink(self, inpID):
		self.inpID = inpID
		if str(self.inpID).isdigit() == True and len(str(self.inpID)) == 24:
			self.properlink = self.lin1 + str(self.inpID)
		else:
			exit('Numer przesylki jest niepoprawny')

	def findData(self):
		self.r = requests.get(self.properlink)
		soup = BeautifulSoup(self.r.content, 'html.parser')
		soup = str(soup)
		self.pos1 = soup.find('paczkomacie]')
		self.shorttxt = soup[self.pos1:self.pos1+80]
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