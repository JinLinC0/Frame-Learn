from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QWidget, QPushButton
import sys


class MainWidget(MainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        # 设置主窗体标签
        self.setWindowTitle("QMainWindow")
        self.resize(370, 250)
        # 关闭主窗口
        self.button1 = QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.onButtonClick)  # 将按钮的clicked信号和onButtonClick槽函数关联起来

        layout = QHBoxLayout()  # 水平布局按照从左到右的顺序进行添加按钮部件。
        layout.addWidget(self.button1)  # 添加一个按钮组件

        main_frame = QWidget()  # 新建一个QWidget窗口
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):
        sender = self.sender()  # sender是发送信号的对象
        print(sender.text() + ' 被按下了 ')  # 通过按钮的text()函数获得按钮的显示名称
        qApp = QApplication.instance()  # 槽函数获得发送信号的对象
        qApp.quit()  # 调用quit()函数来关闭窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())