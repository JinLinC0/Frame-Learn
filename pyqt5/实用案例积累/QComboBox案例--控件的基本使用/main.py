# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ComboxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboxDemo, self).__init__(parent)
        self.setWindowTitle("combox 例子")
        self.resize(300, 90)
        layout = QVBoxLayout()
        self.lbl = QLabel("")

        self.cb = QComboBox()  #创建一个下拉框
        self.cb.addItem("C")   #addItem()方法去添加单个选项
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])  #addItems()方法添加多个选项
        self.cb.currentIndexChanged.connect(self.selectionchange)
        #当下拉列表框中的选项发生改变时将发射currentIndexChanged信号，连接到自定义的槽函数selectionchange()
        layout.addWidget(self.cb)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def selectionchange(self, i):  #槽函数selectionchange，当选中下拉列表框中的一个选项时，把选项文本设置为标签文本
        self.lbl.setText(self.cb.currentText())   #把选项文本设置为标签文本
        self.lbl.adjustSize()    #并调整标签大小

        print("Items in the list are :")
        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
            print("Current index", i, "selection changed ", self.cb.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec_())