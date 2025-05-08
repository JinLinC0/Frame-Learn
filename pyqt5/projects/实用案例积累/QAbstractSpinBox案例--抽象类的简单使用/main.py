# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class MyASB(QAbstractSpinBox):
    def __init__(self, parent=None, num="0", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)  #调用方法
        self.lineEdit().setText(num) #设置默认参数，若不设置可以调用时引入

    def stepEnabled(self):
        # 限定0-9
        if int(self.text()) == 0:
            return QAbstractSpinBox.StepUpEnabled
        elif int(self.text()) == 9:
            return QAbstractSpinBox.StepDownEnabled
        elif int(self.text()) < 0 or int(self.text()) > 9:
            return QAbstractSpinBox.StepNone
        else:
            return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int):
        current_num = int(self.text()) + p_int * 2
        self.lineEdit().setText(str(current_num))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self,"1")
        asb.resize(100,30)
        asb.move(100,100)
        asb.setAccelerated(True)  #设置为长按调整步长加快频率
        asb.setReadOnly(True)  #设置只读
        asb.setAlignment(Qt.AlignCenter)  #设置为居中对齐
        asb.setFrame(False)  #设置无边框
        asb.setButtonSymbols(QAbstractSpinBox.PlusMinus) #设置加减号

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())