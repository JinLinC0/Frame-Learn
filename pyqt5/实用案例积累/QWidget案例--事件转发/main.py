# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print("顶层窗口被按下")

class MidWindow(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print("中间控件被按下")

class Label(QLabel):  #标签一般不出来事件，若点击标签，就转发事件给父对象进行处理，标签的父对象是mid_window，点击标签也会显示中间控件被按下
    pass
    #def mousePressEvent(self, QMouseEvent):
        #print("标签控件鼠标按下")

class Label1(QLabel):
    def mousePressEvent(self, evt):
        print("标签控件鼠标按下")
        #evt.accept()
        evt.ignore()

app = QApplication(sys.argv)
window = Window()
window.setWindowTitle("事件转发")
window.resize(500,500)

mid_window = MidWindow(window)
mid_window.resize(300,300)
mid_window.setAttribute(Qt.WA_StyledBackground, True)  #让中间控件的样式生效
mid_window.setStyleSheet("background-color: yellow;")

label = Label(mid_window)
label.setText("这是一个标签")
label.setStyleSheet("background-color: red;")
label.move(100,100)

label1 = Label1(mid_window)
label1.setText("这是一个标签1")
label1.setStyleSheet("background-color: red;")
label1.move(200,200)

window.show()
sys.exit(app.exec_())