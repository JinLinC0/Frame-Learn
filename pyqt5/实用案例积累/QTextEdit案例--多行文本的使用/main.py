# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        self.te = QTextEdit(self)
        self.te.move(120,120)
        #self.占位文本提示()
        #self.文本内容的设置()
        #self.光标插入文本内容()
        #self.光标插入图片内容()
        #self.光标插入文本片段()
        #self.光标插入列表QTextListFormat_Style方式()
        #self.光标插入列表QTextListFormat方式()
        #self.光标文本插入表格()
        #self.光标插入文本块()
        self.插入文本框架()

    def 占位文本提示(self):
        self.te.setPlaceholderText("请输入：")

    def 文本内容的设置(self):
        # 设置普通文本
        #self.te.setPlainText("<h1>xxx</h1>")
        # 设置富文本
        self.te.setHtml("<h1>xxx</h1>")

    def 光标插入文本内容(self):  #在光标处后面进行相关内容的插入
        tc = self.te.textCursor()   #获取文本光标对象
        tcf = QTextCharFormat()  # 首先要创建一个对象
        # 进行文本格式的设置
        tcf.setToolTip("提示文本")  # 设置鼠标停留提示文本
        tcf.setFontFamily("隶书")  # 设置字体的种类
        tcf.setFontPointSize(30)  # 设置字体的大小
        tc.insertText("金琳超", tcf)  # 将插入的文本进行格式设置

    def 光标插入图片内容(self):   #在光标处后面进行相关内容的插入
        tc = self.te.textCursor()  # 设置文本光标
        tif = QTextImageFormat()  # 首先要创建一个对象
        # 进行图片参数的设置，其中常用的三个主要的参数
        tif.setName("123.PNG")  # 设置图片名字
        tif.setWidth(100)  # 设置图片宽度
        tif.setHeight(100)  # 设置图片高度
        tc.insertImage(tif)  # 将插入的文本进行格式设置

    def 光标插入文本片段(self):
        tc = self.te.textCursor()  # 设置文本光标
        #tdf = QTextDocumentFragment.fromHtml("<h1>xxx</h1>")
        tdf = QTextDocumentFragment.fromPlainText("<h1>xxx</h1>")
        tc.insertFragment(tdf)

    def 光标插入文本块(self):
        tc = self.te.textCursor()  # 设置文本光标
        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignRight)   #设置文本段落右对齐
        tbf.setRightMargin(100)  #设置右边间距为100
        tbf.setIndent(1)  #设置3个tab的文本缩进
        tcf = QTextCharFormat()
        tcf.setFontFamily("隶书")
        tcf.setFontItalic(True)
        tcf.setFontPointSize(20)
        tc.insertBlock(tbf,tcf)   #插入文本块

    def 光标插入列表QTextListFormat_Style方式(self):
        tc = self.te.textCursor()  # 设置文本光标
        tc.insertList(QTextListFormat.ListLowerAlpha)

    def 光标插入列表QTextListFormat方式(self):
        tc = self.te.textCursor()  # 设置文本光标
        tlf = QTextListFormat()
        tlf.setIndent(3)  #3个tab键的缩进距离
        tlf.setNumberPrefix("<<")
        tlf.setNumberSuffix(">>")
        tlf.setStyle(QTextListFormat.ListDecimal)
        tc.createList(tlf)

    def 光标文本插入表格(self):
        tc = self.te.textCursor()  # 设置文本光标
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)  #设置表格右对齐
        ttf.setCellPadding(6)  #设置内边距为6
        ttf.setCellSpacing(3)  #设置外边距为3
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength,50),
                                       QTextLength(QTextLength.PercentageLength,40),
                                       QTextLength(QTextLength.PercentageLength,10)))  #设置列宽，百分比设置，之和为100%
        tc.insertTable(5, 3, ttf)

    def 插入文本框架(self):
        tc = self.te.textCursor()  # 设置文本光标
        tff = QTextFrameFormat()
        tff.setBorder(10)  #设置边框有10个像素的宽度
        tff.setBorderBrush(QColor(100,100,100))  #设置边框颜色
        tff.setRightMargin(10)  #设置右侧间距
        tc.insertFrame(tff)   #插入内部框架

        doc = self.te.document()  #设置文本框对象
        root_frame = doc.rootFrame()
        root_frame.setFrameFormat(tff)  #设置文本/根框架


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())