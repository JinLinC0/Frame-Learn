from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()

label1 = QLabel()
label1.setText("label1")
label1.move(50,50)
label1.setParent(window)

label2 = QLabel()
label2.setText("label2")
label2.move(100,100)
label2.setParent(window)

btn = QPushButton(window)
btn.move(150,150)
btn.setText("btn")

#遍历查找，从父对象中查找为QLabel的全部子类，改变其背景颜色
for sub_widget in window.findChildren(QLabel):
    sub_widget.setStyleSheet("background-color:cyan;")

window.show()
sys.exit(app.exec_())