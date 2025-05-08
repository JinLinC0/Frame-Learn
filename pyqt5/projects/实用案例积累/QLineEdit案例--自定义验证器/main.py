# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

#写一个自己的子类化验证器，判断年龄是否在18-100之间
class AgeVadidator(QValidator):
    def validate(self, input_str, pos_int):
        #input_str表示输入文本框中字符串的内容；pos_int表示光标的位置
        print(input_str, pos_int)
        #先判断字符串是否都是由数字组成
        try:
            if 18 <= int(input_str) <= 100:
                return (QValidator.Acceptable, input_str, pos_int)
                # QValidator.Acceptable表示验证通过
            elif 1 <= int(input_str) <= 9:
                return (QValidator.Intermediate, input_str, pos_int)
                # QValidator.Intermediate表示中间状态，目前是被允许的，等待用户输入结束
            else:
                return (QValidator.Invalid, input_str, pos_int)
                # QValidator.Invalid表示不通过，数据将不会显示在文本框中
        except: #否则返回无效
            if len(input_str) == 0:  #使输入框可以清空
                return (QValidator.Intermediate, input_str, pos_int)
            return (QValidator.Invalid, input_str, pos_int)

    def fixup(self, p_str):
        try:
            if int(p_str) < 18:   #如果输入的数据小于18，就给文本框返回18
                return "18"
            return "100"
        except:
            return "18"

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()
        
    def setup_ui(self):
        le = QLineEdit(self)
        le.move(100,100)
        #创建验证器对象
        vadidator = AgeVadidator()
        le.setValidator(vadidator)

        le1 = QLineEdit(self)
        le1.move(100,200)

if __name__ == '__main__':  
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())