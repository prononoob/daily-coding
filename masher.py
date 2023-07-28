from numpy import full, uint8
from cv2 import imread, imwrite
from random import randint
from os import listdir
from abc import ABC, abstractmethod


class MixingStrategy(ABC):
    @abstractmethod
    def mixPixels(self, analyserInstance: 'ImageAnalyser'):
        pass

class RandomMixingStrategy(MixingStrategy):
    def mixPixels(self, analyserInstance: 'ImageAnalyser'):
        self.analyserInstance = analyserInstance
        for height in range(self.analyserInstance.maxHeight):
            print('Progress:', round(height/(self.analyserInstance.maxHeight)*100, 1), '%')
            for width in range(self.analyserInstance.maxWidth):
                self.randomIMG = randint(0, self.analyserInstance.numberOfImages-1)
                if height < len(self.analyserInstance.files[self.randomIMG]) and width < len(self.analyserInstance.files[self.randomIMG][0]):
                    self.analyserInstance.result[height][width] = self.analyserInstance.files[self.randomIMG][height][width]

class CheckerMixingStrategy(MixingStrategy):
    def mixPixels(self, analyserInstance: 'ImageAnalyser'):
        self.analyserInstance = analyserInstance
        self.currentImg = 0
        self.firstPXofRow = 0
        self.firstPass = True
        for height in range(self.analyserInstance.maxHeight):
            if self.firstPass:
                self.firstPass = False
            else:
                if self.currentImg == self.firstPXofRow:
                    self.incrementCurrentImg()
                    self.firstPXofRow = self.currentImg
                else:
                    self.firstPXofRow = self.currentImg
            print('Progress:', round(height/(self.analyserInstance.maxHeight)*100, 1), '%')
            for width in range(self.analyserInstance.maxWidth):
                if height < len(self.analyserInstance.files[self.currentImg]) and width < len(self.analyserInstance.files[self.currentImg][0]):
                    self.analyserInstance.result[height][width] = self.analyserInstance.files[self.currentImg][height][width]
                self.incrementCurrentImg()
    
    def incrementCurrentImg(self):
        if self.currentImg >= self.analyserInstance.numberOfImages-1:
            self.currentImg = 0
        else:
            self.currentImg += 1


class ImageAnalyser:
    def __init__(self):
        self.inputPath = ''
        self.outputPath = ''
        self.files = []
        self.numberOfImages = int()
        self.maxWidth, self.maxHeight = 0, 0
        self.strategy = RandomMixingStrategy()
    
    def setInputPath(self, inputPath:str):
        self.inputPath = inputPath
    
    def setOutputPath(self, outputPath:str):
        self.outputPath = outputPath
    
    def getPaths(self) -> dict:
        return {'inputPath':self.inputPath, 'outputPath':self.outputPath}
    
    def setMixingStrategy(self, strategy: MixingStrategy):
        self.strategy = strategy
    
    def makeFileList(self):
        for file in listdir(self.inputPath):
            self.files.append(imread(str(self.inputPath+file)))
        self.numberOfImages = len(self.files)
    
    def findMaxes(self):
        for file in self.files:
            if len(file) > self.maxHeight:
                self.maxHeight = len(file)
            if len(file[0]) > self.maxWidth:
                self.maxWidth = len(file[0])
        
    def makeBlankImage(self):
        self.result = full((self.maxHeight, self.maxWidth, 3), 255, uint8)

    def performMixingStrategy(self):
        self.strategy.mixPixels(self)
    
    def finalizeImage(self):
        imwrite(self.outputPath+'result.png', self.result)

    def mix(self):
        if self.inputPath and self.outputPath:
            self.makeFileList()
            self.findMaxes()
            self.makeBlankImage()
            self.performMixingStrategy()
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
    #i.setMixingStrategy(CheckerMixingStrategy())
    i.mix()

if __name__ == '__main__':
    main()
