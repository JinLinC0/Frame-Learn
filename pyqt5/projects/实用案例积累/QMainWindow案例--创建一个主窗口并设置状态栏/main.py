import sys
from PyQt5.QtWidgets import QMainWindow , QApplication

class MainWidget(QMainWindow):     #自定义的窗口类MainWindow中，继承了主窗口QMainWindow类所有的属性和方法
	def __init__(self,parent=None):
		super(MainWidget,self).__init__(parent)    #使用父类QMainWindow的构造函数super()初始化窗口
        # 设置主窗体标签
		self.setWindowTitle("QMainWindow")         #设置窗口标题
		self.resize(400, 200)                     #设置QWidget窗口大小，（长，宽）
        #显示状态栏
		self.status = self.statusBar()             #由atatusBar()产生状态栏
		self.status.showMessage("这是状态栏提示",5000)    #由showMessage()显示信息，5000ms后提示消失

if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = MainWidget()
	main.show()
	sys.exit(app.exec_())