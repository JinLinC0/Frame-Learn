# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        kse = QKeySequenceEdit(self)
        #键位默认值的设置
        #ks = QKeySequence("Ctrl+C")
        #ks = QKeySequence(QKeySequence.Copy)
        ks = QKeySequence(Qt.CTRL + Qt.Key_C)
        kse.setKeySequence(ks)
        kse.clear() #清空默认值
        btn = QPushButton(self)
        btn.move(100,100)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda :print(kse.keySequence().toString(),kse.keySequence().count()))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())