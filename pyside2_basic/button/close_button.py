import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtGui import QIcon
from PySide2.QtCore import QCoreApplication


class Ico(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('button')
        self.setWindowIcon(QIcon('icon.jpg'))

        qbu = QPushButton('exit',self)
        qbu.clicked.connect(QCoreApplication.instance().quit)
        qbu.resize(70,30)
        qbu.move(50,50)

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
    app.exec_()
