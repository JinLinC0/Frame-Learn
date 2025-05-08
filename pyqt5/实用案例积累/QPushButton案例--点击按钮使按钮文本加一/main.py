# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
btn = QPushButton(window)
btn.setText("1")
def plus_one():
    num = int(btn.text()) + 1
    btn.setText(str(num))

btn.pressed.connect(plus_one)

window.show()
sys.exit(app.exec_())