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
        # 添加三个子控件：标签，文本框，按钮
        label = QLabel(self)
        label.setText("标签")
        label.move(100,50)
        label.hide()  #默认情况下标签隐藏

        le = QLineEdit(self)
        le.move(100,100)

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100,150)
        btn.setEnabled(False)  #默认情况下按钮不可用

        def text_cao(text):
            if len(text) > 0: #判断文本框中是否有值
                btn.setEnabled(True)
            else:
                btn.setEnabled(False)
            #btn.setEnabled(len(text) > 0)  优化代码代替if判断

        le.textChanged.connect(text_cao)

        def check():
            #获取文本框内容
            content = le.text()
            #判断是否为字符串Sz，是的话显示之前的隐藏标签，展示文本
            if content == "Sz":
                label.setText("登录成功")
            else:
                label.setText("登录失败")
            label.show()
            label.adjustSize()  # 设置标签尺寸自适应

        btn.pressed.connect(check)



if __name__ == '__main__':  
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())