import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('incon')
        self.setWindowIcon(QIcon())

        button = QPushButton("点我！",self)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
