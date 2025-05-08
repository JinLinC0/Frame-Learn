# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
leA = QLineEdit(window)
leA.move(50,50)

leB = QLineEdit(window)
leB.move(50,100)

btn = QPushButton(window)
btn.setText("复制按钮")
btn.move(300,70)
btn.clicked.connect(lambda : leB.setText(leA.text()))
window.show()
sys.exit(app.exec_())