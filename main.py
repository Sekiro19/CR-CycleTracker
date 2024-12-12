import sys
import time
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import numpy as np
from bin import *



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.howToUse = Ui_Form()
        self.howToUse.setupUi(self.howToUse)
        self.howToUse.setWindowTitle('How To Use')
        self.threadPool = QThreadPool()
        self.screenHandler = ScreenHandler()
        self.mystery = QPixmap(r":/all/bin/images/mystery.png")
        
        self.ui.btn_start.setEnabled(False)
        self.ui.btn_setup.setEnabled(True)
        
        self.ui.btn_howToUse.clicked.connect(self.howToUse.show)
        self.ui.btn_setup.clicked.connect(self.showSelectionBox)
        self.ui.btn_start.clicked.connect(self.start)
        self.screenHandler.signals.img.connect(lambda img: self.ui.screenBar.setPixmap(QPixmap.fromImage(img)))
        self.screenHandler.signals.fps.connect(lambda fps: self.ui.fps.setText('FPS:'+str(int(fps))))
        self.screenHandler.signals.updateCards.connect(self.updateCards)
        self.show()


    def updateCards(self):
        for i in range(8):
            if isinstance(self.screenHandler.cards[i], tuple):
                card = self.screenHandler.cards[i][1]
                qimage = self.screenHandler.arrayToQimage(np.require(card, np.uint8, 'C'))  
                self.ui.screen.findChild(QLabel, f"c{i}").setPixmap(QPixmap.fromImage(qimage))
            else:
                self.ui.screen.findChild(QLabel, f"c{i}").setPixmap(self.mystery)

    def setupSettings(self, region):
        x, y, w, h = region
        if w<0 and h<0:
            region = x+w, y+h, -w, -h
        elif w<0 and h>=0:
            region = x+w, y, -w, h
        elif w>=0 and h<0:
            region = x, y+h, w, -h
        self.screenHandler.region = region
        r = self.screenHandler.setRules()    
        self.selectionBox.close()
        if r:
            self.ui.btn_start.setEnabled(True)
        else:
            QMessageBox.critical(self, "wrong area selected", "I can't locate the cards!", buttons=QMessageBox.Ok)

    
    def start(self):
        if self.screenHandler.recordingState:
            self.ui.btn_setup.setEnabled(True)
            self.screenHandler.recordingState = False
            self.ui.btn_start.setStyleSheet(self.ui.btn_start.styleSheet().replace("rgb(189, 255, 0);", "rgb(233, 12, 89);"))
            self.ui.btn_start.setText("Start")
            self.ui.fps.setText('FPS:0')
            self.screenHandler.cards = np.zeros(8, dtype=np.dtype)
            self.ui.editFps.setEnabled(True)
            self.ui.toggleFps.setEnabled(True)
        else:
            if self.ui.toggleFps.isChecked():
                try:
                    fps = int(float(self.ui.editFps.text()))
                    self.screenHandler.fpsThresh = fps
                except ValueError:
                    self.screenHandler.fpsThresh = 240
            else:
                self.screenHandler.fpsThresh = 240
            worker = Worker(self.screenHandler.startRecording)
            self.threadPool.start(worker)
            self.ui.btn_start.setStyleSheet(self.ui.btn_start.styleSheet().replace("rgb(233, 12, 89);", "rgb(189, 255, 0);"))
            self.ui.btn_start.setText("Stop")
            self.ui.editFps.setEnabled(False)
            self.ui.toggleFps.setEnabled(False)
            self.ui.btn_setup.setEnabled(False)
            
        time.sleep(1)
        self.ui.screenBar.clear()
        for i in range(8):
            self.ui.screen.findChild(QLabel, f"c{i}").clear()


    def showSelectionBox(self):
        self.selectionBox = SelectionBox()
        self.selectionBox.showMaximized()
        self.selectionBox.signals.region.connect(lambda region: self.setupSettings(region))

    def closeEvent(self, event: QCloseEvent) -> None:  # handle close window
        msg = QMessageBox.question(self,
                                   "Close",
                                   "Close the app ?",
                                   QMessageBox.Yes, QMessageBox.No)
        if msg == QMessageBox.Yes:
            # stop running threads
            self.screenHandler.recordingState = False
            time.sleep(.2)
            event.accept()
        else:
            event.ignore()

    @staticmethod
    def triggerloadingAnimation(animation: QMovie, btn: QPushButton, start: bool):
        animation.frameChanged.connect(lambda: btn.setIcon(animation.currentPixmap()))
        if start:
            btn.setEnabled(False)
            animation.start()
        else:
            btn.setEnabled(True)
            animation.stop()
            btn.setIcon(QIcon())
            del animation

if __name__ == "__main__":
    app = QApplication()
    app.setApplicationVersion('v1.1 (64-bit)')
    app.setWindowIcon(QIcon(r':/all/bin/images/gob.png'))
    window = MainWindow()
    window.setWindowTitle('CR-Cycle Tracker v1.1')
    sys.exit(app.exec())