
__init__()
    python语言的构造函数

super()
    当子类继承父类时，子类中含有__init__时，不会自动调用父类__init__.想要调用父类的变量，必须用super().__init__();


if __name__ == '__main__':
    
   如果写了这句话并将执行的语句放到这个判断语句的后面，那么只有程序本身被执行的时候才能运行这个判断语句下面的语句。
   否则程序被作为模块导入的时候就会被执行。
   
   
   
QWidget 小部件是pyside2中所有用户界面对象的基类。默认构造函数没有父类，没有父类口小部件称为窗口。

resize() 调整窗口小部件的大小

move()  移动小部件在屏幕的位置。

setWindowTitle() 设置窗口的标题

setWindowIcon(icon) 设置窗口的图标      icon – PySide2.QtGui.QIcon

setGeometry(x,y,wight,hight)  在屏幕上定位窗口并设置它的大小  x y  wight hight

show()  在屏幕上显示窗口小部件，首先在内存中创建，在屏幕上显示





QPushButton  按钮的类

button = QPushButton('xxx',self)  创建一个按钮的对象。第一个参数是按钮的标签，第二个是父窗口小部件 

button.clicked(“槽”) 如果我们点击按钮，点击的信号发出。 槽可以是Qt槽函数，或者Python可调用的函数。

button.resize() 设置按钮大小

button.move() 设置按钮的位置

button.setToolTip() 使用富文本格式





QCoreApplication  包含主事件循环，它处理和调度所有事件

QCoreApplication.instance() 对象实例化



QLineEdit   编辑文本框
self.text = QLineEdit('在这里输入数字', self)      在窗口小部件上，添加一个文本框

self.text.selectAll()          可以理解为将“在这里输入数字”进行全选                 
self.text.setFocus()		   setFocus()就是让输入焦点置于文本栏中，方便用户输入，不然还得手动在文本栏中单击一下，很是麻烦。
self.text.setGeometry(80, 50, 150 ,30)   设置文本框的大小





QMessageBox.about(self, '看结果','猜大了!')就是弹出一个对话框，告诉你结果是什么样的。  第一个参数是self，第二个是弹出对话框的标题，第三个是对话框弹出的内容

QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  第一个字符串出现在标题栏上。 第二个字符串是对话框显示的消息文本。 第三个参数指定出现在对话框中的按钮的组合。 最后一个参数是默认按钮。 它是初始键盘焦点的按钮。 返回值存储在答复变量中。


QtGui.QLCDNumber(self) 窗口上设置一个LCD屏
QtGui.QDial(self)       窗口上设置一个轮盘
dial.valueChanged.connect(lcd.display)  这里我们将QDial这个小部件的一个valueChanged信号连接到lcd数字的显示槽。

QDial对象发送信号。 QLCDNumber接收信号的。 槽是对信号作出反应的方法。


事件与信号处理
在事件模型中，有三个参与者：
1.事件来源    是状态更改的对象，他会生成事件。
2.事件对象    将状态更改封装在事件源中
3.事件目标    是要通知的对象


自定义信号： from PyQt5.QtCore import (Signal, QObject)
class Signal(QObject):
    showmouse = Signal()

self.s = Signal()
        self.s.showmouse.connect(self.about)
		
   def about(self):
        QMessageBox.about(self,'鼠标','你点鼠标了吧！')

