import sys
from PySide2.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout, QDesktopWidget, QTextEdit, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        self.textedit = QTextEdit()

        self.button1 = QPushButton("显示文本")
        self.button2 = QPushButton("显示HTML")

        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)

        layout.addWidget(self.textedit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)


        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)
        self.setLayout(layout)
        self.show()

    def button1_clicked(self):
        self.textedit.setPlainText("hello")

    def button2_clicked(self):
        self.textedit.setHtml("<font color='red' size='6'><red>hello</font>")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()