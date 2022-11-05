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
				if self.catalog[i]:
					print(f'ID: {i} Title: {self.catalog[i]}')
		else:
			for i in self.catalog:
				if self.catalog[i]:
					print(f'ID: {i} Title: {self.catalog[i]}')

	def delete(self, threadID):
		self.threadID = threadID
		if self.threadID in self.catalog:
			self.catalog[self.threadID] = False


class Thread:
	def __init__(self, board):
		self.board = board
		self.replies = {}
		self.replyID = 0

	def reply(self, threadID, replyMsg):
		self.threadID = threadID
		self.replyMsg = replyMsg
		self.replies[self.replyID] = [self.threadID, self.replyMsg]
		self.replyID += 1

	def showReplies(self, threadID):
		self.threadID = threadID
		print('----------')
		print(self.board.catalog[threadID])
		for i in self.replies:
			if self.replies[i][0] == self.threadID:
				print(f'    Reply {i}: {self.replies[i][1]}')


if __name__ == '__main__':
	board = Board()
	board.create('Thread 1')
	board.create('Thread 2')
	board.create('Thread 3')
	board.show()
	thread = Thread(board=board)
	thread.reply(0, 'Reply 1')
	thread.reply(0, 'Reply 2')
	thread.showReplies(0)