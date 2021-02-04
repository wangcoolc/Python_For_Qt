import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap,QPalette

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)

        label1.setText("<A href='https://www.baidu.com/'>百度</a>")
        label2.setText("<A href='https://www.taobao.com/'>淘宝</a>")
        label3.setText("<A href='https://www.meituan.com/'>美团</a>")

        palette1 = QPalette()
        palette1.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette1)
        label1.setAlignment(Qt.AlignCenter)
        label1.setToolTip('百度')
        label1.setOpenExternalLinks(True)

        palette2 = QPalette()
        palette2.setColor(QPalette.Window,Qt.red)
        label2.setPalette(palette2)
        label2.setAlignment(Qt.AlignCenter)
        label2.setToolTip('淘宝')
        label2.setOpenExternalLinks(True)


        palette3 = QPalette()
        palette3.setColor(QPalette.Window,Qt.green)
        label3.setPalette(palette3)
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('美团')
        label3.setOpenExternalLinks(True)


        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addStretch()
        hbox.addWidget(label2)
        hbox.addStretch()
        hbox.addWidget(label3)

        self.setLayout(hbox)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
