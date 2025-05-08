from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget   #QDesktopWidget是描述显示屏幕的类
import sys

class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        # 设置主窗体标签
        self.setWindowTitle("QMainWindow")
        self.resize(370, 250)
        #主窗口居中显示
        self.center()

    #def center(self):
    #    screen = QDesktopWidget().screenGeometry()    #获取屏幕的大小：（screen.width()*screen.height()）
    #    size = self.geometry()              #获取QWidget窗口的大小：（size.width()*size.height()）
    #    self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)  #将窗口移到屏幕中间

    #要在python3.11环境中运行，则def center(self):修改为以下代码：
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        x: int = int((screen.width() - size.width()) / 2)
        y: int = int((screen.height() - size.height()) / 2)
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())