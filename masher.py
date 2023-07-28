from numpy import full, uint8
from cv2 import imread, imwrite
from random import randint
from os import listdir


class ImageAnalyser:
    def __init__(self):
        self.inputPath = ''
        self.outputPath = ''
        self.files = []
        self.numberOfImages = int()
        self.maxWidth, self.maxHeigth = 0, 0
    
    def setInputPath(self, inputPath:str):
        self.inputPath = inputPath
    
    def setOutputPath(self, outputPath:str):
        self.outputPath = outputPath
    
    def getPaths(self) -> dict:
        return {'inputPath':self.inputPath, 'outputPath':self.outputPath}
    
    def makeFileList(self):
        for file in listdir(self.inputPath):
            self.files.append(imread(str(self.inputPath+file)))
        self.numberOfImages = len(self.files)
    
    def findMaxes(self):
        for file in self.files:
            if len(file) > self.maxHeigth:
                self.maxHeigth = len(file)
            if len(file[0]) > self.maxWidth:
                self.maxWidth = len(file[0])
        
    def makeBlankImage(self):
        self.result = full((self.maxHeigth, self.maxWidth, 3), 255, uint8)

    def mixPixels(self):
        for height in range(self.maxHeigth):
            print('Progress:', round(height/(self.maxHeigth)*100, 1), '%')
            for width in range(self.maxWidth):
                self.randomIMG = randint(0, self.numberOfImages-1)
                if height < len(self.files[self.randomIMG]) and width < len(self.files[self.randomIMG][0]):
                    self.result[height][width] = self.files[self.randomIMG][height][width]
    
    def finalizeImage(self):
        imwrite(self.outputPath+'result.png', self.result)

    def mix(self):
        if self.inputPath and self.outputPath:
            self.makeFileList()
            self.findMaxes()
            self.makeBlankImage()
            self.mixPixels()
            self.finalizeImage()
        else:
            if not self.inputPath:
                print('[WARNING] No input path specified, use setInputPath() method')
            if not self.outputPath:
                print('[WARNING] No output path specified, use setOutputPath() method')



def main():
    i = ImageAnalyser()
    #i.setInputPath('input/path')
    #i.setOutputPath('output/path')
    i.mix()

if __name__ == '__main__':
    main()
