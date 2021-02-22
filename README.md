# Python
```python
__init__()
    python语言的构造函数

super()
    当子类继承父类时，子类中含有__init__时，不会自动调用父类__init__.想要调用父类的变量，必须用super().__init__();


if __name__ == '__main__':
    
   如果写了这句话并将执行的语句放到这个判断语句的后面，那么只有程序本身被执行的时候才能运行这个判断语句下面的语句。
   否则程序被作为模块导入的时候就会被执行。
   
range()函数：用法1：只有一个参数，表示从0到这个参数内的所有整数，不包括参数
            用法2：两个参数，第一个表示左边界，第二个表示右边界，range表示从左边界到右边界的所有整数，左闭右开
            用法3：三个参数，第一个表示左边界，第二个表示右边界，第三个表示步长step，即两个整数之间相差的数，左闭右开。
   range(start, stop[, step])
   参数说明：
       start 计数从start开始。默认是从0开始
       stop[  计数到stop结束，但是不包括stop
       step]  步长，默认为1
     
高级特征：   
   切片操作符(Slice):
        L[0:3]
	
	
	迭代 ：如果给定一个list或者tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历成为迭代
	for key in d:
	如何判断一个对象是迭代对象：
	from collections import Iterable
	>>> isinstance('abc', Iterable) # str是否可迭代
        True
	
	
	列表生成式：可以用来创建list的生成式
	>>> [x * x for x in range(1, 11)]
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	
	for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
	>>> [x * x for x in range(1, 11) if x % 2 == 0]
	[4, 16, 36, 64, 100]
	
	还可以使用两层循环，可以生成全排列：
	>>> [m + n for m in 'ABC' for n in 'XYZ']
	['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
	
	生成器：这种一边循环一边计算的机制，称为生成器：generator。
	       第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator。
```  
   
# QWidget（窗口）
	小部件是pyside2中所有用户界面对象的基类。默认构造函数没有父类，没有父类口小部件称为窗口。一个程序可以有多个窗口，一个窗口可以有多个控件
	控件指的是按钮，复选框，文本框，表格，进度条
```python
	resize() 调整窗口小部件的大小

	move()  移动小部件在屏幕的位置。

	setWindowTitle() 设置窗口的标题

	setWindowIcon(icon) 设置窗口的图标      icon – PySide2.QtGui.QIcon

	setGeometry(x,y,wight,hight)  在屏幕上定位窗口并设置它的大小  x y  wight hight

	show()  在屏幕上显示窗口小部件，首先在内存中创建，在屏幕上显示

	setToolTip('这是一个<b>气泡提示</b>') 使用富文本格式

	QToolTip.setFont(QFont('SansSerif'),10)  设置气泡提示信息的字体与字号大小	
```

# QLabel（标签）
	一个占位符，可以显示不可编辑的文本或者图片
```python
	setAlignment()  按照固定值方式对齐文本：
					Qt.AlignLeft   水平方向靠左对齐
					Qt.AlignRight  水平方向靠右对齐  
					Qt.AlignCenter 水平方向居中对齐
					Qt.AlignJustify 水平方向调整间距两端对齐
					Qt.AlignTop      垂直方向靠上对齐
					Qt.AlignBottom  垂直方向靠下对齐
					Qt.AlignVCenter  垂直方向居中对齐
					
	setIndent()     设置文本缩进值
	setPixmap()     设置QLabel为一个Pixmap图片
	text()			获得QLabel的文本内容
	setText()       设置QLabel的文本内容
	selectedText()  返回所选择的字符
	setBuddy()
	setWordWrap()   设置是否允许换行
	
	
	label的信号：
		    linkActivated   当单击标签中嵌入的超链接，希望在新窗口中打开这个超链接时，setOpenExternalLinks特性必须设置为true
	            linkHovered     当鼠标指针滑过标签中嵌入的超链接时，需要用槽函数与这个信号绑定
```

