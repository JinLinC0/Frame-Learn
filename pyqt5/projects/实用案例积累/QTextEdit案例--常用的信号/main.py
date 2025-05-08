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
        self.te.textChanged.connect(self.text_change)
        self.te.selectionChanged.connect(self.select_change)
        self.te.copyAvailable.connect(self.copy_a)

    def text_change(self):
        print("文本内容发生了改变！")

    def select_change(self):
        print("选中文本内容发生了改变！")

    def copy_a(self, yes):
        print("复制是否可用", yes)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())