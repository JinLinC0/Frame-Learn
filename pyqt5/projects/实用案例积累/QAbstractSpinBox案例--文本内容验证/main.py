# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class MyASB(QAbstractSpinBox):
    def __init__(self, parent=None, num="0", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)  #调用方法
        self.lineEdit().setText(num) #设置默认参数，若不设置可以调用时引入

    def stepEnabled(self):
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int):
        current_num = int(self.text()) + p_int
        self.lineEdit().setText(str(current_num))

    #设置验证方法
    def validate(self, p_str, p_int):
        num = int(p_str)
        if num < 18:
            return (QValidator.Intermediate, p_str, p_int)
        elif num <= 180:
            return (QValidator.Acceptable, p_str, p_int)
        else:
            return (QValidator.Invalid, p_str, p_int)

    def fixup(self, p_str):  #失去焦点，结束编辑，当数据不规范时，会进行修复操作
        return "18"

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
        asb.setAlignment(Qt.AlignCenter)  #设置为居中对齐
        btn = QPushButton(self)  #用于切换焦点创建
        btn.setText("测试按钮")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())