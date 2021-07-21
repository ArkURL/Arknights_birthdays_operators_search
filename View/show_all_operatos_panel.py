# -*- coding: utf-8 -*-
# @Time : 2021/7/21 11:57
# @Author : ui_none
import sys
import json

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
# from show_all_operators import show_all_operators

class ShowALLOperatorsListPanel(QDialog):
    def __init__(self):
        super(ShowALLOperatorsListPanel, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('显示所有干员名')

        layout = QVBoxLayout()

        self.tip_label = QLabel('所有干员：')
        self.tip_label.setFont(QFont('微软雅黑', 11))

        self.operators_label = QLabel()
        self.operators_label.setFont(QFont('微软雅黑', 10))

        operator_list = self.show_all_operators()
        operators_name = ''
        for each in operator_list:
            operators_name += each+','
        operators_name = operators_name.strip(',')
        self.operators_label.setText(operators_name)
        self.operators_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.operators_label.setTextInteractionFlags(Qt.TextSelectableByKeyboard)

        self.quit_btn = QPushButton('退出')
        self.quit_btn.setFont(QFont('微软雅黑', 10))
        self.quit_btn.clicked.connect(self.close)

        layout.addWidget(self.tip_label)
        layout.addWidget(self.operators_label)
        layout.addWidget(self.quit_btn)

        self.setLayout(layout)

    def show_all_operators(self):
        with open('..\\arknights.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
            operator_list = []
            for each in file:
                operator_list.append(each['name'])
            return operator_list


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_panel = ShowALLOperatorsListPanel()
    show_panel.show()
    sys.exit(app.exec_())