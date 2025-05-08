# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

#封装(抽离)一个类，在类中提供一个方法给外界用于验证登录信息，最后给出结果
class AccountTool:
    ACCOUNT_ERROR = 1 #账号错误
    PWD_ERROR = 2 #密码错误
    SUCCESS = 3 #登录成功
    @staticmethod  #将下列方法标识为一个静态方法
    def check_login(account, pwd):
        #把账号和密码发送给服务器，等待服务器返回结果
        if account != "jlc":
            return AccountTool.ACCOUNT_ERROR
        if pwd != "123":
            return AccountTool.PWD_ERROR
        return AccountTool.SUCCESS

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用户登陆")
        self.resize(450,450)
        self.setMinimumSize(400,400) #限定窗口最小宽度和高度
        self.setup_ui()

    def setup_ui(self):
        self.leA = QLineEdit(self)
        self.leB = QLineEdit(self)
        self.leB.setEchoMode(QLineEdit.Password) #设置输入方式是加密的
        self.btn = QPushButton(self)
        #占位文本的提示
        self.leA.setPlaceholderText("请输入账号：")
        self.leB.setPlaceholderText("请输入密码：")

        self.leB.setClearButtonEnabled(True)#密码文本框显示清空按钮

        #添加自定义行为操作，明文和密文的切换
        self.action = QAction(self.leB) #为leB创建一个行为对象
        self.action.setIcon(QIcon("close.png"))
        self.leB.addAction(self.action, QLineEdit.TrailingPosition)
        self.action.triggered.connect(self.change_cao)

        #账号自动补全器
        completer = QCompleter(["jlc","jinlinchao","qwerrttt"],self.leA)
        self.leA.setCompleter(completer)

        self.btn.setText("登       录")
        self.btn.clicked.connect(self.login_cao)
        self.lb = QLabel(self)
        self.lb.setAlignment(Qt.AlignCenter)

    #窗口变化，控件位置保持居中
    def resizeEvent(self, evt):
        widget_w = 220  # 控件的宽度
        widget_h = 30  # 控件的高度
        margin = 30  # 控件中的统一间距

        x: int = int((self.width() - widget_w) / 2)  # 控件的x坐标
        self.leA.resize(widget_w, widget_h)
        y: int = int(self.height() / 2)
        self.leA.move(x, y)

        self.leB.resize(widget_w, widget_h)
        self.leB.move(x, self.leA.y() + widget_h + margin)

        self.btn.resize(widget_w, widget_h+10)
        self.btn.move(x, self.leB.y() + widget_h + margin)

        self.lb.resize(widget_w, widget_h)
        self.lb.move(x, self.btn.y() + widget_h + margin)

    #槽函数
    def login_cao(self):
        #获取账号和密码信息
        account = self.leA.text()
        pwd = self.leB.text()
        # 通过AccountTool类进行判断登录信息
        state = AccountTool.check_login(account, pwd)
        if state == AccountTool.ACCOUNT_ERROR:
            print("账号错误！")
            self.lb.setText("账号错误！")
            self.leA.clear()
            self.leB.clear()
            self.leA.setFocus()
        if state == AccountTool.PWD_ERROR:
            print("密码错误！")
            self.lb.setText("密码错误！")
            self.leB.clear()
            self.leB.setFocus()
        if state == AccountTool.SUCCESS:
            print("登录成功！")
            self.lb.setText("登录成功！")

        '''
        if account == "jlc":
            if pwd == "123":
                print("登录成功！")
            else:
                print("密码错误！")
                self.leB.clear()
                self.leB.setFocus()
        else:
            print("账号错误！")
            self.leA.clear()
            self.leB.clear()
            self.leA.setFocus()
        '''

        '''优化写法，对于逻辑复杂的情况非常简单，少了if的嵌套
        if account != "jlc":
            print("账号错误！")
            self.leA.clear()
            self.leB.clear()
            self.leA.setFocus()
            return None
        if pwd != "123":
            print("密码错误！")
            self.leB.clear()
            self.leB.setFocus()
            return None
        print("登录成功！")
        '''

    #明文密文切换的槽函数
    def change_cao(self):
        if self.leB.echoMode() == QLineEdit.Normal:
            self.leB.setEchoMode(QLineEdit.Password)
            self.action.setIcon(QIcon("close.png"))
        else:
            self.leB.setEchoMode(QLineEdit.Normal)
            self.action.setIcon(QIcon("open.png"))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())






