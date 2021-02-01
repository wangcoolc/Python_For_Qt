import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, Slot


@Slot()
def output(self):
    print("hello")
    

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('incon')
        self.setWindowIcon(QIcon())


        edit = QLineEdit('哈哈哈',self)
        edit.selectAll()
        edit.setFocus()
        edit.setGeometry(80,50,150,30)
     

        button = QPushButton("点我！",self)
        button.clicked.connect(self.Messageshow)
        self.show()

    def Messageshow(self):   
       QMessageBox.about(self,"test","很帅")
       QMessageBox.question(self,'很帅','确认退出吗',QMessageBox.No | QMessageBox.Yes, QMessageBox.No)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
    print("hello")