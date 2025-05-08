from PyQt5.Qt import *
import sys

class MyLabel(QLabel):
    def __init__(self, *args ,**kwargs):  #*args ,**kwargs通用适配所有传递过来的参数，传递给父类的方法，让父类来处理
        super().__init__(*args ,**kwargs)
        self.setText("10")
        self.move(100,100)
        self.setStyleSheet("font-size:22px")  #改变字体大小


    def setsec(self, sec):
        self.setText(str(sec))

    def startMyTimer(self, ms):
        self.timer_id = self.startTimer(ms)  #开启定时器，设置间隔，并创建一个timer_id

    def timerEvent(self, *args ,**kwargs):
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))

        if current_sec == 0:
            self.killTimer(self.timer_id)  #关闭定时器

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QObject定时器的使用")
window.resize(500, 500)
label = MyLabel(window)
#设置函数调用，防止过度封装
label.setsec(5)
label.startMyTimer(500)
window.show()
sys.exit(app.exec_())