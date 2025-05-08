# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
btn = QPushButton(window)
btn.setText("菜单按钮")
menu = QMenu()  #创建一个menu对象
#子菜单（最近打开）和行为动作（新建、打开、退出）的添加，同时在打开和退出之间加一个分割线
open_recent_menu = QMenu(menu)  #创建子菜单并设置父对象menu
open_recent_menu.setTitle("最近打开")
open_recent_menu.setIcon(QIcon("123.PNG"))

#new_action = QAction()
#new_action.setText("新建")
#new_action.setIcon(QIcon("123.PNG"))
new_action = QAction(QIcon("123.PNG"),"新建",menu) #代替上述三行代码
new_action.triggered.connect(lambda :print("新建文件"))

open_action = QAction(QIcon("123.PNG"),"打开",menu)
open_action.triggered.connect(lambda :print("打开文件"))

exit_action = QAction(QIcon("123.PNG"),"退出",menu)
exit_action.triggered.connect(lambda :print("退出程序"))

file_action = QAction("python-GUI编程")

menu.addAction(new_action)
menu.addAction(open_action)
open_recent_menu.addAction(file_action)
menu.addMenu(open_recent_menu) #添加一个子菜单
menu.addSeparator()
menu.addAction(exit_action)
btn.setMenu(menu) #设置菜单

window.show()
sys.exit(app.exec_())