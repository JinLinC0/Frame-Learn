# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys
import math

app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
class Btn(QPushButton):
    def hitButton(self, point):
        #使按钮左半部分点击无效，右半部分点击有效
        #if point.x() > self.width() / 2: #如果鼠标点击在按钮的右半部分
        #    return True #设置这个按钮能响应
        #else:
        #    return False  # 设置这个按钮不能响应

        #使按钮点击矩形的内切圆内部有效，思想：通过给定点的坐标，计算与圆心的距离，距离小于半径，是在有效区域内部
        yuanxin_x = self.width() / 2
        yuanxin_y = self.height() / 2
        hit_x = point.x()
        hit_y = point.y()
        distance = math.sqrt((hit_x - yuanxin_x)**2 + (hit_y - yuanxin_y)**2)
        if distance < self.width() / 2:
            return True
        else:
            return False

    def paintEvent(self, evt): #绘制内切圆
        super().paintEvent(evt) #调用父类相同的方法，使其他的父类方法可以使用，同时也可以使用以下自定义的绘制方法
        painter = QPainter(self) #创建一个画家，传递一个画布，本例中画布是整个按钮，就是self
        painter.setPen(QPen(QColor(100,150,200),3)) #给画家一根笔，设置笔的参数100,150,200表示颜色参数；6表示笔的粗细
        painter.drawEllipse(self.rect()) #绘制传递图形的一个内切圆


btn = Btn(window)
btn.resize(100,100)
btn.move(200,200)
btn.setText("点击")
btn.pressed.connect(lambda : print("按钮被点击了"))

window.show()
sys.exit(app.exec_())