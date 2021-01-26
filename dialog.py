import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog)

class Form(QDialog):

    def __init__(self,parent=None):
        super().__init__(parent)
        #create widgets
        self.edit = QLineEdit("write my name here")
        self.button = QPushButton("show Greetings")
        #create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        #set dialog layout
        self.setLayout(layout)
        #add button signal to greetings slot
        self.button.clicked.connect(self.greetings)


    #greet thr user
    def greetings(self):
        print ("hello %s" % self.edit.text())

if __name__ == '__main__':

    #create the qt application
    app = QApplication(sys.argv)

    #create and show the form
    form = Form()
    form.show()

    #run the main qt loop
    sys.exit(app.exec_())

