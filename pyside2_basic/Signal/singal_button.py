import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,350,250)
        self.setWindowTitle("signal")

        self.lab = QLabel('方向',self)

        self.lab.setGeometry(150,100,50,50)

        self.show()

    def keyPressEvent(self,e):

        if e.key() == Qt.Key_Up:
            self.lab.setText('^')

        elif e.key() == Qt.Key_Down:
            self.lab.setText('|')

        elif e.key() == Qt.Key_Left:
            self.lab.setText('<')

        else:
            self.lab.setText('>')


if __name__ == '__main__':
    app = QApplication();
    ex = Example()
    app.exec_()
