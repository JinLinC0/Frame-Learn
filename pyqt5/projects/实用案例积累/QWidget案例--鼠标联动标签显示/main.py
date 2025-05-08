# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Mylabel(QLabel):
    def enterEvent(self, QEvent):
        self.setText("欢迎光临")

    def leaveEvent(self, QEvent):
        self.setText("谢谢惠顾")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("鼠标联动标签显示")
window.resize(500,500)

label = Mylabel(window)
label.resize(200,200)
label.move(100,100)
label.setStyleSheet("background-color: cyan;")

window.show()
sys.exit(app.exec_())