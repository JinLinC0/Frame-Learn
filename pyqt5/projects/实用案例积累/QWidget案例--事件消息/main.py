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
        pass

    def showEvent(self, QShowEvent):  #对窗口展示进行监听
        print("窗口被展示出来")

    def closeEvent(self, QCloseEvent): #对窗口关闭进行监听
        print("窗口被关闭了")

    def moveEvent(self, QMoveEvent): #对窗口左上角的坐标移动进行监听
        print("窗口被移动了")

    def resizeEvent(self, QResizeEvent): #对窗口的尺寸改变进行监听
        print("窗口改变了尺寸大小")

    def enterEvent(self, QEvent): #对鼠标进入窗口进行监听
        print("鼠标进来了")
        self.setStyleSheet("background-color: green;")

    def leaveEvent(self, QEvent): #对鼠标离开窗口进行监听
        print("鼠标离开了")
        self.setStyleSheet("background-color: yellow;")

    def mousePressEvent(self, QMouseEvent): #对鼠标按下进行监听
        print("鼠标被按下")

    def mouseReleaseEvent(self, QMouseEvent): #对鼠标释放进行监听
        print("鼠标被释放")

    def mouseDoubleClickEvent(self, QMouseEvent): #对鼠标双击按下进行监听
        print("鼠标双击")

    def mouseMoveEvent(self, QMouseEvent): #对鼠标移动进行监听
        print("鼠标移动了")

    def keyPressEvent(self, QKeyEvent): #对键盘按下进行监听
        print("键盘上某一个按键被按下了")

    def keyReleaseEvent(self, QKeyEvent): #对键盘释放进行监听
        print("键盘上某一个按键被释放了")

if __name__ == '__main__':  
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())