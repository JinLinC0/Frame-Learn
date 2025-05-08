# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)

le = QLineEdit(window)
le.move(100,100)

btn = QPushButton(window)
btn.setText("光标左移带选中")
btn.move(100,200)
def cursor_move():
    le.cursorBackward(True, 1)
    le.setFocus()  #使文本框获取焦点，方便观察
btn.clicked.connect(cursor_move)

window.show()
sys.exit(app.exec_())