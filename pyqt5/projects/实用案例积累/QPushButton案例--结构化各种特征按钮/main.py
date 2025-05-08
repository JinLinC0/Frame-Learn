# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        layout = QVBoxLayout()   #布局方式是垂直布局
        #第一个按钮btn1
        self.btn1 = QPushButton("Button1")   #创建btn1，起名为Button1
        self.btn1.setCheckable(True)   #设置按钮将保持已点击和释放状态
        self.btn1.toggle()      #设置按钮状态之间进行切换，通过toggle()函数来切换按钮状态
        self.btn1.clicked.connect(lambda: self.whichbtn(self.btn1))
        #通过lambda方式来传递额外的参数btn1，将clicked信号发送给槽函数whichbtn() ，当按钮被点击时触发信号
        self.btn1.clicked.connect(self.btnstate)    #将clicked()信号发射给槽函数btnstate()
        layout.addWidget(self.btn1)   #布局
		#第二个按钮btn2，上面显示一个图标
        self.btn2 = QPushButton('image')   #创建btn2，起名为image
        self.btn2.setIcon(QIcon(QPixmap("./images/python.jpg")))
        #使用setIcon()方法接收一个QPixmap对象的图像文件作为输入参数
        self.btn2.clicked.connect(lambda: self.whichbtn(self.btn2))  #通过lambda的方式连接槽函数
        layout.addWidget(self.btn2)
        self.setLayout(layout)
		#第三个按钮btn3，设置禁用按钮
        self.btn3 = QPushButton("Disabled")
        self.btn3.setEnabled(False)   #通过setEnabled方法进行禁用按钮
        layout.addWidget(self.btn3)
		#第四个按钮btn4，
        self.btn4 = QPushButton("&Download")  #起名，并设置快捷键，快捷键是Alt+D
        self.btn4.setDefault(True)    #通过setDefault()方法设置按钮的默认状态
        self.btn4.clicked.connect(lambda: self.whichbtn(self.btn4))   #通过快捷键来调用槽函数
        layout.addWidget(self.btn4)
        self.setWindowTitle("Button demo")

    def btnstate(self):
        if self.btn1.isChecked():     #通过isChecked()函数来获取按钮是否被点击或释放的状态
            print("button pressed")
        else:
            print("button released")

    def whichbtn(self, btn):
        print("clicked button is " + btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = Form()
    btnDemo.show()
    sys.exit(app.exec_())