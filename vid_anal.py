import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Writer:
	def __init__(self, img, tmp):
		self.img = cv.imread(img)
		self.img_gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
		self.tmp = cv.imread(tmp, 0)
		self.w, self.h = self.tmp.shape[:2]


	def analyse(self):
		res = cv.matchTemplate(self.img_gray, self.tmp, cv.TM_CCOEFF_NORMED)
		threshold = 0.8
		loc = np.where( res >= threshold)
		for pt in zip(*loc[::-1]):
			cv.putText(self.img, 'Nigga', (pt[0], pt[1] - 5), cv.FONT_HERSHEY_SIMPLEX, .75, (0, 255, 255), 2)
			cv.rectangle(self.img, pt, (pt[0] + self.w, pt[1] + self.h), (0,0,255), 2)
		cv.imwrite('msg_data/vid_anal/render.jpg', self.img)


def main():
	#w = Writer('msg_data/vid_anal/texttest.jpg', 'msg_data/vid_anal/word_icon.jpg')
	#w.analyse()


if __name__ == '__main__':
	main()
