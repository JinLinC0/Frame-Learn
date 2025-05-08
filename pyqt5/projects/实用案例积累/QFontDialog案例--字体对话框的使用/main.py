# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FontDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FontDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.fontButton = QPushButton("choose font")  #初始界面设置一个按钮   实例化fontButton对象
        self.fontButton.clicked.connect(self.getFont)  #按钮按下时发射clicked信号，连接槽函数getFont
        layout.addWidget(self.fontButton)
        self.fontLineEdit = QLabel("Hello,测试字体例子")  #创建例子标签，用于字体变化的显示，实例化fontLineEdit对象
        layout.addWidget(self.fontLineEdit)
        self.setLayout(layout)
        self.setWindowTitle("Font Dialog 例子")
        #设置默认字体
        self.firstfont = QFont()
        self.firstfont.setFamily("宋体")
        self.firstfont.setPointSize(36)

    def getFont(self): #自定义槽函数，选择字体，并将字体效果设置到fontLineEdit中
        #font, ok = QFontDialog.getFont(self)  #使用最简单的getFont方法
        font, ok = QFontDialog.getFont(self.firstfont, self, "字体格式选择")
        if ok:    #如果用户选择接受操作
            self.fontLineEdit.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = FontDialogDemo()
    demo.show()
    sys.exit(app.exec_())