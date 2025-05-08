# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
window.setWindowTitle("鼠标操作")
label = QLabel(window)
label.setText("鼠标改变")
label.resize(100,100)
label.setStyleSheet("background-color:cyan;")
label.setCursor(Qt.ForbiddenCursor)  #通过枚举进行鼠标形状的改变

label1 = QLabel(window)
label1.setText("鼠标改变")
label1.move(300,300)
label1.resize(100,100)
label1.setStyleSheet("background-color:cyan;")
#自定义鼠标形状
pixmap = QPixmap("./images/cartoon1.png").scaled(15,15)  #获取图片路径，同时对图片的尺寸进行缩放
cursor = QCursor(pixmap,0,0)
#放入图片，并且确定热点位置（0,0）表示鼠标图片左上角有效，不加0,0默认是中间有效，(15,15)表示图片右下角有效
label1.setCursor(cursor)

#设置鼠标的初始位置
current_cursor = window.cursor()
current_cursor.setPos(100,100)  #其坐标是相对应屏幕位置的坐标

window.show()
sys.exit(app.exec_())