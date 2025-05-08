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
        self.btn.setText("相关事件")
        self.btn.clicked.connect(self.btn_cao)

    def btn_cao(self):
        #self.字体提示窗口()
        #self.字体设置()
        self.统一字体格式设置()

    def 字体提示窗口(self):
        QFontDialog.getFont()

    def 字体设置(self):
        self.te.setFontFamily("幼圆")  #设置字体家族
        self.te.setFontWeight(QFont.Black)  #设置字体的粗细
        self.te.setFontItalic(True)  #设置字体倾斜
        self.te.setFontPointSize(20)  #设置字体大小
        self.te.setFontUnderline(True)  #设置字体下划线

    def 统一字体格式设置(self):
        font = QFont()
        font.setFamily("幼圆")  #设置字体家族
        font.setStrikeOut(True)  #设置删除线
        self.te.setCurrentFont(font)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())