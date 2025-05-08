# -*- coding: UTF-8 -*-
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt学习")
        self.resize(500,500)
        self.city_dic = {
            "北京": {
                "东城": "001",
                "西城": "002",
                "朝阳": "003",
                "丰台": "004"
            },
            "上海": {
                "黄埔": "005",
                "徐汇": "006",
                "长宁": "007",
                "静安": "008",
                "松江": "009"
            },
            "广东": {
                "广州": "010",
                "深圳": "011",
                "湛江": "012",
                "佛山": "013"
            }
        }
        self.setup_ui()

    def setup_ui(self):
        # 1.创建两个下拉列表控件
        pro = QComboBox(self)
        city = QComboBox(self)
        self.pro = pro
        self.city = city
        pro.move(100,100)
        city.move(200,100)

        # 3.监听省下拉列表里面的当前值发生改变的信号
        pro.currentIndexChanged[str].connect(self.pro_changed)

        # 5.监听城市下拉列表里面的当前值发生改变的信号
        city.currentIndexChanged[int].connect(self.city_changed)

        # 2.展示数据到第一个下拉选择控件中
        pro.addItems(self.city_dic.keys())

    def pro_changed(self, pro_name):
        # 4.根据省的名称，到字典里面获取对应的城市字典
        citys = self.city_dic[pro_name]
        #先清空条目在追加，clear()不发射，先中断信号，在打开信号
        self.city.blockSignals(True)
        self.city.clear()
        self.city.blockSignals(False)
        for key, val in citys.items():
            self.city.addItem(key, val)

    def city_changed(self, item_idx):
        print(self.city.itemData(item_idx))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())