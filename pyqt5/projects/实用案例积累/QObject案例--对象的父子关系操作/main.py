from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        #创建对象
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()
        print("obj0", obj0)
        print("obj1", obj1)
        print("obj2", obj2)
        print("obj3", obj3)
        print("obj4", obj4)
        print("obj5", obj5)
        #设置相关的父子关系
        obj1.setParent(obj0)
        obj2.setParent(obj0)
        obj2.setObjectName("2")  #设置参数名称

        obj3.setParent(obj1)
        obj3.setObjectName("3")

        obj4.setParent(obj2)
        obj5.setParent(obj2)
        #通过print输出父子关系验证
        print(obj4.parent())  #查看obj4的父对象

        print(obj0.children())  #查看obj0所有的子对象

        print(obj0.findChild(QObject))  #通过条件查找子对象，找到一个QObject的子对象，找到一个就停止
        print(obj0.findChild(QObject, "2"))  #通过参数2进行查找名称为”2“的子对象
        print(obj0.findChild(QObject, "3"))  #参数3中的递归查找(默认)会继续跟进跨级查找子对象
        print(obj0.findChild(QObject, "3", Qt.FindDirectChildrenOnly))  #改变查找方式后，Qt.FindDirectChildrenOnly 只查找直接子对象，那么就找不到obj3

        print(obj0.findChildren(QObject))  #查找obj0所有的直接和间接的子对象，递归查找(默认)会继续跟进跨级查找子对象

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())