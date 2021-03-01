import sys, random
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("r2")
        self.resize(500,500)

        #全局布局
        wlayout = QHBoxLayout()

        #局部布局1
        vlayout1 = QVBoxLayout()
        label1 = QLabel()
        label1.setText("CPU Usage")
        vlayout1.addWidget(label1)
        self.lcdNumber1 = QLCDNumber()
        self.lcdNumber1.resize(50,50)
        vlayout1.addWidget(self.lcdNumber1)
        vwg1 = QWidget()
        vwg1.setLayout(vlayout1)
        self.thraed1 = MyThread1()
        self.thraed1.sinOut1.connect(self.lcd1display)
        self.thraed1.start()

        #局部布局2
        vlayout2 = QVBoxLayout()
        label2 = QLabel()
        label2.setText("RAM Usage")
        vlayout2.addWidget(label2)
        self.lcdNumber2 = QLCDNumber()
        self.lcdNumber2.resize(50,50)
        vlayout2.addWidget(self.lcdNumber2)
        vwg2 = QWidget()
        vwg2.setLayout(vlayout2)
        self.thraed2 = MyThread2()
        self.thraed2.sinOut2.connect(self.lcd2display)
        self.thraed2.start()

        #局部布局3
        vlayout3 = QVBoxLayout()
        label3 = QLabel()
        label3.setText("Storage Usage")
        vlayout3.addWidget(label3)
        self.lcdNumber3 = QLCDNumber()
        self.lcdNumber3.resize(50,50)
        vlayout3.addWidget(self.lcdNumber3)
        vwg3 = QWidget()
        vwg3.setLayout(vlayout3)
        self.thraed3 = MyThread3()
        self.thraed3.sinOut3.connect(self.lcd3display)
        self.thraed3.start()

       
        wlayout.addWidget(vwg1)
        wlayout.addWidget(vwg2)
        wlayout.addWidget(vwg3)

        self.setLayout(wlayout)
        self.show()

    def lcd1display(self,val):
        self.lcdNumber1.display(val)

    def lcd2display(self,val):
        self.lcdNumber2.display(val)

    def lcd3display(self,val):
        self.lcdNumber3.display(val)




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

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()