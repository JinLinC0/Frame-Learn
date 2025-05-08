# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Radiodemo(QWidget):
    def __init__(self, parent=None):
        super(Radiodemo, self).__init__(parent)
        layout = QHBoxLayout()
        #设置按钮btn1，设置默认选中状态
        self.btn1 = QRadioButton("Button1")
        self.btn1.setChecked(True)   #设置默认是已点击的状态
        self.btn1.toggled.connect(lambda: self.btnstate(self.btn1))
        #当按钮状态变化时，触发toggled信号，与槽函数btnstate连接，使用lambda方式允许将信号源传递给槽函数，将按钮作为参数
        layout.addWidget(self.btn1)

        self.btn2 = QRadioButton("Button2")
        self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))
        layout.addWidget(self.btn2)
        self.setLayout(layout)
        self.setWindowTitle("RadioButton demo")

    def btnstate(self, btn):   #设置槽函数btnstate来检查按钮的状态
        if btn.text() == "Button1":    #text()返回按钮的显示文本
            if btn.isChecked() == True:   #判断按钮是否按下
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")

        if btn.text() == "Button2":
            if btn.isChecked() == True:
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    radioDemo = Radiodemo()
    radioDemo.show()
    sys.exit(app.exec_())