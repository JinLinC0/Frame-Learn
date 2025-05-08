from PyQt5.Qt import *
import sys

class App(QApplication):
    def notify(self, recevier, evt):
        if recevier.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(recevier, evt)
        return super().notify(recevier, evt)

class Btn(QPushButton):
    def event(self, evt):
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)
        return super().event(evt)

    def mousePressEvent(self, *args, **kwargs):
        print("按钮被按下了---")
        return super().mousePressEvent(*args, **kwargs)  #使原来的信号还是可以和槽进行连接的


app = App(sys.argv)
window = QWidget()

btn = Btn(window)
btn.setText("按钮")
btn.move(100,100)

def cao():
    print("按钮被按下了")

btn.pressed.connect(cao)

window.show()
sys.exit(app.exec_())