import os
import time
import numpy as np
import cv2
from .grabScreen import grab_screen
from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QImage
import traceback

class ImageSignals(QObject):
    img = Signal(QImage)
    fps = Signal(float)
    updateCards = Signal()
    
class ScreenHandler:
    def __init__(self) -> None:
        self.signals = ImageSignals()
        self.recordingState = False
        self.region = None
        self.fpsThresh = 240
        self.prevFrame = np.zeros(8, dtype=np.dtype)
        self.rowSplit = None
        self.prevXpos = np.zeros(4, dtype=int)
        self.cards = np.zeros(8, dtype=np.dtype)  # (X, ndarr)
        self.cardsPos = np.zeros(8, dtype=np.dtype)  # (X, ndarr)
        self.D = 15
        self.temp = cv2.imread(os.getcwd()+r"\bin\images\mcard.PNG", 0)
        
        
    def setRules(self) -> bool:
        image = cv2.cvtColor(grab_screen(self.region), cv2.COLOR_RGBA2RGB)
        row, _, _ = image.shape
        self.rowSplit = int(row/3)
        cards = image[self.rowSplit:, :]
        w, h = self.temp.shape[::-1]
        cardsGRAY = cv2.cvtColor(cards, cv2.COLOR_RGBA2GRAY)
        try:
            res = cv2.matchTemplate(cardsGRAY, self.temp, cv2.TM_CCOEFF_NORMED)
        except cv2.error:
            return False  # temp size > image size
        threshold = .8
        th = 3
        loc = np.where(res >= threshold)
        x = np.unique(loc[::-1][0])
        x = np.delete(x, np.argwhere(np.ediff1d(x) < th) + 1)
        if x.size == 8:
            y = loc[::-1][1][:8]
            for i in range(8):
                self.cardsPos[i] = (y[i], y[i]+h, x[i], x[i]+w)
            return True
        else:
            return False
        
        
    def shiftArray(self, arr) -> np.ndarray:
        '''it literlly it dose this: [4 5 6] -> [5 6 -1]'''
        result = np.empty_like(arr)
        result[-1:] = -1
        result[:-1] = arr[1:]
        return result
        
    def trackCycle(self, x):
        '''4 Card Cycle only'''
        for i in range(4):
            if isinstance(self.cards[i], tuple):
                xMin = self.cards[i][0]
                if (x == xMin):  # if the drawn card is in my hand
                    self.cards[i] = self.cards[4]  # replace it whith the closest card to my hand
                    self.cards[4] = -1  # empty the space of the closest card to my hand
                    # shift last 3 cards
                    result = np.zeros(4, dtype=np.dtype)
                    result[-1] = -1
                    result[:3] = self.cards[5:]
                    self.cards[4:] = result
                    return
        self.cards = self.shiftArray(self.cards)
        

    def arrayToQimage(self, image: np.ndarray) -> QImage:
        h, w, ch = image.shape
        bytesPerLine = ch * w
        return QImage(image.data, w, h, bytesPerLine, QImage.Format_BGR888)
    
    def startRecording(self):
        self.prevFrame = np.zeros(8, dtype=np.dtype)
        self.recordingState = True  # ready for processing
        prevTime = 0
        while self.recordingState:
            startTime = time.time()-prevTime
            if startTime > 1./self.fpsThresh:
                prevTime = time.time()
                image = grab_screen(self.region)
                image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
                bar, cards = image[:self.rowSplit, :], image[self.rowSplit:, :]
                self.processImage(cards)
                self.signals.img.emit(self.arrayToQimage(bar))
                fps = 1.0 / (startTime)
                self.signals.fps.emit(fps)

                if (cv2.waitKey(1) & 0xFF) == ord('q'):
                    cv2.destroyAllWindows()
                    break

    def processImage(self, image):
        imageGray = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
        for i in range(8):
            yMin, yMax, xMin, xMax = self.cardsPos[i]
            cardGRAY = imageGray[yMin:yMax, xMin:xMax]
            if not isinstance(self.prevFrame[i], np.ndarray):
                self.prevFrame[i] = cardGRAY
                return
            frameDelta = cv2.absdiff(self.prevFrame[i], cardGRAY)
            thresh = cv2.threshold(frameDelta, 30, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for c in cnts:
                cArea = cv2.contourArea(c)
                if cArea > 2000:
                    if not (self.prevXpos == xMin).any():  # prevent taking multiple screenShots of 1 card motion
                        card = image[yMin:yMax, xMin:xMax]
                        self.trackCycle(xMin)
                        self.cards[-1] = (xMin, card)
                        self.signals.updateCards.emit()
                    self.prevXpos = self.shiftArray(self.prevXpos)
                    self.prevXpos[-1] = xMin
            self.prevFrame[i] = cardGRAY
    
