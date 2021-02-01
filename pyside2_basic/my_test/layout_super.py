import sys
from PySide2.QtWidgets import QApplication, QWidget, QListView, QHBoxLayout, QLineEdit, QPushButton
from PySide2.QtGui import QStandardItemModel, QStandardItem


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        self.setGeometry(300,300,500,500)
        self.setWindowTitle('xx')
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(QLineEdit("",self))
        layout.addWidget(QPushButton('x',self))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()