import numpy as np
import cv2 as cv


class MazeSolver:
	def __init__(self):
		self.img = cv.imread('mazes/maze.png')
		self.posX, self.posY = 167, 318
		self.pathX,self.pathY = [], []
		self.sensors = [[False, False],[False, False]]
		#self.sensors = [[up, down], [right, left]]
		self.lastdir = 3


	def pathing(self):
		self.directions()
		self.sensorcheck()
		if (self.sensors[0][0] == True and any(self.sensors[1]) == False or
			(any(self.sensors[0]) == False and any(self.sensors[1]) == False and
			self.lastdir == 2) or self.sensors[0][0] == True and self.sensors[1][0] == True):
			while int(list(self.up)[2]) + int(list(self.left)[2]) == 255:
				self.posX -= 1
				self.updatepath()
				self.sensorcheck()
			if any(self.sensors[0]) == False and any(self.sensors[1]) == False:
				self.posX -= 1
				self.updatepath()
				self.sensorcheck()
			self.lastdir = 4
		elif (self.sensors[0][1] == True and any(self.sensors[1]) == False or
			(any(self.sensors[0]) == False and any(self.sensors[1]) == False and
			self.lastdir == 1) or self.sensors[0][1] == True and self.sensors[1][1] == True):
			while int(list(self.down)[2]) + int(list(self.right)[2]) == 255:
				self.posX += 1
				self.updatepath()
				self.sensorcheck()
			if any(self.sensors[0]) == False and any(self.sensors[1]) == False:
				self.posX += 1
				self.updatepath()
				self.sensorcheck()
			self.lastdir = 3
		elif (self.sensors[1][0] == True and any(self.sensors[0]) == False or
			(any(self.sensors[0]) == False and any(self.sensors[1]) == False and
			self.lastdir == 4) or self.sensors[0][1] == True and self.sensors[1][0] == True):
			while int(list(self.right)[2]) + int(list(self.up)[2]) == 255:
				self.posY -= 1
				self.updatepath()
				self.sensorcheck()
			if any(self.sensors[0]) == False and any(self.sensors[1]) == False:
				self.posY -= 1
				self.updatepath()
				self.sensorcheck()
			self.lastdir = 1
		elif (self.sensors[1][1] == True and any(self.sensors[0]) == False or 
			(any(self.sensors[0]) == False and any(self.sensors[1]) == False and
			self.lastdir == 3) or self.sensors[0][0] == True and self.sensors[1][1] == True):
			while int(list(self.left)[2]) + int(list(self.down)[2]) == 255:
				self.updatepath()
				self.posY += 1
				self.sensorcheck()
			if any(self.sensors[0]) == False and any(self.sensors[1]) == False:
				self.posY += 1
				self.updatepath()
				self.sensorcheck()
			self.lastdir = 2

	def directions(self):
		self.up = list(self.img[self.posY-1, self.posX])
		self.down = list(self.img[self.posY+1, self.posX])
		self.right = list(self.img[self.posY, self.posX+1])
		self.left = list(self.img[self.posY, self.posX-1])
		self.alldirs = [[self.up, self.down], [self.right, self.left]]

	def sensorcheck(self):
		self.directions()
		for ind, val in enumerate(self.alldirs):
			for ind2, val2 in enumerate(val):
				if val2[2] == 0:
					self.sensors[ind][ind2] = True
				else:
					self.sensors[ind][ind2] = False
		print(self.sensors)



	def updatepath(self):
		self.pathX.append(self.posX)
		self.pathY.append(self.posY)

	def path(self):
		self.directions()
		while self.right[2] == 255:
			self.posX += 1
			self.updatepath()
			self.sensorcheck()
		self.sensorcheck()
		while self.left != [0, 0, 255]:
			self.pathing()

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
