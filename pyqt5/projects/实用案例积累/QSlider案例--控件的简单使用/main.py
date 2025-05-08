# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SliderDemo(QWidget):
    def __init__(self, parent=None):
        super(SliderDemo, self).__init__(parent)
        self.setWindowTitle("QSlider 例子")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.l1 = QLabel("Hello PyQt5")  # 创建文本
        self.l1.setAlignment(Qt.AlignCenter)  # 文本居中
        layout.addWidget(self.l1)

        self.sl = QSlider(Qt.Horizontal)  # 水平方向创建滑动条
        self.sl.setMinimum(10)  # 设置最小值
        self.sl.setMaximum(50)  # 设置最大值
        self.sl.setSingleStep(3)  # 设置步长
        self.sl.setValue(20)  # 设置当前值（初始值）
        self.sl.setTickPosition(QSlider.TicksBelow)  # 刻度位置，刻度在下方
        self.sl.setTickInterval(5)  # 设置刻度间隔
        layout.addWidget(self.sl)

        self.sl.valueChanged.connect(self.valuechange)  # 连接信号槽，滑块值改变时发射信号
        self.setLayout(layout)

    def valuechange(self):
        print('current slider value=%s' % self.sl.value())
        size = self.sl.value()  # 读取滑块条的值
        self.l1.setFont(QFont("Arial", size))  # 滑块条来改变字体大小


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SliderDemo()
    demo.show()
    sys.exit(app.exec_())