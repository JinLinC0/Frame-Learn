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
        #1.添加子控件，复选框
        for i in range(0, 30):
            cb = QCheckBox(self)
            cb.setText("{}".format(i))
            cb.move(i % 4 * 50, i // 4 *60)
            #2.创建一个橡皮筋控件
            self.rb = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, evt):
        #3.设置尺寸大小，包括鼠标点击的位置点
        self.origin_pos = evt.pos()  #记录原始的点
        self.rb.setGeometry(QRect(self.origin_pos, QSize()))  #给一个局部的点坐标和一个空尺寸
        #4.展示橡皮筋控件
        self.rb.show()

    def mouseMoveEvent(self, evt):
        #5.调整橡皮筋选中控件的位置以及尺寸
        self.rb.setGeometry(QRect(self.origin_pos, evt.pos()).normalized())  #前者表示初始的鼠标点位置，后者表示最后的鼠标点位置.normalized()表示可以使橡皮筋反向拖（向左上方拖）

    def mouseReleaseEvent(self, evt):
        #6.获取橡皮筋控件的尺寸范围
        rect = self.rb.geometry()
        #7.遍历所有的子控件，查看哪些子控件在区域范围内，改变其选中状态
        for child in self.children():
            if rect.contains(child.geometry()) and child.inherits("QCheckBox"):  #橡皮筋控件的区域也在范围内，需排除橡皮筋控件，需判定选中的控件是否继承自QCheckBox
                child.toggle()
        self.rb.hide()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())