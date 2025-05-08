# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  #开启鼠标跟踪，可以不开启
        self.move_flag = False #一开始使标记为False
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()
        
    def setup_ui(self):
        pass

    def mousePressEvent(self, evt):
        if evt.button() == Qt.LeftButton:  #当鼠标左键按下时执行
            self.move_flag = True  #设置一个标记，当鼠标按下事件发生时，设值为True，防止鼠标跟踪引起程序错误
            #确定两个全局点：鼠标第一次按下的点和窗口当前所在的左上角原始点
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, evt):
        if self.move_flag:  #当标记为True是执行以下的代码
            #最新的x和y：重新读取evt.globalX()和evt.globalY()
            #计算移动的x和y，计算移动向量
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            #计算窗口目标位置的点坐标：原始位置坐标加上移动向量
            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y
            self.move(dest_x,dest_y)

    def mouseReleaseEvent(self, QMouseEvent):
        self.move_flag = False  #当鼠标释放时，将标记设置为False，移动事件失效
        
if __name__ == '__main__':  
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())