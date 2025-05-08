# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class CheckBoxDemo(QWidget):
    def __init__(self, parent=None):
        super(CheckBoxDemo, self).__init__(parent)

        groupBox = QGroupBox("Checkboxes")   #建立QGroupBox组，并命名，其功能可以把许多复选框组织在一起
        groupBox.setFlat(False)

        layout = QHBoxLayout()   #复选框进行水平布局
        #第一个复选框，设置了快捷键，快捷键可以选中该复选框，实例化一个QCheckBox类对象checkBox1，两种状态选择
        self.checkBox1 = QCheckBox("&Checkbox1")
        self.checkBox1.setChecked(True)   #设置初始状态为选中
        self.checkBox1.stateChanged.connect(lambda: self.btnstate(self.checkBox1)) #状态改变发送信号连接到槽函数
        layout.addWidget(self.checkBox1)
		#第二个复选框，实例化一个QCheckBox类对象checkBox2，两种状态选择
        self.checkBox2 = QCheckBox("Checkbox2")
        self.checkBox2.toggled.connect(lambda: self.btnstate(self.checkBox2))
        layout.addWidget(self.checkBox2)
		#第三个复选框，实例化一个QCheckBox类对象checkBox3，三种状态选择
        self.checkBox3 = QCheckBox("tristateBox")
        self.checkBox3.setTristate(True)   #开启三态模式
        self.checkBox3.setCheckState(Qt.PartiallyChecked)   #设置初始状态为半选中
        self.checkBox3.stateChanged.connect(lambda: self.btnstate(self.checkBox3))
        layout.addWidget(self.checkBox3)

        groupBox.setLayout(layout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)

        self.setLayout(mainLayout)
        self.setWindowTitle("checkbox demo")

    def btnstate(self, btn):   #使用isChecked()方法，判断复选框是否被选中
        chk1Status = self.checkBox1.text() + ", isChecked=" + str(self.checkBox1.isChecked()) + ', chekState=' + str(
            self.checkBox1.checkState()) + "\n"
        chk2Status = self.checkBox2.text() + ", isChecked=" + str(self.checkBox2.isChecked()) + ', checkState=' + str(
            self.checkBox2.checkState()) + "\n"
        chk3Status = self.checkBox3.text() + ", isChecked=" + str(self.checkBox3.isChecked()) + ', checkState=' + str(
            self.checkBox3.checkState()) + "\n"
        print(chk1Status + chk2Status + chk3Status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkboxDemo = CheckBoxDemo()
    checkboxDemo.show()
    sys.exit(app.exec_())