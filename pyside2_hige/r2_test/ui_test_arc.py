import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
       self.setWindowTitle("ui 绘制")

       self.show()

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.begin(self)

        self.drawText1(event,painter)
        self.drawText2(event,painter)
        painter.end() 


    def drawText1(self,event,qp):
        qp.save()
    
        qp.setPen(Qt.NoPen)
	
        rtF = QRectF(500,500,500,500)
        rtF.moveCenter(self.rect().center())
        qp.setBrush(QColor(172, 172, 172))
        qp.drawEllipse(rtF)


        qp.restore()
    def drawText2(self,event,qp):
        qp.save()
        qp.setBrush(QColor(10,10,10))
        rect = QRectF(-90,-90,180,180)
        path = QPainterPath()
        path.arcTo(rect,0,360)
        subpath = QPainterPath()
        subpath.addEllipse(-76,-76,152,152)
        path=path-subpath
        qp.setPen(QColor(168,34,3))
        qp.drawPath(path);

        qp.restore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()