# QLineEdit(单行文本框)
```python
	setAlignment()  按照固定值方式对齐文本：
					Qt.AlignLeft   水平方向靠左对齐
					Qt.AlignRight  水平方向靠右对齐  
					Qt.AlignCenter 水平方向居中对齐
					Qt.AlignJustify 水平方向调整间距两端对齐
					Qt.AlignTop      垂直方向靠上对齐
					Qt.AlignBottom  垂直方向靠下对齐
					Qt.AlignVCenter  垂直方向居中对齐
					
	clear()         清除文本框内容
	setEchoMode()	设置文本框显示格式。允许输入的文本显示格式的值可以是：
					QLineEdit.Normal,正常显示输入的字符，此为默认选项
					QLineEdit.NoEcho,不显示任何输入的字符，常用于密码类型的输入，且其密码长度需要保密时
					QLineEdit.Password,显示与平台相关的密码掩码字符，而不是实际输入的字符
					QLineEdit.PasswordEchoOnEdit 在编辑是显示字符，负责显示密码类型的输入
					
	setPlaceholderText()	设置文本框浮显文字
	setMaxLength()          设置文本框所允许输入的最大字符数
	setReadOnly()		设置文本框为只读的
	setText() 		设置文本框内容
	Text()			返回文本内容
	setDragEnabled()	设置文本框是否接受拖动
	selectAll()		全选
	setFocus（）             得到焦点
	setInputMask()		设置掩码
	setValidator()          设置文本框的验证器(验证规则)，将限制任意可能输入的文本，可用的检验器为：
							QIntValidator 限制输入整数
							QDoubelValidator   限制输入浮点数
							QRegexpValidator   检查输入是否符合正则表达式
	
	LineEdit的信号：
					selectionChanged     只要选择改变了，这个信号就会被发射
					textChange           当修改文本内容时，这个信号会被发射
					editingFinished      当编辑文本结束时，这个信号会被发射
```

# QTextEdit（多行文本框）
```python
	setPlainText()			设置多行文本框的文本内容
	toPlainText()			返回多行文本框的文本内容
	setHtml()			设置多行文本框的内容为HTML文档，HTML文档是描述网页的
	totHtml（）		       返回多行文本框的HTML文档内容
	clear（）			       清除多行文本框的内容
```

# QAbstractButton (按钮类控件)
	QPushButton， QToolButton， QRadioButton, QCheckBox
```python
	isDown()         提示按键被按下
	isChecked()      提示按键是否已经标记
	isEnable()	 提示按钮是否可以被用户点击
	isCheckAble()    提示按钮是否为可标记的
	setAutoRepeat()  设置按钮是否在用户长按时可以自动重复执行
	
	QAbstractButton的信号：
				pressed        当鼠标指针在按钮上并按下左键时触发该信号
				Released       当鼠标左键被释放时触发该信号
				Clicked        当鼠标左键被按下然后释放时，或者快捷键被释放时触发该信号
				Toggled        当按钮的标记状态发生改变时触发该信号
```
## QPushButton (按钮的类)
	其形状是长方形，文本标题或图标可以显示在长方形上。它也是一种命令按钮，可以单击该按钮执行一些命令
```python
	setCheckable() 	设置按钮是否已经被选中，如果设置为True，则表示按钮将保持以点击和释放状态
	toggle()	在按钮状态之间进行切换
	setIcon()       设置按钮上的图标
	setEnabled()	设置按钮是否可以使用，当设置为Flash时，按钮变成不可用状态，点击它不会发射信号
	isChecked()	返回按钮的状态，返回值为True或False
	setDefault()    设置按钮的默认状态
	setText（）      设置按钮的显示文本
	text（）         返回按钮显示的文本	
```
## QRadioButton
	提供了一组可供选择的按钮和文本标签，用户可以选择其中一个选项，标签用于显示对应的文本信息。比如开关按钮“on” or “off”
```python
	setCheckable()	设置按钮是否已经被选中，可以改变单选按钮的选中状态，如果设置为True，则表示单选按钮将保持已点击和释放状态
	isChecked()	返回按钮的状态，返回值为True或False
	setText（）     设置按钮的显示文本
	text（）        返回按钮显示的文本
```

## QCheckBox
```python
	setCheckable()	设置按钮是否已经被选中，可以改变单选按钮的选中状态，如果设置为True，则表示单选按钮将保持已点击和释放状态
	isChecked()	返回按钮的状态，返回值为True或False
	setText（）      设置按钮的显示文本
	text（）         返回按钮显示的文本
	setTriState()	设置复选框为一个三态复选框 
	                Qt.Checked  2  组件没有被选中
					Qt.PartiallyChecked  1  组件被半选中
					Qt.Unchecked   0     组件被选中
```

# QComboBox(下拉列表框)
```python
	addItem()        添加一个下拉选项
	addItems()       从列表中添加下拉选项
	Clear()		 删除下拉选项集合中的所有选项
	count（）        返回下拉选项集合中的数目
	currentText()    返回选中选项的文本
	itemText(i)	 获取索引为i的item的选项文本
	currentIndex()   返回选中项的索引
	setItemText(int index，text)  改变序号为index项的文本
	
	QComboBox的信号：
				Activated		当用户选中一个下拉选项时发射该信号
				currentIndexChanged     当下拉选项的索引发生改变时发射该信号
				highlighted		当选中一个已经选中的下拉选项时，发射该信号
```

