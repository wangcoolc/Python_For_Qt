import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PySide2.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('准备就绪')
        self.setGeometry(300,300,400,200)
        self.setWindowTitle('test')

        exitact = QAction(QIcon('picture.jpeg'),'退出(&E)',self)
        exitact.setShortcut('Ctrl+Q')
        exitact.setStatusTip('退出程序')
        exitact.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(exitact)

        self.show()

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = Example()
    app.exec_()