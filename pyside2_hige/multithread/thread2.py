import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

global sec  
sec = 0


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("thread2")
        layout = QVBoxLayout()
        layout.addWidget(lcdNumber)

        button = QPushButton("开始")
        layout.addWidget(button)
        self.setLayout(layout)
        
        button.clicked.connect(self.work)
        timer.timeout.connect(self.counttime)
        self.show()

    def work(self):
        timer.start(1000)
        workThread.start()
        workThread.trigger.connect(self.timestop)

    def timestop(self):
        timer.stop()
        print("运行结束时用",lcdNumber.value())
        global sec
        sec = 0

    def counttime(self):
        global sec
        sec += 1
        print("aaaaaaaaaaaa")
        lcdNumber.display(sec)


class workThread(QThread):
    trigger = Signal()
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(20000000000):
            pass

        self.trigger.emit()

   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = QTimer()
    lcdNumber = QLCDNumber()
    workThread = workThread()
    ex = Example()
    app.exec_()

