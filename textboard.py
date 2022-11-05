class Board:
	def __init__(self):
		self.catalog = {}
		self.idCounter = 0
		print('Class initialized!')

	def create(self, title):
		self.title = title
		self.catalog[self.idCounter] = self.title
		self.idCounter += 1

	def show(self, amount = 0):
		if amount >= len(self.catalog):
			self.amount = len(self.catalog)
		else:
			self.amount = amount
		print('----------')
		if self.amount:
			for i in range(self.amount):
				print(f'ID: {i} Title: {self.catalog[i]}')
		else:
			for i in self.catalog:
				print(f'ID: {i} Title: {self.catalog[i]}')
		# print('----------')

	def delete(self, threadID):
		pass


class Thread:
	def __init__(self):
		pass


board = Board()
board.create('Thread 1')
board.create('Thread 2')
board.create('Thread 3')
board.show()
board.show(4)
board.show(2)