# QSpinBox(计数器)
	QSpinBox是一个计数器控件，允许用户选择一个整数值，通过单击向上/向下按钮或按键盘上的上/下箭头来增加/减少当前显示的值，当然用户也可以输入值
```python
	setMinimum()	设置计数器的下界
	setMaximum()	设置计数器的上界
	setRange()	设置计数器的最大值，最小值和步长值
	setValue()	设置计数器的当前值
	Value()		返回计数器的当前值
	singleStep()	设置计数器的步长值
	
	QSpinBox的信号：
				valueChanged      每次点击向上/向下按钮时，都会发送信号。
```

# QSlider(滑动条)

# QDialog (对话框类控件)
	快捷的通过各个类完成字号大小、字体颜色以及文件的选择
```python
	setWindowTitle()   设置对话框标题
	setWindowModality()  设置窗口模态，取值如下：
						 Qt.NonModal   非模态，可以和程序的其他窗口交互
						 Qt.WindowModal 窗口模态，程序在未处理完当前对话框时，将阻止和对话框的父窗口进行交互
						 Qt.ApplicationModal  应用程序模态，阻止和任何其他窗口进行交互
```

## QMessageBox(弹出式对话框)
	用于显示消息，允许用户通过单击不同的标准按钮对消息进行反馈。
	QMessageBox提供了许多常用的弹出式对话框，如提示，警告，错误，询问，关于，只是显示时的图标不同，其他功能是一样的
```python
	information(parent,title,text,button,defaultButton)   弹出消息对话框：
									parent：指定的父窗口控件
									title：对话框标题
									text：对话框文本
									buttons:多个标准按钮，默认为OK按钮
									defaultButton：默认选中的标准按钮，默认是第一个标准按钮
	question(parent,title,text,button,defaultButton)      弹出问答对话框
	warning(parent,title,text,button,defaultButton)       弹出警告对话框
	ctitical(parent,title,text,button,defaultButton)      弹出严重错误对话框
	about(parent,title,text,button,text)		      弹出关于对话框
	setTitle()					      设置标题
	setText()					      设置消息正文
	setIcon()					      设置弹出对话框的图片
	
	QMessageBox的标准按钮类型：
							QMessage.OK       同意操作
							QMessage.Cancel   取消操作
							QMessage.Yes      同意操作
							QMessage.NO       取消操作
							QMessage.Abort    中止操作
							QMessage.Retry    重试操作
							QMessage.Ignore   忽略操作
							
	QMessageBox.information(self,"标题",“消息对话框正文”,QMessageBox.Yes | QMessage.NO, QMessage.Yes)	
```

## QInputDialog(标准对话框)
	QInputDialog控件是一个标准对话框，由一个文本框和两个按钮（OK按钮和Cancel按钮）组成。
	当用户单击Ok按钮或按Enter键后，在父窗口可以收集通过QInputDialog控件输入的信息
```python
	getInt()       从控件中获得标准整数输入
	getDouble()    从控件中获得浮点数输入
	getText()      从控件中获得标准字符串输入
	getItem()      从控件中获得列表里的选项输入
```

## QFontDialog(字体选择对话框)
	可以让用户选择所显示文本的字号大小，样式和格式
## QFileDialog(打开和保存文件的对话框)
```python
	getOpenFileName()    返回用户所选择文件的名称，并打开该文件
	getSaveFileName()    使用用户选择的文件名并保存文件
	setFileMode()        可以选择的文件类型，枚举常量是：
						QFileDialog.anyFile   任何文件
						QFileDialog.ExistingFile  已存在的文件
						QFileDialog.Directory     文件目录
						QFileDialog.ExistingFiles  已经存在的多个文件
						
	setFilter()         设置过滤器，只显示过滤器允许的文件类型
```
# 窗口绘图类控件
	一般可以通过QPainter，Qpen, QBrush来实现绘图功能
## QPainter
	在QWidget上执行绘图操作，它是一个绘图工具。
## QPen
	Qpen(钢笔)是一个基本的图形对象，用于绘制直线，曲线或者给轮廓画出矩形，椭圆形，多边形
## QBrush
	QBrush(画刷)是一个基本的图形对象，用于填充如矩形，椭圆形，多边形的形状\
## Drag和Drop（拖拽和剪贴板）
	为用户提供直观的拖拽功能，复制或移动对象
## Calendar(日历与时间)
	QCalendar是一个日历控件，它提供了一个基于月份的视图，允许用户通过鼠标或键盘选择日期，
	默认选中的是今天的日期，也可以对日历的日期范围进行规定。
