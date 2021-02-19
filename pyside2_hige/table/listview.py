import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PySide2.QtCore import QStringListModel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("list view")
        self.setGeometry(500,500,300,300)

        listview = QListView()
        slm = QStringListModel()
        self.qList = ['item1','item2','item3','item4']
        slm.setStringList(self.qList)
        listview.setModel(slm)
        listview.clicked.connect(self.clicked)
         

        layout = QVBoxLayout()
        layout.addWidget(listview)
        self.setLayout(layout)

        self.show()
    
    def clicked(self,QModelIndex):
        QMessageBox.information(self,"Lisewidgets","你选择了:"+ self.qList[QModelIndex.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()