# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
le = QLineEdit(window)
le.setText("jlc")

btn1 = QPushButton(window)
btn1.setText("插入")
btn1.move(50,50)
btn1.clicked.connect(lambda : le.insert("123"))

btn2 = QPushButton(window)
btn2.setText("输出")
btn2.move(50,100)
btn2.clicked.connect(lambda : print(le.text()))
window.show()
sys.exit(app.exec_())