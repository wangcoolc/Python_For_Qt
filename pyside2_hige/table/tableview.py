import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("table view")
        self.setGeometry(500,500,300,300)

        self.model = QStandardItemModel(4,4)
        self.model.setHorizontalHeaderLabels(['标题1','标题2','标题3','标题4'])

        for row in range(4):
            for column in range(4):
                item = QStandardItem("row %s,column %s"%(row,column))

            self.model.setItem(row,column,item)

        self.tableview = QTableView()
        self.tableview.setModel(self.model)

        dlglayout = QVBoxLayout()
        dlglayout.addWidget(self.tableview)
        self.setLayout(dlglayout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()