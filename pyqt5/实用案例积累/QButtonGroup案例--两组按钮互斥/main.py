# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)

#创建两组单选按钮
rb_nan = QRadioButton("男", window)
rb_nan.move(100,100)
rb_nv = QRadioButton("女", window)
rb_nv.move(100,150)
#创建第一个按钮组
sex_group = QButtonGroup(window)
sex_group.addButton(rb_nan)
sex_group.addButton(rb_nv)

rb_yes = QRadioButton("是", window)
rb_yes.move(300,100)
rb_no = QRadioButton("否", window)
rb_no.move(300,150)

#创建第二个按钮组
answer_group = QButtonGroup(window)
answer_group.addButton(rb_yes)
answer_group.addButton(rb_no)

window.show()
sys.exit(app.exec_())