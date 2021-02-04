import sys
from PySide2.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QDesktopWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        flo = QFormLayout()
        edit1 = QLineEdit()
        edit2 = QLineEdit()
        edit3 = QLineEdit()
        edit4 = QLineEdit()

        flo.addRow("Normal",edit1)
        flo.addRow("Noecho",edit2)
        flo.addRow("Password",edit3)
        flo.addRow("Passwoedecho",edit4)

        edit1.setPlaceholderText("Normal")
        edit2.setPlaceholderText("Noecho")
        edit3.setPlaceholderText("Password")
        edit4.setPlaceholderText("Passwoedecho")

        edit1.setEchoMode(QLineEdit.Normal)
        edit2.setEchoMode(QLineEdit.NoEcho)
        edit3.setEchoMode(QLineEdit.Password)
        edit4.setEchoMode(QLineEdit.PasswordEchoOnEdit)



        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)
        self.setLayout(flo)
        self.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()