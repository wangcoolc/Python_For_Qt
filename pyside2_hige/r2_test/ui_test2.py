import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from math import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
       self.setWindowTitle("ui 绘制")
       self.setGeometry(300,300,500,500)

       self.show()

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.begin(self)

        self.drawText1(event,painter)
        self.drawText2(event,painter)
        self.drawText3(event,painter)
        self.drawText4(event,painter)
        painter.end() 

    def drawText1(self,event,qp):
        qp.save()
        radius=100
        r = radius
        qp.setPen(Qt.NoPen)
	
        rtF = QRectF(500,500,r*2,r*2)
        rtF.moveCenter(self.rect().center())
        qp.setBrush(QColor(172, 172, 172))
        qp.drawEllipse(rtF)

        b = 90
        rtF1 = QRectF(500,500,b*2,b*2)
        rtF1.moveCenter(self.rect().center())
        qp.setBrush(QColor(40, 40, 40))
        qp.setPen(Qt.NoPen)
        qp.drawEllipse(rtF1)

        qp.restore()

    def drawText2(self,event,qp):
        r = 85
        lineWidth = 1
        angle = 60
        qp.save()
        qp.translate(250,250)
        qp.rotate(angle)

        a = (360-(angle*2)) / 100

        for i in range(100):
            color = QColor(84, 84, 84)
            if i > 80:
                color = QColor(250, 0, 0)

            if (i % 10) == 0:
                qp.setPen(QPen(color, 1.3*lineWidth))
                qp.drawLine(0, r, 0, r / 1.2)
            elif ((i % 2) == 0):
                qp.setPen(QPen(color, 1*lineWidth))
                qp.drawLine(0, r, 0, r / 1.1)
            
            qp.rotate(a)

        qp.restore()

    def drawText3(self,event,qp):
        qp.save()
        qp.translate(250,250)
        poitns = [QPoint(0, -2), QPoint(0, 2), QPoint(60, 0)]
        pts = QPolygon(poitns)
        
        c = 60
        Angle = 60
        degRotate =Angle +  (360.0 - Angle - Angle) / 100 * 68

        qp.rotate(degRotate)
        #辐射渐变，内部填充颜色
        haloGradient = QRadialGradient(0, 0, 60, 0, 0)
        haloGradient.setColorAt(0, QColor(100, 100, 100))
        haloGradient.setColorAt(1, QColor(250, 50, 50)); #red
        qp.setPen(QColor(250, 150, 150)); # 边框颜色
        qp.setBrush(haloGradient)
        qp.drawConvexPolygon(pts)

        #画中心圆圈
        radial = QRadialGradient(0, 0, 14)  #渐变
        radial.setColorAt(0.0, QColor(100, 100, 100))
        radial.setColorAt(1.0, QColor(250, 50, 50))
        qp.setPen(Qt.NoPen);  #填满没有边界
        qp.setBrush(radial)
        qp.drawEllipse(-7, -7, 14, 14)

        qp.restore()

    def drawText4(self,event,qp):
        qp.save()
        qp.translate(250,250)
        r = 60
        qp.setFont(QFont("Arial", 10))
        qp.setPen(QPen(QColor(255,255,255)))

        fm = QFontMetricsF(qp.font())
        gap = (360-60*2) / 10

        for i in range(11):
            angle = 90+60+gap*i  #角度,10格子画一个刻度值

            angleArc =( angle % 360) * 3.14 / 180 # 转换为弧度
            x = (r)*cos(angleArc)
            y = (r)*sin(angleArc)

            # value = string()
            # value.number(i*100)
            strvalue = str(int(i*10))
            w = fm.width(strvalue)
            h = fm.height()
            x = x - w/2
            y = y + h/4
            qp.drawText(QPointF(x, y),strvalue)

        qp.restore()

        # qp.save()
        # satrt = 150
        # end = 60
        # qp.translate(250,250)
        # qp.setPen(QPen(QColor(255,255,255)))
        # startRad = satrt * (3.14 / 180)
        # stepRad = (360-(satrt-end)) * (3.14 / 180) / 10
 
        # fm = QFontMetricsF(qp.font())
        # for i in range(0, 11):
        #     sina = sin(startRad + i*stepRad)
        #     cosa = cos(startRad + i*stepRad)
 
        #     tmpVal = i*((100-0)/10) + 0
        #     tmpVal = tmpVal / 100
        #     s = '{:.0f}'.format(tmpVal)
        #     w = fm.size(Qt.TextSingleLine, s).width()
        #     h = fm.size(Qt.TextSingleLine, s).height()
        #     x = 80*cosa - w/2
        #     y = 80*sina - h/2
        #     qp.drawText(QRectF(x, y, w, h), s)
         
        # qp.restore()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
