import sys
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QFormLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("nest")

        wlayout = QHBoxLayout()

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


        hwg = QWidget()
        vwg = QWidget()
        gwg = QWidget()
        fwg = QWidget()

        hwg.setLayout(hlayout)
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(flayout)

        wlayout.addWidget(hwg)
        wlayout.addWidget(vwg)
        wlayout.addWidget(gwg)
        wlayout.addWidget(fwg)


        self.setLayout(wlayout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()


        
