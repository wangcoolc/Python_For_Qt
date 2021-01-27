import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon

class Ico(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,220)
        self.setWindowTitle("set icon")
        self.setWindowIcon(QIcon("icon.jpg"))

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
    app.exec_()
