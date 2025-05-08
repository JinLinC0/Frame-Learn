# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())