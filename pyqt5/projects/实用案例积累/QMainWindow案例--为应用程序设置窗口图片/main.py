# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("主窗口顶层界面")  #双引号中不写东西，则默认显示python；若双引号中输入空格，则窗口标题不显示任何东西
window.resize(500,500)
icon = QIcon('./images/cartoon1.png')
window.setWindowIcon(icon)
window.show()
sys.exit(app.exec_())