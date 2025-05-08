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
        label = QLabel(self)
        label.setText("这是一个字体显示标签")
        label.move(100,100)

        fcb = QFontComboBox(self)
        fcb.currentFontChanged.connect(lambda font: label.setFont(font))
        fcb.setEditable(False)  #设置不能编辑，只能选中

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())