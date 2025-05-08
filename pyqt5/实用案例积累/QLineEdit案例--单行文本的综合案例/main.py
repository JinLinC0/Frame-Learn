# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        # 第一个文本框e1,
        e1 = QLineEdit()
        e1.setValidator(QIntValidator())  # 只允许输入整数
        e1.setMaxLength(4)  # 最大长度为4个字符
        e1.setAlignment(Qt.AlignRight)  # 右对齐
        e1.setFont(QFont("Arial", 20))  # 使用自定义字体，Arial样式，大小20
        # 第二个文本框e2
        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))  # 限制输入小数点到后两位
        # 第三个文本框e3
        e3 = QLineEdit()
        e3.setInputMask('+99_9999_999999')  # 需要输入一个掩码输入电话号码
        # 第四个文本框e4
        e4 = QLineEdit()
        e4.textChanged.connect(self.textchanged)  # 需要发射信号textChanged，连接到槽函数textchanged()
        # 第五个文本框e5
        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)  # 设置显示模式EchoMode为Password
        e5.editingFinished.connect(self.enterPress)  # 发射editingFinished按下回车信号函数enterPress()
        # 第六本框e6
        e6 = QLineEdit("Hello PyQt5")  # 显示一个默认文本，不能编辑
        e6.setReadOnly(True)  # 设置只读

        flo = QFormLayout()
        flo.addRow("integer validator", e1)
        flo.addRow("Double validator", e2)
        flo.addRow("Input Mask", e3)
        flo.addRow("Text changed", e4)
        flo.addRow("Password", e5)
        flo.addRow("Read Only", e6)
        self.setLayout(flo)
        self.setWindowTitle("QLineEdit例子")

    def textchanged(self, text):  # 自定义槽函数textchanged()，在e4中发生变化，则在pycharm打印变化
        print("输入的内容为: " + text)

    def enterPress(self):  # 自定义槽函数enterPress()，在e5一旦回车，就打印以下信息
        print("已输入值")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())