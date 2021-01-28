import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QPainter, QColor, QPen
from PySide2.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(200,200,1000,500)
        self.setWindowTitle("mouse")
        self.label = QLabel(self)
        self.label.resize(500,40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self,event):
        distance_from_center = round(((event.y()-250)**2 + (event.x() -500)**2)**0.5)

        self.label.setText('坐标:(x: %d,y: %d)' % (event.x().event.y()) + "离中心点距离:" + str(distance_from_center))

        self.pos = event.pos()
        self.updata()

    def paintEvent(self, event):
        if self.pos:
            q = QPainter(self)
            q.drawLine(0,0,delf.pos.x(),self.pos.y())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
