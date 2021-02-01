import sys
from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,500,300,300)
        self.setWindowTitle('test')

        bt1 = QPushButton("甲",self)
        bt2 = QPushButton("乙",self)
        bt3 = QPushButton("丙",self)
        bt4 = QPushButton("丁",self)

        layout = QHBoxLayout()
        layout.addWidget(bt1)
        layout.addWidget(bt2)
        layout.addWidget(bt3)
        layout.addWidget(bt4)


        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addLayout(layout)

        self.setLayout(vlayout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()


