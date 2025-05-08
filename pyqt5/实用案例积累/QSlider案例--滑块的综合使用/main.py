# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Slider(QSlider):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setup_ui()

    def setup_ui(self):
        self.lb = QLabel(self)  # 在滑块控件中创建一个标签控件
        self.lb.setText("0")
        self.lb.setStyleSheet("color: red;")
        self.lb.hide()

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)  #为了保持父类中的完整性，我们只是增加功能，不是重写功能
        x: int = int((self.width() - self.lb.width()) / 2)  #居中效果
        y: int = int((1 - self.value() / (self.maximum() - self.minimum())) * self.height() - self.lb.height())
        self.lb.show()
        self.lb.move(x, y)

    def mouseMoveEvent(self, evt):
        super().mouseMoveEvent(evt)
        x: int = int((self.width() - self.lb.width()) / 2)  # 居中效果
        y: int = int((1 - self.value() / (self.maximum() - self.minimum())) * (self.height() - self.lb.height()))
        self.lb.move(x, y)
        self.lb.setText(str(self.value()))
        self.lb.adjustSize()

    def mouseReleaseEvent(self, evt):  #鼠标释放，标签消失
        super().mouseReleaseEvent(evt)
        self.lb.hide()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 创建两个控件
        sd = Slider(self)
        sd.move(200,200)
        sd.resize(30,200)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())