## QDateTimeEdit
	是一个允许用户编辑日期时间的控件。
	QDateEdit和QTimeEdit都是QDateTimeEdit的子类
	
# 菜单栏、工具栏与状态栏
## QMenuBar(菜单栏)
```python
	menuBar()	返回主窗口的QMenuBar对象
	addMenu()       在菜单栏中添加一个新的QMenu对象
	addAction()     向QMenu小控件中添加一个操作按钮，其中包含文本或图标
	setEnabled()	将操作按钮状态设置为启用/禁用
	addSeperator()  在菜单中添加一条分隔线
	clear()		删除菜单/菜单栏的内容
	setShortcut()   将快捷键关联到操作按钮
	setText()	设置菜单项的文本
	setTitle()	设置QMenu小控件的标题
	text()		返回与QAction对象关联的文本
	title()		返回QMenu小控件的标题
```
## QToolBar
	由文本按钮，图标或其他小控件按钮组成的可移动面板，通常位于菜单栏下方
```python
	addAction()     添加具有文本或图标的工具按钮
	addSeperator()  分组显示工具按钮
	addWidget()	添加工具栏中按钮以外的控件
	addToolBar()	使用QMainWindow类的方法添加一个新的工具栏
	setMovable()	工具栏变的可移动
	setOrientation()  工具栏的方向可以设置为Qt.Horizontal或Qt.vertical
	
	QToolBar的信号：
	        actionTriggered；每当单击工具栏中的按钮时，都将发射这个信号
```

## QStatusBar
	MainWindow对象在底部保留有一个水平条，作为状态栏(QStatusBar)，用于显示永久的或临时的状态信息
```python
	self.statusBar = QStatusBar()
	self.setStatusBar(self.statusBar)

    	addWidget()		在状态栏中添加给定的窗口小控件对象
	addPermanentWidget()    在状态栏中永久添加给定的窗口小控件对象
	showMessage()    	在状态栏中显示一条临时信息指定时间间隔
	clearMessage()		删除正在显示的临时信息
	removeWidget()		从状态栏中删除指定的小控件
```
## Printer
	打印图像是图像处理软件中的一个常用功能。

# 表格和树
## QTableView
	一个应用需要和一批数据（比如数组、列表）进行交互，然后以表格的形式输出这些信息
```python
	QStringListModel()        			存储一组数据
	QStandardItermModel(4,4)		  	存储任意层次结构的数据
	QDirModel()					对文件系统进行封装
	QSqlQucryModel()				对SQL的查询结果集进行封装
	QSqlTableModel()				对SQL中的表格进行封装
	QSqlRelationalTableModel()			对带有foreign key 的SQL表格进行封装
	QSortFilterProxyModel()				对模型中的数据进行排序或过滤	
```
## QListView
	用于展示数据，QListView是基于模型(Model)的，需要程序来建立模型，然后保存数据
```python
	setModel()		用来设置View所关联的Model,可以使用Python原生的list作为数据源Model
	selectedItem()		选中Model中的条目
	isSelected()		判断Model中的某条目是否被选中
	
	QListView的信号：
			clicked            当单击某项时，信号被发射
			doubleClicked	   当双击某项时，信号被发射
```

## QListWidget
	是一个基于条目的接口，用于从列表中添加或删除条目，列表中的每个条目都是一个QListWidgetItem对象
```python
	addItem()  			在列表中添加QListWidgetItem对象或字符串
	addItems()			添加列表中的每个条目
	insertItem()                    在指定的索引处插入条目
	clear()				删除列表的内容
	setCurrentItem()	        设置当前所选条目
	sortItem()			按升序重新排列条目
	
	QListWidget的信号：
				currentItemChanged          当列表中的条目发生改变时，发射此信号
				itemClicked		    当点击列表中的条目时，发射此信号
```

## QTableWidget
	QTabWidget是Qt程序中常用的显示数据表格的空间，它使用标准的数据模型，并且其单元格数据是通过QTableWidgetItem对象来实现的。
	使用QTableWidget时就需要QTableWidgetItem,用来表示表格中的一个单元格，整个表格就是用各单元格构建起来的
