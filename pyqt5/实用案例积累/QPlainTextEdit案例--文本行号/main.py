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
        self.pte = QPlainTextEdit(self)
        self.pte.move(100, 100)
        self.pte.resize(300,300)
        self.btn = QPushButton(self)
        self.btn.move(200,50)
        self.btn.setText("相关事件")
        self.btn.clicked.connect(self.btn_cao)
        #展示行号控件
        line_num_parent = QWidget(self)
        line_num_parent.resize(30,300)
        line_num_parent.move(70,100)
        line_num_parent.setStyleSheet("background-color: cyan;")
        self.line_label = QLabel(line_num_parent)
        self.line_label.move(0,5)
        #1-100行号
        line_nums = "\n".join([str(i) for i in range(1,101)])
        self.line_label.setText(line_nums)

    def btn_cao(self):
        self.信号的操作()

    def 信号的操作(self):
        self.pte.updateRequest.connect(lambda rect, dy: self.line_label.move(self.line_label.x(),self.line_label.y() + dy))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())