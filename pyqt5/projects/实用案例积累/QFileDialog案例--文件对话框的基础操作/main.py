# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.btn = QPushButton("加载图片")  # 创建加载图片按钮
        self.btn.clicked.connect(self.getfile)  # 点击按钮时发射clicked信号，连接槽函数getfile
        layout.addWidget(self.btn)

        self.le = QLabel("")  # 创建空文本框，用于显示加载的图片文件
        layout.addWidget(self.le)

        self.btn1 = QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)

        self.contents = QTextEdit()  # 创建多行文本，用于加载打开的文本文件
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("File Dialog 例子")

    def getfile(self):  # 获取格式为.jpg和.gif的文件，路径为C盘下，QFileDialog.getOpenFileName，调用文件对话框来显示图像
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.png)")
        self.le.setPixmap(QPixmap(fname))  # 在le label中加载图片

    # 在QFileDialog.getOpenFileName()函数中：
    # 第一个参数用于指定父组件，第二个参数是QFileDialog对话框的标题，第三个参数是对话框显示时默认打开的目录，“.”代表程序运行的目录
    # “/”代表当前盘下的根目录。第四个参数是对话框中文拓展名过滤器（Filter），比如使用“Image files(*.jpg *.gif)”表示只能显示.jpg和.gif文件
    def getfiles(self):  # 允许打开文本文件，路径为C盘下，使用QFileDialog对象的exec_()方法来选择文件，并把选择的文件显示
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)  # 在多行文本框上显示打开的文本内容


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())