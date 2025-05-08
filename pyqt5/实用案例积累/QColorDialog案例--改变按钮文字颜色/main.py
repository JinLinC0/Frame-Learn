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
        btn = QPushButton(self)
        btn.move(100,100)
        btn.setText("测试按钮")
        btn.clicked.connect(self.test)
        self.btn = btn

    def test(self):
        cd = QColorDialog(self)
        def sel_color(color):
            palette = QPalette()  # 创建调色板对象
            palette.setColor(QPalette.ButtonText, color)
            self.btn.setPalette(palette)
        #cd.colorSelected.connect(sel_color)  #最终颜色确定时发射信号
        cd.currentColorChanged.connect(sel_color)
        cd.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())