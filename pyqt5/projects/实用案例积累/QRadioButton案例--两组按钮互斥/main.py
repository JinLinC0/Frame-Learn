# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
#为按钮组创建两个父控件，分别放一组按钮
red = QWidget(window)
red.resize(60,100)
red.setStyleSheet("background-color: red")
red.move(50,50)

green = QWidget(window)
green.resize(60,100)
green.setStyleSheet("background-color: green")
green.move(red.x() + red.width(), red.y() + red.height())

#创建两组单选按钮
rb_nan = QRadioButton("男", red)
rb_nan.move(10,10)
rb_nv = QRadioButton("女", red)
rb_nv.move(10,50)

rb_yes = QRadioButton("是", green)
rb_yes.move(10,10)
rb_no = QRadioButton("否", green)
rb_no.move(10,50)

window.show()
sys.exit(app.exec_())