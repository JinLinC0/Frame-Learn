# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class MyWindow(QWidget):  #创建一个子类，子类中没有的方法则去父类中找
    def __init__(self):
        super().__init__()
        self.setWindowTitle("鼠标移动")
        self.resize(500, 500)
        self.move(200,200)
        self.setMouseTracking(True)  # 开启鼠标跟踪，鼠标左键不点击也会触发mouseMoveEvent事件

        label = QLabel(self)
        self.label = label
        label.setText("这是一个标签")
        label.move(100, 100)
        label.setStyleSheet("background-color: cyan;")

    def mouseMoveEvent(self, me):
        print("鼠标移动了", me.localPos())  #触发mouseMoveEvent事件需要鼠标左键点击并拖动
        self.label.move(me.localPos().x(), me.localPos().y())

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())