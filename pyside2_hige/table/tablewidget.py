import sys
from PySide2.QtWidgets import QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("table widget")
        self.setGeometry(300,300,500,500)

        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        tablewidget.setHorizontalHeaderLabels(['姓名','性别','体重'])

        newitem = QTableWidgetItem("张三")
        tablewidget.setItem(0,0,newitem)

        newitem = QTableWidgetItem("男")
        tablewidget.setItem(0,1,newitem)

        newitem = QTableWidgetItem("120")
        tablewidget.setItem(0,2,newitem)
        

        layout = QHBoxLayout()
        layout.addWidget(tablewidget)
        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()