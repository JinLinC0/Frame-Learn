# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Mylabel(QLabel):
    def keyPressEvent(self, evt):  #可以通过ctrl键+点击QKeyEvent查看相关方法
        if evt.key() == Qt.Key_Tab:
            print("用户点击了Tab键位")
        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            print("用户点击了ctrl + s")
        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:
            print("用户点击了ctrl + Shift + a")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("监听用户按键")
window.resize(500,500)

label = Mylabel(window)
label.resize(200,200)
label.move(100,100)
label.setStyleSheet("background-color: cyan;")
label.grabKeyboard()  #标签去捕获键盘,所有的键盘按键都会传递给标签按键进行接收

window.show()
sys.exit(app.exec_())