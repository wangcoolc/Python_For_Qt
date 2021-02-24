import sys
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("form")

        self.resize(400,100)

        formlayout = QFormLayout()
        lab1l = QLabel("标签1")
        lineedit1 = QLineEdit()

        lab12 = QLabel("标签2")
        lineedit2 = QLineEdit()

        lab13 = QLabel("标签3")
        lineedit3 = QLineEdit()

        formlayout.addRow(lab1l,lineedit1)
        formlayout.addRow(lab12,lineedit2)
        formlayout.addRow(lab13,lineedit3)

        self.setLayout(formlayout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()

