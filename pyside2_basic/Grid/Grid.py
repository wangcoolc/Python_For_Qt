import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QLCDNumber, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('Grid')
        
        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd,0,0,3,0)
        grid.setSpacing(10)

        
        names = ['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']


        positions = [(i,j) for i in range(4,9) for j in range(4,8)]

        for position, name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)
            button.clicked.connect(self.aa)


        self.show()

    def aa(self):
        sender = self.sender().text()
        ls = ['/','*','-','=','+']
        if sender in ls:
            self.lcd.display('A')
        else:
            self.lcd.display(sender)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()

