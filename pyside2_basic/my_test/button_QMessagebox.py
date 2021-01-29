import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, Slot


@Slot()
def output():
    print("hello")

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('incon')
        self.setWindowIcon(QIcon())

        box = Q

        button = QPushButton("点我！",self)
        button.clicked.connect(output)



        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
