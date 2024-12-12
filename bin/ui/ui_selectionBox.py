from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class BoxSignals(QObject):
    region = Signal(tuple)
    
class SelectionBox(QWidget):
    def __init__(self, ) -> None:
        super().__init__()
        # self.setWindowFlag(Qt.Tool)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.5)       
        self.signals = BoxSignals()
        self.box = None 
        self.begin = QPoint()
        self.end = QPoint()
        
    def paintEvent(self, event):
        qp = QPainter(self)
        br = QBrush(QColor(100, 10, 10, 40))  
        qp.setBrush(br)
        self.box = QRect(self.begin, self.end)
        qp.drawRect(self.box)    

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        region = self.box.x(), self.box.y(), self.box.width(), self.box.height()
        self.signals.region.emit(region)