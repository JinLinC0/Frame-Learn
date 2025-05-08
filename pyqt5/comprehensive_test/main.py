# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TabDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)
        # 设置三个选项卡，并添加进去
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.setWindowTitle("Tab 例子")
        self.resize(600, 550)
    def tab1UI(self):
        mianlayout = QVBoxLayout()

        label_box = QGroupBox("文本框控件")
        l_layout = QHBoxLayout()
        label1 = QLabel(self)
        label1.setText("这是一个文本标签。")
        label1.setAutoFillBackground(True)  # 表示的是自动填充背景,如果想使用后面的代码,这里必须要设置为True
        palette = QPalette()  # 实例化一个调色板对象，背景需要一个颜色器来生成
        palette.setColor(QPalette.Window, Qt.blue)  # 设置背景颜色，实例为蓝色
        label1.setPalette(palette)  # 将颜色器上的颜色整合到label上去
        label1.setAlignment(Qt.AlignCenter)  # 设置文本标签居中显示
        label2 = QLabel(self)
        label2.setAlignment(Qt.AlignCenter)  # 设置图片标签居中显示
        label2.setToolTip('这是一个图片标签')
        label2.setPixmap(QPixmap("./images/clock.png"))
        l_layout.addWidget(label1)
        l_layout.addWidget(label2)
        label_box.setLayout(l_layout)

        button_box = QGroupBox("按钮控件")
        b_layout = QHBoxLayout()
        btn1 = QPushButton("简单按钮")
        btn2 = QRadioButton("互斥按钮")
        btn3 = QCheckBox("三态按钮")
        btn3.setTristate(True)
        btn4 = QComboBox()
        btn4.addItem("C")
        btn4.addItems(["C++", "Java", "C#", "Python"])
        b_layout.addWidget(btn1)
        b_layout.addWidget(btn2)
        b_layout.addWidget(btn3)
        b_layout.addWidget(btn4)
        button_box.setLayout(b_layout)

        edit_box = QGroupBox("文本框控件")
        e_layout = QHBoxLayout()
        pNormalLineEdit = QLineEdit()
        pNormalLineEdit.setPlaceholderText("单行文本框")
        textEdit = QTextEdit()
        textEdit.setPlaceholderText("多行文本框")
        e_layout.addWidget(pNormalLineEdit)
        e_layout.addWidget(textEdit)
        edit_box.setLayout(e_layout)

        count_box = QGroupBox("计数器控件")
        c_layout = QHBoxLayout()
        sp = QSpinBox()
        sp.setValue(3)
        sl = QSlider(Qt.Horizontal)
        sl.setMinimum(10)  # 设置最小值
        sl.setMaximum(50)  # 设置最大值
        sl.setSingleStep(3)  # 设置步长
        sl.setValue(20)  # 设置当前值（初始值）
        sl.setTickPosition(QSlider.TicksBelow)  # 刻度位置，刻度在下方
        sl.setTickInterval(5)  # 设置刻度间隔
        c_layout.addWidget(sp)
        c_layout.addStretch()
        c_layout.addWidget(sl)
        count_box.setLayout(c_layout)

        progress_bar_box = QGroupBox("进度条控件")
        p_layout = QHBoxLayout()
        self.pbar = QProgressBar(self)  # 创建一个进度条
        self.pbar.setGeometry(30, 40, 200, 25)  # 设置位置和大小
        # 创建按钮，连接信号槽函数doAction()
        self.btn = QPushButton('Start', self)
        self.btn.setProperty('name', 'mybtn1')
        self.btn.clicked.connect(self.doAction)
        # 创建一个定时器
        self.timer = QBasicTimer()
        self.step = 0
        p_layout.addWidget(self.pbar)
        p_layout.addWidget(self.btn)
        p_layout.addStretch()
        progress_bar_box.setLayout(p_layout)

        # 把相关内容添加到总布局中
        mianlayout.addWidget(label_box)
        mianlayout.addWidget(button_box)
        mianlayout.addWidget(edit_box)
        mianlayout.addWidget(count_box)
        mianlayout.addWidget(progress_bar_box)

        # 设置窗口显示的内容是最外层布局方式
        self.setLayout(mianlayout)
        self.setTabText(0, "基础组件")
        self.tab1.setLayout(mianlayout)

    def tab2UI(self):
        mianlayout = QVBoxLayout()
        grid_control_box = QGroupBox("表格控件")
        conLayout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        conLayout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(['序号', '姓名', '性别', '体重(kg)'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior( QAbstractItemView.SelectRows)
        grid_control_box.setLayout(conLayout)

        button_box = QGroupBox("表格操作按钮")
        b_layout = QVBoxLayout()
        btn1 = QPushButton('清空', self)
        btn2 = QPushButton('数据1', self)
        btn3 = QPushButton('数据2', self)
        btn4 = QPushButton('打印全部数据', self)
        btn1.setProperty('name', 'myBtn1')
        btn2.setProperty('name', 'myBtn1')
        btn3.setProperty('name', 'myBtn1')
        btn4.setProperty('name', 'myBtn1')
        btn1.clicked.connect(self.clearall)
        btn2.clicked.connect(self.dateone)
        btn3.clicked.connect(self.datetwo)
        btn4.clicked.connect(self.printdate)
        b_layout.addWidget(btn1)
        b_layout.addWidget(btn2)
        b_layout.addWidget(btn3)
        b_layout.addWidget(btn4)
        button_box.setLayout(b_layout)

        mianlayout.addWidget(grid_control_box)
        mianlayout.addWidget(button_box)

        self.setLayout(mianlayout)
        self.setTabText(1, "表格")
        self.tab2.setLayout(mianlayout)


    def tab3UI(self):
        mianlayout = QVBoxLayout()

        Popup_Control_box = QGroupBox("弹窗控件")
        P_layout = QHBoxLayout()
        btn8 = QPushButton('提示弹窗', self)
        btn9 = QPushButton('对话弹窗', self)
        btn8.setProperty('name', 'mybtn')
        btn9.setProperty('name', 'mybtn')
        btn8.clicked.connect(self.showdialog)
        btn9.clicked.connect(self.msg)
        P_layout.addWidget(btn8)
        P_layout.addWidget(btn9)
        P_layout.addStretch()
        Popup_Control_box.setLayout(P_layout)

        Drawer_control_box = QGroupBox("抽屉控件")
        D_layout = QHBoxLayout()
        btn10 = QPushButton('左侧抽屉', self)
        btn11 = QPushButton('右侧抽屉', self)
        btn12 = QPushButton('顶部抽屉', self)
        btn13 = QPushButton('底部抽屉', self)
        btn10.setProperty('name', 'myBtn')
        btn11.setProperty('name', 'myBtn')
        btn12.setProperty('name', 'myBtn')
        btn13.setProperty('name', 'myBtn')
        D_layout.addWidget(btn10)
        D_layout.addWidget(btn11)
        D_layout.addWidget(btn12)
        D_layout.addWidget(btn13)
        D_layout.addStretch()
        Drawer_control_box.setLayout(D_layout)

        time_box = QGroupBox("日期时间控件")
        t_layout = QHBoxLayout()
        cal = QCalendarWidget(self)
        cal.setMinimumDate(QDate(1980, 1, 1))
        cal.setMaximumDate(QDate(3000, 1, 1))
        cal.setGridVisible(True)
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime(), self)
        #设置日期时间格式
        dateTimeEdit2.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        t_layout.addWidget(cal)
        t_layout.addWidget(dateTimeEdit2)
        time_box.setLayout(t_layout)

        mianlayout.addWidget(Popup_Control_box)
        mianlayout.addWidget(Drawer_control_box)
        mianlayout.addWidget(time_box)

        self.setLayout(mianlayout)
        self.setTabText(2, "其他组件")
        self.tab3.setLayout(mianlayout)

    def timerEvent(self, e):  # 重新实现timerEvent事件
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):  #start按钮的槽函数
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

    def clearall(self):
        self.tableWidget.clear()

    def dateone(self):
        self.tableWidget.setHorizontalHeaderLabels(['序号', '姓名', '性别', '体重(kg)'])
        newItem = QTableWidgetItem("1")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("张三")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("男")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem("180")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 3, newItem)

        newItem = QTableWidgetItem("2")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem("李四")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem("女")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem("170")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 3, newItem)

    def datetwo(self):
        self.tableWidget.setHorizontalHeaderLabels(['序号', '姓名', '性别', '体重(kg)'])
        newItem = QTableWidgetItem("1")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("小明")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("男")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem("185")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 3, newItem)

        newItem = QTableWidgetItem("2")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem("小红")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem("女")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem("160")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 3, newItem)

        newItem = QTableWidgetItem("3")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(2, 0, newItem)

        newItem = QTableWidgetItem("小绿")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(2, 1, newItem)

        newItem = QTableWidgetItem("男")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(2, 2, newItem)

        newItem = QTableWidgetItem("170")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(2, 3, newItem)

    def printdate(self):
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                print('' if self.tableWidget.item(i, j) is None else self.tableWidget.item(i, j).text(), end=' ')
            print()

    def showdialog(self):  #槽函数showdialog
        dialog = QDialog()
        label = QLabel("这是一个提示弹窗！", dialog)
        label.move(50, 50)
        dialog.setWindowTitle("提示")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def msg(self):
        #使用infomation信息框
        reply = QMessageBox.information(self, "对话", "这是一个对话弹窗！", QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabDemo()
    qssStyle = '''     
                QPushButton[name = "mybtn1"]:hover {background-color: blue}
                QPushButton[name = "myBtn1"] {background-color: green}
                QPushButton[name = "mybtn"] {background-color: green} 		
    			QPushButton[name = "myBtn"] {background-color: red}	
    		'''
    demo.setStyleSheet(qssStyle)
    demo.show()
    sys.exit(app.exec_())