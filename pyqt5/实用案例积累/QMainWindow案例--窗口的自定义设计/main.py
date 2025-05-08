# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置为无边框，无标题栏
        self.setWindowOpacity(0.5)  # 设置为半透明
        self.setWindowTitle("自定义设计顶层窗口")
        self.resize(500, 500)

        #公共数据，修改参数直接在这里修改
        self.top_margin = 10  # 按钮距离顶部的距离
        #设置每个操作控件按钮的宽度和高度
        self.btn_w = 80
        self.btn_h = 40

        self.setup_ui()

    def setup_ui(self): #将所有创建子控件的代码放在这里
        # 添加三个子控件按钮，在窗口的右上角
        close_btn = QPushButton(self)
        self.close_btn = close_btn #局部变量变成全局变量，跨方法调用
        close_btn.setText("关闭")
        close_btn.resize(self.btn_w, self.btn_h)

        max_btn = QPushButton(self)
        self.max_btn = max_btn
        max_btn.setText("最大化")
        max_btn.resize(self.btn_w, self.btn_h)

        min_btn = QPushButton(self)
        min_btn.setText("最小化")
        self.min_btn = min_btn
        min_btn.resize(self.btn_w, self.btn_h)

        # 通过信号与槽进行相关功能的实现
        close_btn.pressed.connect(lambda: self.close())

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText("最大化")
            else:
                self.showMaximized()
                max_btn.setText("恢复")

        max_btn.pressed.connect(lambda: max_normal())
        min_btn.pressed.connect(lambda: self.showMinimized())

    def resizeEvent(self, QResizeEvent): #窗口大小改变时监听，使右上角三个按键及时改变位置
        window_w = self.width()
        close_btn_x = window_w - self.btn_w
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        min_btn_x = max_btn_x - self.btn_w
        min_btn_y = self.top_margin
        self.min_btn.move(min_btn_x, min_btn_y)

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
        self.move_flag = False  #当鼠标释放时，将标记设

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())