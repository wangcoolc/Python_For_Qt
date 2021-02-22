import sys
from PySide2.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PySide2.QtCore import QTimer, QDateTime

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(500,500,500,500)
        self.setWindowTitle("QTimer")

        layout = QGridLayout(self)

        self.list = QListWidget()
        self.label1 = QLabel('显示当前时间')
        self.startbut = QPushButton("开始")
        self.endbut = QPushButton("结束")

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.showtime)

        layout.addWidget(self.label1,0,0,1,2)
        layout.addWidget(self.startbut,1,0)
        layout.addWidget(self.endbut,1,1)

        self.startbut.clicked.connect(self.starttimer)
        self.endbut.clicked.connect(self.endtimer)

        self.show()

    def showtime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label1.setText(timeDisplay)


    def starttimer(self):
        self.timer.start(1000)
        self.startbut.setEnabled(False)
        self.startbut.setEnabled(True)

    def endtimer(self):
        self.timer.stop()
        self.endbut.setEnabled(True)
        self.endbut.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()