# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
btn = QPushButton(window)
btn.setText("按钮扁平化")
btn.setFlat(True)

btn1 = QPushButton(window)
btn1.setText("默认按钮")
btn1.setDefault(True)
btn1.move(100,100)

btn2 = QPushButton(window)
btn2.setText("自动默认按钮")
btn2.setAutoDefault(True)
btn2.move(200,200)

window.show()
sys.exit(app.exec_())