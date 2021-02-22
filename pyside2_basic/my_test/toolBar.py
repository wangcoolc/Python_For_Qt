import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("toolbar")

        layout = QVBoxLayout()
        tb = self.addToolBar("File")

        new = QAction("new",self)
        tb.addAction(new)

        open = QAction("open",self)
        tb.addAction(open)

        save = QAction("save",self)
        tb.addAction(save)

        tb.actionTriggered[QAction].connect(self.tool)


        self.setLayout(layout)
        self.show()

    def tool(self,a):
        print("pressed tool button is",a.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
    