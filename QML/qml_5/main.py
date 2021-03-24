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
            p = os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip("\n")
            cpu_used = int(float(p))
            print("CpuUsage",cpu_used)
            self.CpuSignal.emit(int(cpu_used))
            self.sleep(1)

class Cputemperature(QThread):
    CputemSignal = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            f = open("/sys/class/thermal/thermal_zone0/temp",'r')
            temp = int(f.read().strip("\n"))/1000
            print("Cputemperature",temp)
            self.CputemSignal.emit(int(temp))
            self.sleep(1)



class RamUsage(QThread):
    RamSignal = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        p = os.popen('free')
        i = 0
        while True:
            i = i + 1
            line = p.readline()
            if i==2:
                RAM_stats = line.split()[1:4]  
                RAM_total = round(int(RAM_stats[0]) / 1000,0)
                RAM_used = round(int(RAM_stats[1]) / 1000,0)

                print("RAM_total",RAM_total)
                print("RAM_used",RAM_used)

                used = round(int((RAM_used / RAM_total) * 100),0)
                print("used",used)
                self.RamSignal.emit(int(used))
                self.sleep(1)
                p = os.popen('free')
                i = 0


class StorageUsage(QThread):
    StoragSignal = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        p = os.popen("df -h /")
        i = 0
        while True:
            i = i +1
            line = p.readline()
            if i==2:
                DISK_stats = line.split()[1:5]
                DISK_total = int(str(DISK_stats[0][0:2]))
                DISK_used = int(str(DISK_stats[1][0:2]))

                print("DISK_total",DISK_total)
                print("DISK_used",DISK_used)

                val = round(int((DISK_used / DISK_total) * 100),0)
                print("StorageUsage",val)
                self.StoragSignal.emit(int(val))
                self.sleep(1)
                p = os.popen("df -h /")
                i = 0


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
        os.system('sudo chown pi:pi /sys/class/backlight/10-0045/brightness')
        values = '%d'%val
        x = 'echo ' + values + ' > /sys/class/backlight/10-0045/brightness'
        os.system(x)

    #Camera
    @Slot()
    def Cameraon(self):
        print("camera on")
        os.system('sudo sed -i "s/start_x=0/start_x=1/g" /boot/config.txt')
    @Slot()
    def Cameraoff(self):
        print("camera off")
        os.system('sudo sed -i "s/start_x=1/start_x=0/g" /boot/config.txt')

    #SSH
    @Slot()
    def SSHon(self):
        print("ssh on")
        os.system('sudo ln -s /lib/systemd/system/ssh.service /etc/systemd/system/multi-user.target.wants/ssh.service')
    @Slot()
    def SSHoff(self):
        print("ssh off")
        os.system('sudo rm /etc/systemd/system/multi-user.target.wants/ssh.service')

    #VNC
    @Slot()
    def VNCon(self):
        print("vnc on")
        os.system('sudo ln -s /usr/lib/systemd/system/vncserver-x11-serviced.service /etc/systemd/system/multi-user.target.wants/vncserver-x11-serviced.service')
    @Slot()
    def VNCoff(self):
        print("vnc off")
        os.system('sudo rm /etc/systemd/system/multi-user.target.wants/vncserver-x11-serviced.service')
        


    #SPI
    @Slot()
    def SPIon(self):
        print("SPI on")
        os.system('sudo sed -i "s/dtparam=spi=off/dtparam=spi=on/g" /boot/config.txt')
    @Slot()
    def SPIoff(self):
        print("SPI off")
        os.system('sudo sed -i "s/dtparam=spi=on/dtparam=spi=off/g" /boot/config.txt')

    #I2C
    @Slot()
    def I2Con(self):
        print("i2c on")
        os.system('sudo sed -i "s/dtparam=i2c_arm=off/dtparam=i2c_arm=on/g" /boot/config.txt')
    @Slot()
    def I2Coff(self):
        print("i2c off")
        os.system('sudo sed -i "s/dtparam=i2c_arm=on/dtparam=i2c_arm=off/g" /boot/config.txt')
    
    #Serial
    @Slot()
    def Serialon(self):
        print("Serial on")
        os.system('sudo sed -i "s/enable_uart=0/enable_uart=1/g" /boot/config.txt')
    @Slot()
    def Serialoff(self):
        print("Serial off")
        os.system('sudo sed -i "s/enable_uart=1/enable_uart=0/g" /boot/config.txt')

    #Shutdown
    @Slot()
    def Shutdown(self):
        print("Shutdown")
        os.system('sudo shutdown now')

    #Reboot
    @Slot()
    def Rebooton(self):
        print("Rebooton")
        os.system('sudo reboot')

    #Logout
    @Slot()
    def Logout(self):
        print("Logout")
        os.system('exit')

    


if __name__ == '__main__':
    app = QApplication([])
    # view = QQuickView()
    engine = QQmlApplicationEngine()
    url = QUrl("NewbuttonUI.qml")

    cpu = CpuUsage()
    cputem = Cputemperature()
    arm = RamUsage()
    Storage = StorageUsage()
    axis = Accelerator()
    sysinfo = Systeminfo()

    seting = Settting()

    # context = view.rootContext()
    context = engine.rootContext()
    context.setContextProperty("_CpuUsage", cpu)
    context.setContextProperty("_Cputemperature", cputem)
    context.setContextProperty("_RamUsage", arm)
    context.setContextProperty("_StorageUsage", Storage)
    context.setContextProperty("_Accelerator", axis)
    context.setContextProperty("_Systeminfo", sysinfo)

    context.setContextProperty("_Settting", seting)



    cpu.start()
    cputem.start()
    arm.start()
    Storage.start()
    axis.start()
    sysinfo.start()

    # view.setSource(url)
    # view.show()
    engine.load(url)
    # engine.show()
    app.exec_()
