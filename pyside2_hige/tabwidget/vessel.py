import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Example(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1,"tab 1")
        self.addTab(self.tab2,"tab 2")
        self.addTab(self.tab3,"tab 3")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.setWindowTitle("tab")
        self.show()

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名",QLineEdit())
        layout.addRow("地址",QLineEdit())
        self.setTabText(0,"联系方式")
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))

        layout.addRow(QLabel("性别"),sex)
        layout.addRow("生日",QLineEdit())
        self.setTabText(1,"个人详细信息")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.setTabText(2,"教育程度")
        self.tab3.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