```python
	setRowCount(int row)   				设置QTableWidget表格控件的行数
	setColumnCount(int col)                         设置QTableWidget表格控件的列数	
	setHorizontalHeaderLabels()			设置QTableWidget表格控件的水平标签
	setVerticalHeaderLabels()			设置QTableWidget表格控件的垂直标签
	setItem(int,int,QTableWidgetItem)	        在QTableWidget表格控件的每个选项的单元空间里添加控件
	horizontalHeader()				获取QTableWidget表格控件的表格头，以便执行隐藏
	rowCount()					获得QTableWidget表格的行数
	columnCount() 					获得QTableWidget表格的列数
	setEditTriggers(EditTriggers triggers)		设置表格是否可编辑，设置编辑规则的枚举值
	setSelectionBehavior()				设置表格的选择行为
	setTextAlignment()				设置单元格内文字的对齐方式
	setSpan(int row,int column,int rowSpanCount,int columnSpanCount)   合并单元格，要改变单元格的第Row行第column列，
									   要合并rowSpanCount行数和columnSpanCount列数
																	   
	setShowGrid()					在默认情况下，表格的显示是有网格线的
										true：显示网格线
										false：不显示网格线
	setColumnWidth(int column,int width)	        设置单元格的宽度
	setRowHeight(int row,int height)		设置单元格的高度
	
	setEditTriggers(EditTriggers triggers) 编辑规则的枚举值类型：
								QAbstractItemView.NoEditTriggers0No     	 0     	不能对表格内容进行修改
								QAbstractItemView.CurrentChange1Editing 	 1	任何时候都能对单元格进行修改
								QAbstractItemView.DoubleClicked2Editing          2	双击单元格
								QAbstractItemView.SelectedClicked4Editting       4	单击已选中的内容	
								QAbstractItemView.EditKeyPressed8Editing	 8	当修改键被按下时修改单元格
								QAbstractItemView.AnyKeyPressed16Editing	 16	按下任意键时修改单元格
								QAbstractItemView.AllEditTriggers31Editing       31	包括以上所有条件
											
	
	setSelectionBehavior() 表格选择行为的枚举值类型：
								QAbstractItemView.SelectItem0Selecting       0      选中单个单元格
								QAbstractItemView.SelectRowslSelecting	     1	    选中一行
								QAbstractItemView.SelectColumns2Selecting    2	    选中一列

	setTextAlignment()					设置单元格内文字的水平对齐方式
	                                                                                Qt.AlignLeft             将单元格的内容沿单元格的左边缘对齐
											Qt.AlignRight			 将单元格的内容沿单元格的右边缘对齐
											Qt.AlignHCenter			 在可用空间中，居中显示在水平方向上
											Qt.AlignJustify			 将文本在可用空间中对齐，默认是从左到右
											
								设置单元格内文字的垂直对齐方式
											Qt.AlignTop      		与顶部对齐
											Qt.AlignBottom			与底部对齐
											Qt.AlignVCenter                 在可用空间中，居中显示在垂直方向上
											Qt.AlignBaseline		与基线对齐
```

## QTreeView(树形结构)
	树形结构是通过QTreeWidget和QTreeWidgetItem实现的，其中QTreeWidgetItem类实现了节点的添加
```python
QTreeWidget的方法：
	setColumnWidth(int column, int Width)      将指定列的宽度设置为给定的值
								 Column  指定的列
								 Width   指定列的宽度
											   
	insertTopLevelItems()			   在视图的顶层索引中插入项目列表
	expandAll()				   展开所有的树形节点
	invisibleRootItem()			   返回所有选定的非隐藏项目的列表
	
	
	QTreeWidgetItem中的常用的方法：
				    addChild()			将子项追加到子列表中
				    setText()			设置显示的节点文本
				    Text()			返回显示的节点文本
				    setCheckState()		设置指定列的选中状态：
										Qt.Checked   节点选中
										Qt.Unchecked  节点未选中
				    setIcon(column,icon)        在指定的列中显示图标
```

## QTabWidget
	QTabWidget控件提供了一个选项卡和一个页面区域，默认先死第一个选项卡的页面。
```python
	addTab()                  将一个控件添加到Tab控件的选项卡中
	insertTab()	          将一个Tab控件的选项卡插入到指定的位子
	removeTab()		  根据指定的索引删除Tab控件
	setCurrentIndex()	  设置当前可见的选项卡所在的索引
	setCurrentWidget()	  设置当前可见的页面
	setTabBar()		  设置选项卡栏的小控件
	setTabPosition()	  设置选项卡的位置：
						QTabWidget.North       显示在页面的上方
						QTabWidget.South       显示在页面的下方
						QTabWidget.West        显示在页面的右侧
						QTabWidget.East        显示在页面的右侧
	setTabText()		  定义Tab选项卡的显示值
	
	QTabWidget的信号：
			  currentChanged      切换当前页面时发射该信号
```

## QStackedWidget
	是一个堆栈窗口控件，可以填充一些小控件，但是同一时间只有一个小控件可以显示。
	QStackedWidget使用QStackedLayout布局。
