import sys
from PySide2.QtWidgets import QApplication, QMainWindow

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('准备就绪')
        self.setGeometry(300,300,400,200)
        self.setWindowTitle('test')
        self.show()

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = Example()
    app.exec_()