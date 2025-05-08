# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        self.te = QTextEdit(self)
        self.te.move(120, 120)
        self.te.setText("123456789")
        self.btn = QPushButton(self)
        self.btn.move(200,50)
        self.btn.setText("光标事件")
        self.btn.clicked.connect(self.btn_cao)

    def btn_cao(self):
        self.文本的选中和清空()
    def 文本的选中和清空(self):
        tc = self.te.textCursor()  #设置文本光标对象
        #tc.setPosition(6, QTextCursor.KeepAnchor)   #将光标移动到第六个字符后面，将移动模式设置成将锚点(原先所在光标的位置)固定在原地，就可以实现选中效果
        #tc.movePosition(QTextCursor.End, QTextCursor.KeepAnchor, 1)
        tc.select(QTextCursor.BlockUnderCursor)
        self.te.setTextCursor(tc)  #将文本光标设置回去
        self.te.setFocus()  #重新获取焦点

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())