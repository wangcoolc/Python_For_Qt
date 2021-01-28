import sys
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
from PySide2.QtCore import Signal, QObject

class Signal(QObject):
    showmouse = Signal()

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("mouse")

        self.s = Signal()
        self.s.showmouse.connect(self.about)

        self.show()

    def about(self):
        QMessageBox.about(self,'鼠标','你点鼠标了吧！')

    def mousePressEvent(self,e):
        self.s.showmouse.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
