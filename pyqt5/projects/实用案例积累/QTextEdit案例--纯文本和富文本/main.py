# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle("QTextEdit 例子")
        self.resize(300, 270)

        self.textEdit = QTextEdit()  # 创建多行文本
        self.btnPress1 = QPushButton("显示文本")  # 创建显示文本按钮
        self.btnPress2 = QPushButton("显示HTML")  # 创建显示HTML按钮

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)  # 按下按钮clicked信号连接到槽函数btnPress1_Clicked
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)  # 按下按钮clicked信号连接到槽函数btnPress2_Clicked

    def btnPress1_Clicked(self):  # 槽函数，在多行文本中显示相关文本
        self.textEdit.setPlainText("Hello PyQt5!\n点击按钮")

    def btnPress2_Clicked(self):  # 槽函数，在多行文本中显示相关文本
        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\n点击按钮。</font>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())