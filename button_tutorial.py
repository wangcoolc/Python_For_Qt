import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot

# Greetings
@Slot()
def say_hello():
    print("button clicked, Hello!")

#Create the Qt Application
app = QApplication(sys.argv)

#create a button
button = QPushButton("Click me")

#connect the button to the function
button.clicked.connect(say_hello)

#show the button
button.show()
#run the main qt loop
app.exec_()
