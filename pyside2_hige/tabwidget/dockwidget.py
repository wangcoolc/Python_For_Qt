import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("dock widget")

        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("new")
        file.addAction("save")
        file.addAction("quit")

        self.items = QDockWidget("Dockable",self)
        self.listWidget = QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")

        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())

        self.addDockWidget(Qt.RightDockWidgetArea,self.items)
        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
