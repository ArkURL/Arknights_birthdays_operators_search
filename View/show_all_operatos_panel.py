# -*- coding: utf-8 -*-
# @Time : 2021/7/21 11:57
# @Author : ui_none
import sys
import json

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from project_settings import *

NUMS_PER_ROW = 8


class ShowALLOperatorsListPanel(QDialog):
    def __init__(self):
        super(ShowALLOperatorsListPanel, self).__init__()
        self.initUi()

    def initUi(self):
        if not arkjson.is_file():
            return

        self.setWindowTitle('显示所有干员名')

        layout = QVBoxLayout()

        self.tip_label = QLabel('所有干员：')
        self.tip_label.setFont(QFont('微软雅黑', 11))

        layout.addWidget(self.tip_label)

        operator_list = self.show_all_operators()

        self.operators_label_list = [QLabel() for each in range(0, len(operator_list), NUMS_PER_ROW)]

        operators_name = ''
        count = 0
        for each in operator_list:
            operators_name += each+','
            count += 1
            if count % NUMS_PER_ROW == 0:
                operators_name = operators_name.strip(',')
                self.operators_label = self.operators_label_list[0]
                self.operators_label.setText(operators_name)
                self.operators_label.setFont(QFont('微软雅黑', 8))
                # 设置文本可复制
                self.operators_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
                self.operators_label.setTextInteractionFlags(Qt.TextSelectableByKeyboard)
                layout.addWidget(self.operators_label)
                operators_name = ''
                self.operators_label_list.pop(0)


        self.quit_btn = QPushButton('退出')
        self.quit_btn.setFont(QFont('微软雅黑', 10))
        self.quit_btn.clicked.connect(self.close)

        layout.addWidget(self.quit_btn)

        self.setLayout(layout)

    def show_all_operators(self):
        try:
            with open(Path_to_arkjson, 'r', encoding='utf-8') as f:
                file = json.load(f)
                operator_list = []
                for each in file:
                    operator_list.append(each['name'])
                return operator_list
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_panel = ShowALLOperatorsListPanel()
    show_panel.show()
    sys.exit(app.exec_())