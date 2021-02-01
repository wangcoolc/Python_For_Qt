import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLabel, QLineEdit, QTextEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('表单')

        formlayout = QFormLayout()
        namelabel = QLabel("姓名")
        namelineedit = QLineEdit("")
        
        instrlabel = QLabel("简介")

        instrlineedit = QTextEdit("")

        formlayout.addRow(namelabel,namelineedit)
        formlayout.addRow(instrlabel,instrlineedit)

        self.setLayout(formlayout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
    
