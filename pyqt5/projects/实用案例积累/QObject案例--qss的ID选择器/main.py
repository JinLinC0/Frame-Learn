from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()
        
    def setup_ui(self):
        #读取QObject.qss文件中整个的字符串并设置qss
        with open("QObject.qss","r") as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.move(50,50)
        label.setObjectName("notice")
        label.setText("这是一个label")

        label1 = QLabel(self)
        label1.move(150, 150)
        label1.setObjectName("notice")
        label1.setText("这是一个label1")

        label2 = QLabel(self)
        label2.move(200, 200)
        label2.setText("这是一个label2")
        
if __name__ == '__main__':  
	import sys
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())