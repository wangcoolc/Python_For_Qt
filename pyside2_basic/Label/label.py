import sys
from PySide2.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap ,QPalette

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("这是一个文本标签")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap('picture.jpeg'))

        label4.setText("<A href='https://github.com/wangcoolc/'>欢迎</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')

        vbox = QVBoxLayout() 
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        label2.setOpenExternalLinks(True)

        label4.setOpenExternalLinks(True)

        label4.linkActivated.connect(self.link_clicked)

        label2.linkHovered.connect(self.link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        
        self.setLayout(vbox)
        self.setWindowTitle('label例子')

        self.show()

    def link_hovered(self):
        print("当鼠标滑过label-2标签时，触发事件")

    def link_clicked(self):
        print("当鼠标滑过label-4标签时，触发事件")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
