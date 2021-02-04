import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.but1 = QRadioButton("but1")
        self.but1.setChecked(True)
        self.but1.toggled.connect(lambda:self.btnstate(self.but1))
        layout.addWidget(self.but1)

        self.but2 = QRadioButton("but2")
        self.but2.toggled.connect(lambda:self.btnstate(self.but2))
        layout.addWidget(self.but2)

        self.setLayout(layout)
        self.show()

    def btnstate(self,bt):
        if bt.text() == "but1":
            if bt.isChecked() == True:
                print(bt.text() + "is selected")
            else:
                print(bt.text() + "is deselected")
        
        if bt.text() == "but2":
            if bt.isChecked() == True:
                print(bt.text() + "is selected")
            else:
                print(bt.text() + "is deselected")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()