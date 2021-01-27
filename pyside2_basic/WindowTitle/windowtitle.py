import sys
from PySide2.QtWidgets import QApplication, QWidget ,QLabel

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(300,300)
    w.move(500,500)
    w.setWindowTitle('test')
    w.show()

    app.exec_()
