import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QMessageBox
from PySide2.QtCore import Signal, QObject

class Example(QWidget):

    restarted = Signal(QWidget,str)
    _self = None

    def __init__(self,path):
        super().__init__()
        Example._self = self
        self.initUI(path)

    def initUI(self,path):
        self.setGeometry(500,500,300,300)
        self.setWindowTitle('test')
        layout = QVBoxLayout()
        layout.addWidget(QLabel("当前工作目录:",self))

        self.diredit = QLineEdit(self,"请输入要切换的目录")
        # self.diredit = QLineEdit(self,placeholderText="请输入要切换的目录",returnPressed=self.onChangeDir)
        layout.addWidget(self.diredit)

        # self.button = QPushButton('切换',self,clicked=self.onChangeDir)
        # layout.addWidget(self.button)

        # self.restarted.connect(Example.onRestart) 
        self.show()

    # def onChangeDir(self):
    #     path = self.diredit.text().strip()
    #     if path and QMessageBox.question(self,"提示","确认要切换到{0}目录吗".format(path)) == QMessageBox.Yes:
    #         self.hide()
    #         self.restarted.emit(self,path)
    #     else:
    #         self.diredit.setFocus()

    # def onRestart(cls,widget,path):
    #     w = Example(path)
    #     w.show()
    #     widget.close()
    #     widget.deleteLater()
    #     del widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example('my_test')
    app.exec_()
    
