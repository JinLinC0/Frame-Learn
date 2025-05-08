# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
btn = QCommandLinkButton("标题", "描述", window)
btn.setText("开始")
btn.setDescription("这是描述")
window.show()
sys.exit(app.exec_())