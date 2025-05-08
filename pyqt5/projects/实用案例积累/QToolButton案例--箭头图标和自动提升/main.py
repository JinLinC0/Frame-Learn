# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
tb = QToolButton(window)
tb.setArrowType(Qt.LeftArrow)
tb.setAutoRaise(True)
window.show()
sys.exit(app.exec_())