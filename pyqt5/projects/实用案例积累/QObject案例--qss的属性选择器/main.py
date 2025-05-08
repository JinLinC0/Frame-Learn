from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()
        
    def setup_ui(self):
        # 读取QObject.qss文件中整个的字符串并设置qss
        with open("QObject.qss", "r") as f:
            qApp.setStyleSheet(f.read())

        label1 = QLabel(self)
        label1.move(50, 50)
        label1.setObjectName("notice")
        label1.setText("这是一个label1")

        label2 = QLabel(self)
        label2.move(100,100)
        label2.setObjectName("notice")
        label2.setProperty("notice_level","normal")
        label2.setText("这是一个正常标签label2")

        label3 = QLabel(self)
        label3.move(150, 150)
        label3.setObjectName("notice")
        label3.setProperty("notice_level", "warning")
        label3.setText("这是一个警告标签label3")

        label4 = QLabel(self)
        label4.move(200, 200)
        label4.setObjectName("notice")
        label4.setProperty("notice_level", "error")
        label4.setText("这是一个错误标签label4")


if __name__ == '__main__':  
	import sys
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())