```python
	addWidget()               在堆栈窗口控件，添加控件
	setCurrentIndex()	  设置当前可见的选项卡所在的索引
	QStackedWidget的信号：
			  currentChanged      切换当前页面时发射该信号
```

## QDockWidget
	是一个可以停靠在QMainWindow内的窗口控件，它可以保持在浮动状态或者在指定位置作为子窗口附加到主窗口中。
```python
	setWidget()                     在Dock窗口区域设置QWidget
	setFloating()			设置Dock窗口是否可以浮动，如果设置为True，则表示可以浮动
	setAllowedAreas()		设置窗口可以停靠的区域：
							LeftDockWidgetArea     左边停靠区域
							RightDockWidgetArea    右边停靠区域
							TopDockWidgetArea      顶部停靠区域
							BottomDockWidgetArea   底部停靠区域
							NoDockWidgetArea       不显示widget
			
	setFeatures()			设置停靠窗口的功能属性：
							DockWidgetClosable                 可关闭
							DockWidgetMovable                  可移动
							DockWidgetFloable		   可漂浮
							DockWidgetVerticalTitleBar	   在左边显示垂直的标签栏
							AllDockWidgetFeatures		   具有前三种属性的所有功能
							NoDockWidgetFeatures               无法关闭，不能移动，不能漂浮
```

# 多文档界面
	创建多个独立的窗口，每个窗口都可以有自己的菜单系统，工具栏。
	MDI应用程序占用较小的内存资源，子窗口都可以放在主窗口的容器中，这个容器控件被称为QMdiArea
## QMdiArea	
	QMdiArea控件通常占据在QMainWindow对象的中央位子，子窗口在这个区域是QMdiSubWindow类的实例，可以设置任何QWidget作为子窗口对象的内部控件
```python
	QMdiArea和QMdiSubWindow的常用方法：
			addSubWindow()					将一个小控件添加在MDI区域作为一个新的子窗口
			removeSubWindow()				删除一个子窗口中的小控件
			setActiveSubWindow()                            激活一个子窗口
			cascadeSubWindows()				安排子窗口在MDI区域级联显示
			tileSubWindows()				安排子窗口在MDI区域平铺显示
			closeActiveSubWindow()			        关闭活动的子窗口
			subWindowList()					返回MDI区域的子窗口列表
			setWidget()					设置一个小控件作为QMdiSubwindow实例对象的内部控件
```

## QScrollBar
	这个窗口控件提供了水平的或垂直的滚动条，这样可以扩大当前窗口的有效装载面积，从而装在更多的控件
```python
	QScrollBar的信号:
			valueChanged             当滑动条的值改变时发射此信号
			sliderMoved		 当用户拖动滑块时发射此信号
```

# 多线程
	多线程技术涉及三种方法，一种是使用计时器模块QTimer,一种是使用多线程模块QThread，还有一种是使用事件处理的功能
## QTimer(定时器)
	在应用程序中周期性的进行某项操作，QTimer提供了重复的和单次的定时器。
	要使用定时器，需要先创建一个QTimer实例，将其timeout信号连接到相应的槽，并调用start().
	然后，定时器会已恒定的间隔发出timeout信号。
	当窗口控件收到timeout信号后，他就会停止这个定时器。
```python
常用方法：
	start(milliseconds)				启动或重新启动定时器，时间间隔为毫秒。如果定时器已经运行，他将被停止并重新启动。
							如果singleShot信号为真，定时器将仅被激活一次
	stop()				停止定时器
			
	QTimer的信号：
		singleshot 					在给定的时间间隔后调用一个槽函数时发射此信号
		timeout						当定时器超时时发射此信号
				
		获取系统现在的时间：
		time = QDateTime.currentDateTime()
		
		设置系统时间显示格式：
		timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
		
		在标签上显示时间：
		self.label.setText(timeDisplay)
		
		无边框窗口：
		self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
```
## QThread(线程)
	QThread是Qt线程类中最核心的底层类。由于PyQt的跨平台特性，QThread要隐藏所有与平台相关的代码
	要使用QThread开始一个线程，可以创建它的一个子类，然后覆盖其QThread.run()函数
