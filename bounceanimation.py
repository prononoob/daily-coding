from time import sleep
from os import system


class Objects:
	def __init__(self):
		self.room = []
		self.roomX, self.roomY, self.temprow = 7, 10, []
		for xi in range(self.roomX):
			self.temprow.append(' ')
		for yi in range(self.roomY):
			self.room.append(self.temprow[:])
		self.ball = 'O'
		self.x, self.y = 0, 1
		self.maxy, self.maxx = len(self.room)-1, len(self.room[0])-1
		self.xdir, self.ydir = True, True

class Animation:
	def __init__(self):
		objs = Objects()
		print(objs.x, objs.y)
		objs.room[objs.y][objs.x] = objs.ball
		system('clear')
		for obj in objs.room:
			print(obj)
		for i in range(100):
			sleep(.2)
			if objs.x == objs.maxx and objs.xdir == True or objs.x == 0 and objs.xdir == False:
				objs.xdir = not objs.xdir
			if objs.y == objs.maxy and objs.ydir == False or objs.y == 0 and objs.ydir ==True:
				objs.ydir = not objs.ydir
			objs.room[objs.y][objs.x] = ' '
			if objs.xdir == True:
				objs.x += 1
			else:
				objs.x -= 1
			if objs.ydir == True:
				objs.y -= 1
			else:
				objs.y += 1
			objs.room[objs.y][objs.x] = objs.ball
			system('clear')
			for obj in objs.room:
				print(obj)


def main():
	anim = Animation()

if __name__	== '__main__':
	main()
