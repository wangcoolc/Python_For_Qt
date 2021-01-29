import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtCore import Slot

#@slot()是一个装饰器，标志这这个函数是一个slot（槽）
@Slot()

def output():
    print("Button clicked!")

app = QApplication(sys.argv)
button = QPushButton("clicked me")
#将信号与槽进行绑定
button.clicked.connect(output)
button.show()
app.exec_()
