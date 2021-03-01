import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWebEngineWidgets import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("webengineview")
        self.setGeometry(5,30,1355,730)

        self.view = QtWebEngineView()

        self.view.load(QUrl('https://blog.csdn.net/anlian523/article/details/81075841'))

        self.setCentralWidget(self.view)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()