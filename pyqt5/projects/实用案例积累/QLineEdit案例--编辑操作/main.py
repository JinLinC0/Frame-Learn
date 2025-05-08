# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
le = QLineEdit(window)
le.resize(200,200)
le.move(0,150)
#退格按钮
btn_backspace = QPushButton(window)
btn_backspace.move(250,50)
btn_backspace.setText("退格")
def backspace_cao():
    le.setFocus()
    le.backspace()
btn_backspace.clicked.connect(backspace_cao)

#删除按钮
btn_del = QPushButton(window)
btn_del.move(250,100)
btn_del.setText("删除")
def del_cao():
    le.setFocus()
    le.del_()
btn_del.clicked.connect(del_cao)

#复制粘贴按钮
btn_copy_cut = QPushButton(window)
btn_copy_cut.move(250,150)
btn_copy_cut.setText("复制粘贴")
def copy_cut_cao():
    le.cursorBackward(True,3)  #向左选择三个字符
    le.copy()  #将文本的内容复制到系统的剪贴板中
    le.setCursorPosition(0)  #将光标放在第一个位置
    le.paste()
    le.setFocus()
btn_copy_cut.clicked.connect(copy_cut_cao)

#文本框的拖放
le2 = QLineEdit(window)
le2.resize(50,50)
le2.move(300,300)
le.setDragEnabled(True)  #可以将le中的文本内容选中，拖拽到le2中

window.show()
sys.exit(app.exec_())