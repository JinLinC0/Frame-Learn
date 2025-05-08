# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyqt5学习")
window.resize(500,500)
tb = QToolButton(window)
menu = QMenu(tb)
sub_menu = QMenu(menu)
sub_menu.setTitle("子菜单")
action = QAction("行为", menu)
action.setData([1,2,3])
action1 = QAction("行为1", menu)
action1.setData({"name": "jlc"})
menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action)
menu.addAction(action1)
tb.setMenu(menu)
#设置菜单的弹出方式
tb.setPopupMode(QToolButton.InstantPopup)

#行为信号传递
def do_action(action):
    print("点击了行为", action.data())
tb.triggered.connect(do_action)

window.show()
sys.exit(app.exec_())