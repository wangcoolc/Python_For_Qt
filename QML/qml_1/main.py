# This Python file uses the following encoding: utf-8
import os, random
import sys
import PySide2.QtQml
from PySide2.QtWidgets import *
from PySide2.QtQuick import *
from PySide2.QtCore import *

#定时器的方式
# class MyClass(QObject):
#     timerSignal = Signal(int)

#     def __init__(self):
#         super().__init__()

#         # 定义一个时间信号
        
#         self._timer = QTimer(self, timeout=self.onTimeout)
#         self._timer.start(1000)

#     def onTimeout(self):
#         # 定时器发送信号通知qml
#         val = random.randint(1,100)
#         print("val",val)
#         self.timerSignal.emit(int(val))


# 线程的方式
class CpuUsage(QThread):
    CpuSignal = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            val = random.randint(1,100)
            print("vvv1",val)
            self.CpuSignal.emit(int(val))
            self.sleep(1)


class RamUsage(QThread):
    RamSignal = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            val = random.randint(1,100)
            print("vvv2",val)
            self.RamSignal.emit(int(val))
            self.sleep(1)


class StorageUsage(QThread):
    StoragSignal = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            val = random.randint(1,100)
            print("vvv3",val)
            self.StoragSignal.emit(int(val))
            self.sleep(1)


class Accelerator(QThread):
    AxisSignal = Signal(int,int,int)
    def __init__(self):
        super().__init__()
    
    def run(self):
    
        while True:
            val1 = random.randint(4000,12000)
            val2 = random.randint(4000,12000)
            val3 = random.randint(4000,12000)
            self.AxisSignal.emit(val1,val2,val3)
            self.sleep(1)


if __name__ == '__main__':
    app = QApplication([])
    view = QQuickView()
    url = QUrl("Ui.ui.qml")

    cpu = CpuUsage()
    arm = RamUsage()
    Storage = StorageUsage()
    axis = Accelerator()

    context = view.rootContext()
    context.setContextProperty("_CpuUsage", cpu)
    context.setContextProperty("_RamUsage", arm)
    context.setContextProperty("_StorageUsage", Storage)
    context.setContextProperty("_Accelerator", axis)
    cpu.start()
    arm.start()
    Storage.start()
    axis.start()

    view.setSource(url)
    view.show()
    app.exec_()
