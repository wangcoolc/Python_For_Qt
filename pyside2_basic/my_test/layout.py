import sys
from  PySide2.QtWidgets import QApplication ,QWidget ,QLabel ,QPushButton ,QLCDNumber, QFormLayout ,QGridLayout ,QTextEdit
from  PySide2.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800,300,500,500)
        self.setWindowTitle("xxx")
        self.setWindowIcon(QIcon('picture.jpeg'))

        form = QFormLayout()
        

        #self.lcd = QLCDNumber()
        #self.lcd.display("1234")
        strlabel = QLabel("对话内容")
        self.stredit  = QTextEdit("")
        # stredit.resize(100,100)

        self.button = QPushButton("发送")
        butedit  = QTextEdit("")
         
       # form.addWidget(self.button)
        form.addRow(strlabel,self.stredit)
        form.addRow(self.button,butedit)
             
        self.button.clicked.connect(self.cli)
        self.show()

    def cli(self):
        self.stredit.text(butedit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()

