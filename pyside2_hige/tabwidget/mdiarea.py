import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Example(QMainWindow):
    count = 0
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        self.setWindowTitle("MDI")
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered[QAction].connect(self.windowaction)

        self.show()

    def windowaction(self,q):
        print("triggered")

        if q.text() == "New":
            print("aaaaaaa")
            Example.count = Example.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow"+str(Example.count))
            self.mdi.addSubWindow(sub)
            sub.show()

        if q.text() == "cascade":
            self.mdi.cascadeSubWindow()

        if q.text() == "Tiled":
            self.mdi.tileSubWindow()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()