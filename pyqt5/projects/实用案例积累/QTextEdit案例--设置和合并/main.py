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
        self.te.setText("xxx")
        self.btn = QPushButton(self)
        self.btn.move(200,50)
        self.btn.setText("光标事件")
        self.btn.clicked.connect(self.cao)

    def cao(self):
        #setBlockCharFormat(QTextCharFormat)方法
        #tc = self.te.textCursor()
        #tcf = QTextCharFormat()
        #tcf.setFontFamily("幼圆")
        #tcf.setFontPointSize(20)
        #tc.setBlockCharFormat(tcf)

        #setBlockFormat(QTextBlockFormat)方法
        #tc = self.te.textCursor()
        #tbf = QTextBlockFormat()
        #tbf.setAlignment(Qt.AlignCenter)  #设置中间对齐，当一行没有被填满时，该行文本居中显示
        #tbf.setIndent(1)
        #tc.setBlockFormat(tbf)

        #setCharFormat(QTextCharFormat)方法
        tc = self.te.textCursor()
        tcf = QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(20)
        tc.setCharFormat(tcf)

        #mergeCharFormat(QTextCharFormat)方法
        #结合原先的setCharFormat()设置方法
        tc2 = QTextCharFormat()
        tc2.setFontOverline(True)
        tc.mergeCharFormat(tc2)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())