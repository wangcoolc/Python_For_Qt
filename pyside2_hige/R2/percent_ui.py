import sys, random
import cgitb
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Percent(QWidget):

    MinValue = 0
    MaxValue = 100
    Value = 0
    BorderWidth = 8
    Clockwise = True  # 顺时针还是逆时针
    ShowPercent = True  # 是否显示百分比
    ShowFreeArea = False  # 显示背后剩余
    ShowSmallCircle = False  # 显示带头的小圆圈
    TextColor = QColor(255, 255, 255)  # 文字颜色
    BorderColor = QColor(24, 189, 155)  # 边框圆圈颜色
    BackgroundColor = QColor(70, 70, 70)  # 背景颜色


    def __init__(self, *args, value=0, minValue=0, maxValue=100,
                 borderWidth=8, clockwise=True, showPercent=True,
                 showFreeArea=False, showSmallCircle=False,
                 textColor=QColor(255, 255, 255),
                 borderColor=QColor(24, 189, 155),
                 backgroundColor=QColor(70, 70, 70), **kwargs):
        super().__init__()
        self.Value = value
        self.MinValue = minValue
        self.MaxValue = maxValue
        self.BorderWidth = borderWidth
        self.Clockwise = clockwise
        self.ShowPercent = showPercent
        self.ShowFreeArea = showFreeArea
        self.ShowSmallCircle = showSmallCircle
        self.TextColor = textColor
        self.BorderColor = borderColor
        self.BackgroundColor = backgroundColor
    
        self.setWindowTitle("R2框架")

    def paintEvent(self,event):
        width = self.width()
        height = self.height()
        side = min(width, height)
        painter = QPainter(self)

         # 反锯齿
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.TextAntialiasing)
        # 坐标中心为中间点
        painter.translate(width / 2, height / 2)

         # 按照100x100缩放
        painter.scale(side / 100.0, side / 100.0)

        painter.begin(self)

        #绘制中心圆
        self.drawCircle(event,painter)
        # #绘制圆弧
        self.drawArc(event,painter)
        # #绘制文字
        self.drawText(event,painter)
        painter.end()


    def drawCircle(self,event,painter):
        # 绘制中心圆
        radius = 50
        radius = radius - self.BorderWidth
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.BackgroundColor)
        painter.drawEllipse(QRectF(-radius, -radius, radius * 2, radius * 2))
        painter.restore()

    def drawArc(self,event,painter):
        # 绘制圆弧
        radius = 50 - self.BorderWidth / 2
        painter.save()
        painter.setBrush(Qt.NoBrush)
        # 修改画笔
        pen = painter.pen()
        pen.setWidthF(self.BorderWidth)
        pen.setCapStyle(Qt.RoundCap)

        arcLength = 360.0 / (self.MaxValue - self.MinValue) * self.Value
        rect = QRectF(-radius, -radius, radius * 2, radius * 2)

        if not self.Clockwise:
            # 逆时针
            arcLength = -arcLength

        # 绘制剩余进度圆弧
        if self.ShowFreeArea:
            acolor = self.BorderColor.toRgb()
            acolor.setAlphaF(0.2)
            pen.setColor(acolor)
            painter.setPen(pen)
            painter.drawArc(rect, (0 - arcLength) *
                            16, -(360 - arcLength) * 16)

        # 绘制当前进度圆弧
        pen.setColor(self.BorderColor)
        painter.setPen(pen)
        painter.drawArc(rect, 0, -arcLength * 16)


        # 绘制进度圆弧前面的小圆
        if self.ShowSmallCircle:
            offset = radius - self.BorderWidth + 1
            radius = self.BorderWidth / 2 - 1
            painter.rotate(-90)
            circleRect = QRectF(-radius, radius + offset,
                                radius * 2, radius * 2)
            painter.rotate(arcLength)
            painter.drawEllipse(circleRect)

        painter.restore()


    def drawText(self,event,painter):
        radius = 50
        # 绘制文字
        painter.save()
        painter.setPen(self.TextColor)
        painter.setFont(QFont('Arial', 25))
        strValue = '{}%'.format(int(self.Value / (self.MaxValue - self.MinValue)
                                    * 100)) if self.ShowPercent else str(self.Value)
        painter.drawText(QRectF(-radius, -radius, radius * 2,
                                radius * 2), Qt.AlignCenter, strValue)
        painter.restore()



class MyThread1(QThread):
    sinOut1 = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            val = random.randint(1,100)
            print("vvv",val)
            self.sinOut1.emit(int(val))
            self.sleep(1)


class MyThread2(QThread):
    sinOut2 = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            val = random.randint(1,100)
            print("vvv",val)
            self.sinOut2.emit(int(val))
            self.sleep(1)


class MyThread3(QThread):
    sinOut3 = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            val = random.randint(1,100)
            print("vvv",val)
            self.sinOut3.emit(int(val))
            self.sleep(1)



class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,500,500)
        layout = QHBoxLayout(self)
        self._widgets = []
        self._widgets.append(Percent(self))
        layout.addWidget(self._widgets[0])
        self.thraed1 = MyThread1()
        self.thraed1.sinOut1.connect(self.Percent1display)
        self.thraed1.start()

        self._widgets.append(Percent(self))
        layout.addWidget(self._widgets[1])
        self.thraed2 = MyThread2()
        self.thraed2.sinOut2.connect(self.Percent2display)
        self.thraed2.start()

        self._widgets.append(Percent(self))
        layout.addWidget(self._widgets[2])
        self.thraed3 = MyThread3()
        self.thraed3.sinOut3.connect(self.Percent3display)
        self.thraed3.start()
    
    def Percent1display(self,val):
        self._widgets[0].Value = val
        self._widgets[0].update()

    def Percent2display(self,val):
        self._widgets[1].Value = val
        self._widgets[1].update()

    def Percent3display(self,val):
        self._widgets[2].Value = val
        self._widgets[2].update()

class mianwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        button1 = QPushButton()
        button1.setIcon(QIcon('1.png'))
        layout.addWidget(button1)

        button2 = QPushButton()
        button2.setIcon(QIcon('2.png'))
        layout.addWidget(button2)
        button2.clicked.connect(self.myshow)

        button3 = QPushButton()
        button3.setIcon(QIcon('3.png'))
        layout.addWidget(button3)

        button4 = QPushButton()
        button4.setIcon(QIcon('4.png'))
        layout.addWidget(button4)

        button5 = QPushButton()
        button5.setIcon(QIcon('5.png'))
        layout.addWidget(button5)

        self.setLayout(layout)

    def myshow(self):
        ex = Window()
        ex.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # w = mianwindow()
    # w.show()
    ex = Window()
    ex.show()
    app.exec_()