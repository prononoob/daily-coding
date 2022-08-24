import requests
from bs4 import BeautifulSoup


#InPost response demo

class InPost:
	def __init__(self):
		self.lin1 = 'https://inpost.pl/sledzenie-przesylek?number='
		print('Class initialized')

	def genProperlink(self, inpID):
		self.inpID = inpID
		self.properlink = self.lin1 + str(self.inpID)
		self.r = requests.get(self.properlink)
		print(self.properlink)
		soup = BeautifulSoup(self.r.content, 'html.parser')
		print(soup.find_all(class_='paragraph--component -small -white mt-4'))

f = InPost()
f.genProperlink(2222)
