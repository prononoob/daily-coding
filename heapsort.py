from time import sleep


class Sorting:
	def __init__(self, array):
		self.array = array
		#self.array.insert(0, 'bruh')
		self.heapSize = len(self.array)
		self.oml = []

	def heapify(self, array):
		#self.oml = []
		self.heapSize = len(array)
		#print(array, self.array)
		#self.array = array
		self.cur = self.heapSize-1
		for ind, val in enumerate(array):
			while array[self.cur] > array[int((self.cur+1)/2)-1] and self.cur>0:
				array[self.cur], array[int((self.cur+1)/2)-1] = array[int((self.cur+1)/2)-1], array[self.cur]
				self.cur = int((self.cur+1)/2)-1
			self.heapSize -= 1
			self.cur = self.heapSize - 1
		array[0], array[-1] = array[-1], array[0]
		if len(array) > 1:
			self.oml.insert(0, array[-1])
			sleep(.2)
			for i in array[:-1]:
				print('|'*i)
			for i in self.oml:
				print('|'*i)
			print(array[:-1], self.oml, '\n\n')
			self.heapify(array[:-1])
			#self.heapify(array[:-1])
		#self.array.append(array[-1])


if __name__ == '__main__':
	#sorting = Sorting([3,7,8,5,2])
	sorting = Sorting([31, 7, 43, 92, 3, 35, 100, 84, 80, 119, 143, 142, 45, 108, 26, 150, 38, 66, 23, 127, 74, 14, 65, 37, 61, 118, 94, 11, 54, 24, 34, 78])
	sorting.heapify(sorting.array)
	#sorting.heapsort()
