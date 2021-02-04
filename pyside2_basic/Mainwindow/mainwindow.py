import sys
from PySide2.QtWidgets import QWidget, QApplication, QMainWindow

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle('哈哈')

        self.status = self.statusBar()
        self.status.showMessage("这是状态栏提示",5000)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()