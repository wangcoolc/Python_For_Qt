import sys
from PySide2.QtWidgets import QWidget, QApplication, QMainWindow, QDesktopWidget

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle('屏幕中间')

        self.status = self.statusBar()
        self.status.showMessage("这是状态栏提示",5000)

        self.center()
        self.show()

    def center(self):
        scree = QDesktopWidget().screenGeometry()

        size = self.geometry()

        self.move((scree.width() - size.width()) / 2,((scree.height() - size.height())/2))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
