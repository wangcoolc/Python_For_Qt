import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber, QDial

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('signal')

        lcd.setGeometry(100,50,150,60)
        dial.setGeometry(120,120,100,100)

        dial.valueChanged.connect(lcd.display)

        self.show()


if __name__ == '__main__':
    app = QApplication()
    ex = Example()
    app.exec_()

