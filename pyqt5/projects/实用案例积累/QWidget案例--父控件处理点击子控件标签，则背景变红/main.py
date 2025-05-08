# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

#方法一：重写继承方法,自定义QLabel控件
#class Label(QLabel):
#	def mousePressEvent(self, QMouseEvent):
#		self.setStyleSheet("background-color: red;")

#方法二，通过父控件处理
class Window(QWidget):
	def mousePressEvent(self, evt):
		local_x = evt.x()
		local_y = evt.y()
		sub_widget = self.childAt(local_x,local_y)
		if sub_widget is not None:  #如果没有在给定坐标中找到子控件，会返回None，进行判断，防止点击空白部分程序崩溃
			sub_widget.setStyleSheet("background-color: red;")

app = QApplication(sys.argv)
window = Window()

#批量创建标签
for i in range(1,11):
	#label = Label(window)  #对应方法一的继承
	label = QLabel(window)
	label.setText("标签" + str(i))
	label.move(40*i,40*i)

window.show()
sys.exit(app.exec_())