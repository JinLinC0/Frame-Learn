# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class InputdialogDemo(QWidget):
    def __init__(self, parent=None):
        super(InputdialogDemo, self).__init__(parent)
        layout = QFormLayout()
        self.btn1 = QPushButton("获得列表里的选项")  #创建按钮
        self.btn1.clicked.connect(self.getItem)  #点击按钮发射clicked函数，连接到槽函数getItem
        self.le1 = QLineEdit()    #创建单行文本框，用于显示读取的信息
        layout.addRow(self.btn1, self.le1)

        self.btn2 = QPushButton("获得字符串")
        self.btn2.clicked.connect(self.getIext)
        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)

        self.btn3 = QPushButton("获得整数")
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()
        layout.addRow(self.btn3, self.le3)
        self.setLayout(layout)
        self.setWindowTitle("Input Dialog 例子")

    def getItem(self):
        items = ("C", "C++", "Java", "Python")  #往列表中加入四个内容
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "语言列表", items, 0, False)
        #调用静态方法QInputDialog.getItem对话框，编辑相关信息，允许用户从QCombox中选择一个选项，允许用户确认和取消操作。
        if ok and item:
            self.le1.setText(item)  #在单行文本框中写入读取的数据

    def getIext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', '输入姓名:')
        if ok:
            self.le2.setText(str(text))

    def getInt(self):
        # num, ok = QInputDialog.getInt(self, "integer input dualog", "输入数字")
        # if ok:
        #     self.le3.setText(str(num))
        ind = QInputDialog(self)
        ind.setInputMode(QInputDialog.IntInput)
        ind.setIntRange(0, 100)
        ind.setIntStep(2)
        ind.intValueSelected.connect(lambda val: self.le3.setText(str(val)))
        ind.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = InputdialogDemo()
    demo.show()
    sys.exit(app.exec_())