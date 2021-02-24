import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Thread")

        self.thraed = Worker()
        self.listFile = QListWidget()
        self.btstart = QPushButton("开始")

        layout = QGridLayout(self)
        layout.addWidget(self.listFile,0,0,1,2)
        layout.addWidget(self.btstart,1,1)
    
        self.btstart.clicked.connect(self.slotStart)
        self.thraed.sinOut.connect(self.slotAdd)

        self.show()

    def slotAdd(self,file_inf):
        self.listFile.addItem(file_inf)

    def slotStart(self):
        self.btstart.setEnabled(False)
        self.thread.start()

class Worker(QThread):
    sinOut = Signal(str)

    def __init__(self):
        super().__init__()
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while self.working == True:
            file_str = 'File index {0}'.format(self)
            self.num += 1

            self.sinOut.emit(file_str)

            self.sleep(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()









































