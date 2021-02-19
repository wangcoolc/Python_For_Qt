import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Example(QListWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        