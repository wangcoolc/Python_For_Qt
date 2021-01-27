import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon




if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    w = QWidget()
    w.resize(300,300)
    w.move(300,300)
    w.setWindowTitle("test inco")
#    s = QIcon()
    w.setWindowIcon(QIcon('icon.jpg'))

    w.show()

    app.exec_()
