import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap ,QPalette

class Example(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('&Name',self)
        nameEd1 = QLineEdit(self)
        label1.setBuddy(nameEd1)

        label2 = QLabel('&passwed',self)
        nameEd2 = QLineEdit(self)
        label2.setBuddy(nameEd1)

        button1 = QPushButton('&OK')
        button2 = QPushButton('&Cancel')

        mianLayout = QGridLayout(self)
        mianLayout.addWidget(nameEd1,0,0)
        mianLayout.addWidget(nameEd1,0,1,1,2)

        mianLayout.addWidget(nameEd2,1,0)
        mianLayout.addWidget(nameEd2,1,1,1,2)

        mianLayout.addWidget(button1,2,1)
        mianLayout.addWidget(button2,2,2)

        
        self.setWindowTitle('label例子')

        self.show()

    def link_hovered(self):
        print("当鼠标滑过label-2标签时，触发事件")

    def link_clicked(self):
        print("当鼠标滑过label-4标签时，触发事件")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
