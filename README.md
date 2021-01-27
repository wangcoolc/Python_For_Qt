
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


QCoreApplication  包含主事件循环，它处理和调度所有事件

QCoreApplication.instance() 对象实例化