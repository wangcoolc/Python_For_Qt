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
        # self.drawText3(event,painter)
        painter.end() 


    def drawText1(self,event,qp):
        qp.save()
        radius=100

        lgl = QLinearGradient(0,radius,0,-radius)
        lgl.setColorAt(0,QColor(24,24,24))
        lgl.setColorAt(1,QColor(150,150,150))

        qp.setBrush(lgl)
        qp.setPen(QColor(168,34,3))
        #画整个大圆
        qp.drawEllipse(-92,-92,184,184)

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

    # def drawText3(self,event,qp):
    #     qp.save()
    #     qp.setPen(m_foreground)
    #     startRad=(270-m_startAngle)*(3.14/180);
    #     deltaRad=(360-m_startAngle-m_endAngle)*(3.14/180)/m_scaleMajor;
    #     sina,cosa;
    #     int x,y;

    #     font = QFont("Bahnschrift", 8, 50)
    #     fm = QFontMetricsF(font)
    #     qp.setFont(font)

    #     str = QString()

    #     for 





       


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()