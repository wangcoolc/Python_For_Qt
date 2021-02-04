import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Example(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.but1 = QPushButton("button1")
        self.but1.setCheckable(True)
        self.but1.toggle()
        self.but1.clicked.connect(lambda:self.whichbtn(self.but1))
        self.but1.clicked.connect(self.btnstate)

        self.but2 = QPushButton()
        self.but2.setIcon(QIcon('picture.jpeg'))
        self.but2.clicked.connect(lambda:self.whichbtn(self.but2))

        self.but3 = QPushButton("button3")
        self.but3.setEnabled(False)
    

        self.but4 = QPushButton("&button4")
        self.but4.setDefault(True)
        self.but4.clicked.connect(lambda:self.whichbtn(self.but4))

        layout.addWidget(self.but1)
        layout.addWidget(self.but2)
        layout.addWidget(self.but3)
        layout.addWidget(self.but4)

        self.setLayout(layout)
        self.show()

    def whichbtn(self,butn):
        print("clicked button is" + butn.text())

    def btnstate(self):
        if self.but1.isChecked():
            print("button pressed")
        else:
            print("button released")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()