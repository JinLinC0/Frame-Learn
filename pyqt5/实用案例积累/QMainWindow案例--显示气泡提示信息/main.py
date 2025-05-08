# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QApplication
from PyQt5.QtGui import QFont

class Winform(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))    #是用来设置气泡提示的提示信息的字体与字号大小，有时字体会显示不出来
        self.setToolTip('这是一个<b>气泡提示</b>')    #设置显示内容的气泡提示
        self.setGeometry(200, 300, 400, 400)
        self.setWindowTitle('气泡提示demo')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())