```python
	class Example(QThread):
		def __init__(self):
			super().__init__()
				
		def run(self):
			pass
			
		接下来创建一个新的线程：
		thread = Thread()
		thread.start()
		
	
		QThread的常用方法：
			start() 		启动线程
			wait()			阻止线程，直到满足如下条件之一：
									与此QThread对象关联的线程已完成执行(即从run()返回时)。
									如果线程完成执行，此函数将返回True；如果线程尚未启动此函数也返回True
															
									等待时间的单位是毫秒。如果时间是ULONG_Max(默认值)，则等待
									永远不会超时(线程必须从run()返回);如果等待超时将返回False
															
			sleep()			强制当前线程睡眠
			
			
		QThread的信号：
			started                 在开始执行run()函数之前，从相关线程发射此信号
			finshed			当程序完成业务逻辑时，从相关线程发射此信号
```


# QWidgets 
	小部件是pyside2中所有用户界面对象的基类。默认构造函数没有父类，没有父类口小部件称为窗口。

  - resize() 调整窗口小部件的大小

  - move()  移动小部件在屏幕的位置。

  - setWindowTitle() 设置窗口的标题

  - setWindowIcon(icon) 设置窗口的图标      icon – PySide2.QtGui.QIcon

  - setGeometry(x,y,wight,hight)  在屏幕上定位窗口并设置它的大小  x y  wight hight

  - show()  在屏幕上显示窗口小部件，首先在内存中创建，在屏幕上显示





# QPushButton  按钮的类
```python
button = QPushButton('xxx',self)  创建一个按钮的对象。第一个参数是按钮的标签，第二个是父窗口小部件 

button.clicked(“槽”) 如果我们点击按钮，点击的信号发出。 槽可以是Qt槽函数，或者Python可调用的函数。

button.resize() 设置按钮大小

button.move() 设置按钮的位置

button.setToolTip() 使用富文本格式
```




# QCoreApplication  包含主事件循环，它处理和调度所有事件
```python
QCoreApplication.instance() 对象实例化
```


# QLineEdit   编辑文本框
```python
self.text = QLineEdit('在这里输入数字', self)      在窗口小部件上，添加一个文本框
self.text.selectAll()          可以理解为将“在这里输入数字”进行全选                 
self.text.setFocus()		   setFocus()就是让输入焦点置于文本栏中，方便用户输入，不然还得手动在文本栏中单击一下，很是麻烦。
self.text.setGeometry(80, 50, 150 ,30)   设置文本框的大小
```



# QMessageBox 弹出对话框
```python
QMessageBox.about(self, '看结果','猜大了!')就是弹出一个对话框，告诉你结果是什么样的。  第一个参数是 PySide2.QtWidgets.QWidget（self），第二个是弹出对话框的标题，第三个是对话框弹出的内容

QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  第一个字符串出现在标题栏上。 第二个字符串是对话框显示的消息文本。 第三个参数指定出现在对话框中的按钮的组合。 最后一个参数是默认按钮。 它是初始键盘焦点的按钮。 返回值存储在答复变量中。
```





# 事件与信号处理
在事件模型中，有三个参与者：
1.事件来源    是状态更改的对象，他会生成事件。
2.事件对象    将状态更改封装在事件源中
3.事件目标    是要通知的对象

```python
QtGui.QLCDNumber(self) 窗口上设置一个LCD屏
QtGui.QDial(self)       窗口上设置一个轮盘
dial.valueChanged.connect(lcd.display)  这里我们将QDial这个小部件的一个valueChanged信号连接到lcd数字的显示槽。
QDial对象发送信号。 QLCDNumber接收信号的。 槽是对信号作出反应的方法。
```

## 事件处理重写
```python
self.setMouseTracking(True)   启动鼠标跟踪
当鼠标滑动时，事件发生启动
def mouseMoveEvent(self, event):
```

## 事件发送者信号
```python
窗口小部件发送信号： sender()
bt1 = QPushButton('xx',self)
bt1.clicked.connect(self.函数)

def 函数():
    sender = self.sender()
	sender.text() == 'xx' (可以检测哪个按钮被按下)
``` 


## 自定义信号
```python
from PyQt5.QtCore import (Signal, QObject)
class Signal(QObject):
    showmouse = Signal()

self.s = Signal()
        self.s.showmouse.connect(self.about)
		
   def about(self):
        QMessageBox.about(self,'鼠标','你点鼠标了吧！')
```		

## 布局
### 箱式布局
    
    QHBoxLayout和QVBoxLayout是基本的布局类
	
	hbox = QHBoxLayout() 创建一个水平框布局
	hbox.addStretch(1)    创建一个拉伸因子  （就是两个框之间的距离） 这个拉伸在三个按钮之前增加了一个可伸缩的空间。这将把它们推到窗口的右边。

 
	vbox = QVBoxLayout()   水平放置在垂直布局中。
	vbox = addStretch(1)   垂直框中的拉伸因子将按钮的水平框推到窗口的底部
        vbox.addLayout(hbox)   水平布局放置在垂直布局中  
   
	self.setLayout(vbox)   设置窗口的主要布局
	
        addStretch函数的作用是在布局器中增加一个伸缩量
	
	
