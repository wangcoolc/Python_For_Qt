import sys
from PySide2.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("nest1")
        self.resize(700,200)

        wwg = QWidget()

        wl = QHBoxLayout(wwg)

        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        glayout = QGridLayout()
        flayout = QFormLayout()


        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))

        vlayout.addWidget(QPushButton(str(3)))
        vlayout.addWidget(QPushButton(str(4)))

        glayout.addWidget(QPushButton(str(5)),0,0)
        glayout.addWidget(QPushButton(str(6)),0,1)
        glayout.addWidget(QPushButton(str(7)),1,0)
        glayout.addWidget(QPushButton(str(8)),1,1)

        flayout.addWidget(QPushButton(str(9)))
        flayout.addWidget(QPushButton(str(10)))
        flayout.addWidget(QPushButton(str(11)))
        flayout.addWidget(QPushButton(str(12)))

        wl.addLayout(hlayout)
        wl.addLayout(vlayout)
        wl.addLayout(glayout)
        wl.addLayout(flayout)

        wl.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()