import sys
from PySide2.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QHBoxLayout

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle('关闭主窗口')

        self.status = self.statusBar()
        self.status.showMessage("这是状态栏提示",5000)

        self.button = QPushButton('关闭')
        self.button.clicked.connect(self.onbutton)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

        self.show()
    
    def onbutton(self):
        sender = self.sender()
        print(sender.text() + '被按下')
        qApp = QApplication.instance()
        qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()