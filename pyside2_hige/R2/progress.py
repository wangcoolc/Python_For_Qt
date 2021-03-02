import sys, random ,math
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class ProgressBar(QWidget):
    # 浪高百分比
    waterHeight = 1
    # 密度
    waterDensity = 1
    # 样式1为矩形, 0为圆形
    styleType = 1
    # 文字颜色
    textColor = Qt.white
    # 背景颜色
    backgroundColor = Qt.gray
    # 波浪颜色1
    waterColor1 = QColor(33, 178, 148)
    # 波浪颜色2
    waterColor2 = QColor(33, 178, 148, 100)

    def __init__(self, *args, **kwargs):
        super(ProgressBar, self).__init__(*args, **kwargs)
        self._offset = 0
        # 每隔100ms刷新波浪（模拟波浪动态
    
    

    



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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    app.exec_()