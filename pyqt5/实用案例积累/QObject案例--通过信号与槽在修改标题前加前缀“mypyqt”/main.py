from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()

def title_prefix(title):
    #取消信号与槽的连接，防止进入死循环,执行完后重新连上超函数，后续改名直接加前缀
    #window.windowTitleChanged.disconnect()
    #window.setWindowTitle("mypyqt-" + title)
    #window.windowTitleChanged.connect(title_prefix)

    #可以采用临时终值信号与槽的连接
    window.blockSignals(True)
    window.setWindowTitle("mypyqt-" + title)
    window.blockSignals(False)

window.windowTitleChanged.connect(title_prefix)
window.setWindowTitle("pyqt学习")
window.setWindowTitle("pyqt学习1")
window.show()
sys.exit(app.exec_())