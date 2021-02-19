import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("tree view")
        self.setGeometry(300,300,500,500)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['key','value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0,'root')
        root.setIcon(0,QIcon("picture.jpeg"))
        self.tree.setColumnWidth(0,160)

        child1 = QTreeWidgetItem(root)
        root.setText(0,'child1')
        root.setText(1,'ios')
        root.setIcon(0,QIcon("picture.jpeg"))

        child2 = QTreeWidgetItem(root)
        root.setText(0,'child2')
        root.setText(1,'')
        root.setIcon(0,QIcon("picture.jpeg"))

        child3 = QTreeWidgetItem(child2)
        root.setText(0,'child3')
        root.setText(1,'andriod')
        root.setIcon(0,QIcon("picture.jpeg"))

        self.tree.addTopLevelItem(root)

        self.tree.expandAll()

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()





