# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys
#python3.11环境下不能运行，切换至python3.9环境运行
app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
window.move(300,300)

widget_count = 20  #设置总控件个数
column_count = 3  #设置一行有多少列
widget_width = window.width() / column_count  #计算一个控件的宽度
row_count = (widget_count - 1) // column_count + 1  #计算总行数
widget_height = window.height() / row_count  #计算一个控件的高度
for i in range(0, widget_count):
    w = QWidget(window)
    w.resize(widget_width, widget_height)
    widget_x = i % column_count * widget_width
    widget_y = i // column_count * widget_height
    w.move(widget_x, widget_y)
    w.setStyleSheet("background-color: red;border: 1px solid yellow")
window.show()
sys.exit(app.exec_())