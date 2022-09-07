import numpy as np
import cv2 as cv
from time import sleep


class MazeSolver:
	def __init__(self):
		self.img = cv.imread('mazes/maze.png')
		self.posX, self.posY = 167, 318
		self.pathX,self.pathY = [], []

	def pathing(self, dire):
		self.dire = dire
		self.directions()
		while self.dire[2] == 255:
			print(self.posX, self.posY)
			sleep(.1)
			self.updatepath()
			if self.dire == self.up:
				self.posY -= 1
				print(1)
			elif self.dire == self.down:
				self.posY += 1
				print(2)
			elif self.dire == self.right:
				self.posX += 1
			elif self.dire == self.left:
				self.posX -= 1
			self.directions()


	def directions(self):
		self.up = list(self.img[self.posY-1, self.posX])
		self.down = list(self.img[self.posY+1, self.posX])
		self.right = list(self.img[self.posY, self.posX+1])
		self.left = list(self.img[self.posY, self.posX+-1])

	def updatepath(self):
		self.pathX.append(self.posX)
		self.pathY.append(self.posY)

	def path(self):
		self.directions()
		while int(list(self.img[self.posY, self.posX+1])[2]) + int(list(self.img[self.posY-1, self.posX])[2]) != 0:
			print(int(list(self.img[self.posY, self.posX+1])[2]) + int(list(self.img[self.posY-1, self.posX])[2]))
			self.pathing(self.right)
			self.pathing(self.up)
		#while True:
			#self.directions()
			#if self.up[2] == 0 and self.right[2] == 0:
				#self.pathingW()



	def drawing(self):
		for ind, val in enumerate(self.pathX):
			self.img[self.pathY[ind], val] = [0, 255, 0]
		cv.imwrite('mazes/render.png', self.img)

def main():
	solver = MazeSolver()
	solver.path()
	solver.drawing()

if __name__ == '__main__':
	main()