### 格栅布局
	QGridLayout   也称为网格布局(多行多列)
                      将提供给它的空间划分成行和列，并在每个窗口部件插入并管理到正确的单元格 
				  
				  
### 表单布局
	QFormLayout  管理输入型控件和关联的标签组成的那些Form表单
	
# 界面搭建
      QMainWindow类提供了一个主应用程序窗口。 这使得能够创建具有状态栏，工具栏和菜单栏的经典应用程序框架。
## 状态栏
      要获取状态栏，我们需要调用QWidget.QMainWindow类的statusBar()方法
      该方法的第一个调用创建一个状态栏，后续调用返回状态栏对象。
      showMessage() 在状态栏上显示一条消息
## 菜单
```python
	    exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
	    exitAct.setShortcut('Ctrl+Q')
	    exitAct.setStatusTip('退出程序')
``` 
	    QAction是使用菜单栏，工具栏或自定义键盘快捷方式执行操作的抽象。
	    创建一个具有特定图标和”退出“标签的动作
	
	    exitAct.triggered.connect(qApp.quit)
	    当我们选择这个特定的动作时，发出触发信号，信号连接到QApplication小部件的quit()方法。 这终止了应用程序。
```python	
	    menubar = self.menuBar()
	    fileMenu = menubar.addMenu('文件(&F)')
	    fileMenu.addAction(exitAct)
``` 		
	    menuBar()方法创建一个菜单栏。我们使用addMenu()创建文件菜单，并使用addAction()添加操作。
            &”这个符号，增加这个符号后，当我们按住”Alt+F“的时候就能快速打开文件这个菜单

## 子菜单
	    使用QMenu创建新菜单
```python
	    saveMenu = QMenu('保存方式(&S)', self)
	    saveAct = QAction(QIcon('save.png'),'保存...', self)
	    saveAct.setShortcut('Ctrl+S')
	    saveAct.setStatusTip('保存文件')
	    saveasAct = QAction(QIcon('saveas.png'),'另存为...(&O)', self)
	    saveasAct.setStatusTip('文件另存为')
	    saveMenu.addAction(saveAct)
	    saveMenu.addAction(saveasAct)
```	    
	    使用addAction()被添加到子菜单中
## 上下文菜单
```python
       def contextMenuEvent(self, event):
       cmenu = QMenu(self)
       newAct = cmenu.addAction("新建")
       opnAct = cmenu.addAction("保存")
       quitAct = cmenu.addAction("退出")
       action = cmenu.exec_(self.mapToGlobal(event.pos()))
       if action == quitAct:
           qApp.quit()
```
	   重新实现contextMenuEvent()方法，使用exec_()方法显示上下文菜单。 从事件对象获取鼠标指针的坐标。 mapToGlobal()方法将窗口小部件坐标转换为全局屏幕坐标。

# 学习计划：
### 时间1月26日-1月29日
    - 数据类型
    - 字符串和编码
    - 条件判断
    - 循环
    - 函数
    - 开发环境搭建
    -  widget窗口小组件
    -  button按钮部件
    - Icon窗口标题
    - 事件与信号处理
  
### 达成目标:可以设置窗口小部件，给窗口小部件设置图标，添加按钮，触发事件处理

### 时间：2月1日-2月5日
    - python特性
    - 函数编程
    - 模块
    - 面向对象
    - 面向高级对象
    - 布局
    - 界面搭建
    - 标准输入对话框
    - 进度对话框
    
### 时间: 2月17日-2月19日
    - 复选框
    - 单选按钮
    - 标签
    - 文本输入栏
    - 纯文本输入框
    - 写出一个类似QQ的界面
### 达成目标：可以写出一个类似QQ一样的操作界面
     
### 时间：2月22日-2月26日
    - io编程
    - 进程和线程
    - 常用内建模块
    - 图形界面
    - 网络编程
    - 访问数据库
    
### 时间：3月1日-3月5日
    - QListView高级部件
    - QTreeWidget部件
    - QTabWidget部件
    - QTableWidget部件
    
### 时间：3月8日-3月12日
    - QTimer与QThread的综合应用
    - Web页面交互初探
    - 与数据库互联
    - 局域网小工具
    
### 时间：3月12日-3月15日
    - Graphics View
    - DIY浏览器
    
### 达成目标：可以写出一个类似局域网聊天工具和diy一个浏览器
### 终极目标：实现一个类似野火的操作界面

