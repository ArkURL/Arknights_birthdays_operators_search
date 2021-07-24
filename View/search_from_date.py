# -*- coding: utf-8 -*-
# @Time : 2021/7/18 16:09
# @Author : ui_none
import sys

from bir_search import from_date_get_operators
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QApplication
from PyQt5.QtGui import QFont, QIcon


class SearchFromDate(QDialog):
    def __init__(self):
        super(SearchFromDate, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('根据日期查询同一天生日的干员')

        # designed by 3602638-halloween-party from Flaticon
        self.setWindowIcon(QIcon('spider_in_web.png'))

        layout = QVBoxLayout()

        self.message_label = QLabel('输入日期查询是否有对应干员生日')
        self.message_label.setFont(QFont('微软雅黑', 12))

        self.input_line = QLineEdit()
        self.input_line.setFont(QFont('微软雅黑', 9))

        self.confirm_btn = QPushButton('确定')
        self.confirm_btn.setFont(QFont('微软雅黑', 10))
        self.confirm_btn.clicked.connect(self.get_result)

        self.result_label = QLabel('结果会在这里显示')
        self.result_label.setFont(QFont('微软雅黑', 12))

        self.return_btn = QPushButton('返回')
        self.return_btn.setFont(QFont('微软雅黑', 10))
        self.return_btn.clicked.connect(self.close)

        layout.addWidget(self.message_label)
        layout.addWidget(self.input_line)
        layout.addWidget(self.confirm_btn)
        layout.addWidget(self.result_label)
        layout.addWidget(self.return_btn)

        self.setLayout(layout)


    def get_result(self):
        date = self.input_line.text()
        result = from_date_get_operators(date)
        if len(result) == 0:
            self.result_label.setText('看来没有和你同一天生日的干员呢...')
        else:
            result_text = ''
            for each in result:
                result_text += each + ','
            result_text = result_text.strip(',')
            self.result_label.setText(f'你和{result_text}同一天生日哦！')

        self.input_line.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    search_date = SearchFromDate()
    search_date.show()
    sys.exit(app.exec_())