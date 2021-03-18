# This Python file uses the following encoding: utf-8
import os, random
import sys
import PySide2.QtQml
from PySide2.QtQml import QQmlApplicationEngine
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

class Systeminfo(QThread):
    SystemSignal = Signal(str,str,str,str,str,str)
    def __init__(self):
        super().__init__()
    
    def run(self):
        Compute = "CM46666"
        Retermial = "RT666"
        Version = "Raspberry Pi OS:Jan.12th 2012"
        Kernel = "6.9"
        Ethernet = "192.168.4.253"
        Wifi = "okey"
        self.sleep(1)
        self.SystemSignal.emit(Compute,Retermial,Version,Kernel,Ethernet,Wifi)


class Settting(QObject):

    # LCD Backlight
    @Slot(int)
    def Lcdlightset(self,val):
        print("tetete",val)


    #Camera
    @Slot()
    def Cameraon(self):
        print("camera on")

    @Slot()
    def Cameraoff(self):
        print("camera off")

    #SSH
    @Slot()
    def SSHon(self):
        print("ssh on")

    @Slot()
    def SSHoff(self):
        print("ssh off")


if __name__ == '__main__':
    app = QApplication([])
    # view = QQuickView()
    engine = QQmlApplicationEngine()
    url = QUrl("NewbuttonUI.qml")

    cpu = CpuUsage()
    arm = RamUsage()
    Storage = StorageUsage()
    axis = Accelerator()
    sysinfo = Systeminfo()

    seting = Settting()

    # context = view.rootContext()
    context = engine.rootContext()
    context.setContextProperty("_CpuUsage", cpu)
    context.setContextProperty("_RamUsage", arm)
    context.setContextProperty("_StorageUsage", Storage)
    context.setContextProperty("_Accelerator", axis)
    context.setContextProperty("_Systeminfo", sysinfo)

    context.setContextProperty("_Settting", seting)



    cpu.start()
    arm.start()
    Storage.start()
    axis.start()
    sysinfo.start()

    # view.setSource(url)
    # view.show()
    engine.load(url)
    # engine.show()
    app.exec_()
