# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("信息提示案例")
window.resize(500,500)
window.statusBar() #创建状态栏
window.setWindowFlags(Qt.WindowContextHelpButtonHint) #窗口改为查看这是啥模式
#当鼠标停留在窗口控件上时，在状态栏显示一段文本
window.setStatusTip("这是一个窗口")
print(window.statusTip())

label = QLabel(window)
label.setText("11111111")
label.setStatusTip("这是一个标签")
#当鼠标停留在控件上时，停留一小会，会在旁边展示一个气泡提示
label.setToolTip("这是一个提示标签")
print(label.toolTip())
label.setToolTipDuration(5000)
print(label.toolTipDuration())
#窗口切换到“查看这是啥”模式，点击相关控件显示设置的提示信息
label.setWhatsThis("这是啥？这是标签")

window.show()
sys.exit(app.exec_())