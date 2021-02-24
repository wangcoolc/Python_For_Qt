from PySide2.QtCore import QObject, Signal

class Example(QObject):

    sendmsg = Signal(object)

    def __init__(self):
        super().__init__()

    def run(self):
        self.sendmsg.emit("hello pyside2")

class Slot(QObject):
    def __init__(self):
        super().__init__()

    
    def get(self,msg):
        print("QSlot get msg =>" + msg)

        