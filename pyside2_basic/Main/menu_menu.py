import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
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

        savemenu = QMenu('保存方式(&S)',self)
        saveact = QAction(QIcon('picture.jpeg'),'保存...',self)
        saveact.setShortcut("Ctrl+S")
        saveact.setStatusTip('保存文件')

        savesact = QAction(QIcon('picture.jpeg'),'另存为...(&O)',self)
        savesact.setStatusTip('文件另存为')
        savemenu.addAction(saveact)
        savemenu.addAction(savesact)

        newact = QAction(QIcon('picture.jpeg'),'新建(&N)',self)
        newact.setShortcut('Ctrl+N')
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newact)
        fileMenu.addMenu(savemenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitact)

        self.show()

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = Example()
    app.exec_()