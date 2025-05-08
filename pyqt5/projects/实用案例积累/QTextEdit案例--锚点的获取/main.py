# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class MyTextEdit(QTextEdit):  #重写QTextEdit中的鼠标点击事件
    def mousePressEvent(self, me):
        link_str = self.anchorAt(me.pos()) #获取锚点中对应的链接地址
        if len(link_str) > 0:
            QDesktopServices.openUrl(QUrl(link_str))  #桌面服务的方法打开网址

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        self.te = MyTextEdit(self)
        self.te.move(120, 120)
        self.te.insertHtml("<a href = 'https://www.baidu.com/'>百度</a>")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())