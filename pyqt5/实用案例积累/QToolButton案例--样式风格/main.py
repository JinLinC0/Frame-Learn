# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
tb = QToolButton(window)
tb.setText("工具")
tb.setIcon(QIcon("123.PNG"))
tb.setToolTip("这是一个新建按钮")
#通过setToolButtonStyle()方式使图标和文本可以一起显示
tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
window.show()
sys.exit(app.exec_())