import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

global sec
sec = 0

def setTime():
    global sec
    sec += 1
    lcdNumber.display(sec)

def work():
    timer.start(1000)

    for i in range(20000):
        pass

    timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300,120)

    layout = QVBoxLayout(top)
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("测试")
    layout.addWidget(button)

    timer = QTimer()
    timer.timeout.connect(setTime)
    button.clicked.connect(work)
    
    top.setLayout(layout)
    top.show()
    app.exec_()

