# -*- coding: utf-8 -*-
# @Time : 2021/7/18 11:20
# @Author : ui_none
import sys

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import bir_search as bs


class SearchOperatorsBirthdays(QDialog):
    def __init__(self):
        super(SearchOperatorsBirthdays, self).__init__()
        self.initUi()

    def get_birthdays(self):
        name = self.input_text.text()
        result = bs.from_operatos_get_birthdays(name)
        if result == False:
            self.message_label.setText('输入干员名称有误，请输入正确的干员名')
        else:
            self.message_label.setText(f'干员{name}的生日是{result}')
        self.input_text.setText('')


    def initUi(self):
        self.setWindowTitle('查询干员生日')

        sobd_layout = QVBoxLayout()

        self.prompt_label = QLabel('请输入您想要查询的干员的名字：')
        self.prompt_label.setFont(QFont('微软雅黑', 12))
        self.prompt_label.setAlignment(Qt.AlignCenter)

        self.input_text = QLineEdit()
        self.input_text.setFont(QFont('微软雅黑', 12))

        self.confirm_button = QPushButton(self.tr('确定'))
        self.confirm_button.setFont(QFont('微软雅黑', 10))
        self.confirm_button.clicked.connect(self.get_birthdays)

        self.message_label = QLabel(self.tr('干员的生日信息会显示在这里'))
        self.message_label.setFont(QFont('微软雅黑', 12))

        self.quit_button = QPushButton('退出')
        self.quit_button.setFont(QFont('微软雅黑', 10))
        self.quit_button.clicked.connect(self.close)

        sobd_layout.addWidget(self.prompt_label)
        sobd_layout.addWidget(self.input_text)
        sobd_layout.addWidget(self.confirm_button)
        sobd_layout.addWidget(self.message_label)
        sobd_layout.addWidget(self.quit_button)

        self.setLayout(sobd_layout)
        # self.setWindowModality(Qt.ApplicationModal)

        # self.exec()

    def show_dialog(self):
        app = QApplication(sys.argv)
        search_from_operators = SearchOperatorsBirthdays()
        search_from_operators.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    search_from_operators = SearchOperatorsBirthdays()
    search_from_operators.show()
    sys.exit(app.exec_())