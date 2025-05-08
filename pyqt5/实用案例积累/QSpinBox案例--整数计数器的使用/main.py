# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class spindemo(QWidget):
    def __init__(self, parent=None):
        super(spindemo, self).__init__(parent)
        self.setWindowTitle("SpinBox 例子")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.l1 = QLabel("current value:")  # 创建标签，同时设置名字
        self.l1.setAlignment(Qt.AlignCenter)  # 标签居中
        layout.addWidget(self.l1)

        self.sp = QSpinBox()  # 创建计数器
        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.valuechange)  # 将计数器的valueChanged信号连接到槽函数valuechange
        self.setLayout(layout)

    def valuechange(self):  # 槽函数valuechange()把计数器的当前值设置到标签文本中
        self.l1.setText("current value:" + str(self.sp.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = spindemo()
    ex.show()
    sys.exit(app.exec_())