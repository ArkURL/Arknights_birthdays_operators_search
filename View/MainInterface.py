# -*- coding: utf-8 -*-
# @Time : 2021/7/17 22:29
# @Author : ui_none
import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
# import threading
# from scrapy.utils.project import get_project_settings
# from scrapy.crawler import CrawlerProcess
from multiprocessing import Process

# 通过命令行启动时的设置
# 为避免通过命令行启动时报ModuleNotFound的错误，需要手动引入当前工作目录作为环境
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# 为避免QT弹出废弃警告，修改以下程序环境变量
from os import environ

environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"
# 结束通过命令行启动程序时的设置

from View.search_from_operators import SearchOperatorsBirthdays
from View.search_from_date import SearchFromDate
from View.show_all_operators_panel import ShowALLOperatorsListPanel

import Arknight_operators_birthdays.run as run
from project_settings import *


class MainInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.tr('明日方舟干员-生日查询器'))

        # designed by 3602638-halloween-party from Flaticon
        self.setWindowIcon(QIcon('spider_in_web.png'))

        layout = QVBoxLayout()

        self.welcome_message_label = QLabel('欢迎使用明日方舟干员-生日查询器！')
        self.welcome_message_label.setFont(QFont(Font_Style, 18))
        self.welcome_message_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.welcome_message_label)

        self.tip_label = QLabel('查询功能要在爬取信息之后才可以使用哦')
        self.tip_label.setFont(QFont('微软雅黑', 9))
        self.tip_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.tip_label)

        self.spider_button = QPushButton(self.tr('爬取信息'))
        self.spider_button.setFont(QFont('微软雅黑', 10))
        self.spider_button.clicked.connect(self.activate_spider)
        self.spider_button.setIcon(QIcon('spider.png'))

        layout.addWidget(self.spider_button)

        # 根据干员名查询干员生日
        self.search_birthday_according_to_operators_name_button = QPushButton(self.tr('查询干员生日'))
        self.search_birthday_according_to_operators_name_button.setFont(QFont('微软雅黑', 10))
        # 设置按钮不可用（对应文件不存在的情况下）
        if not arkjson.is_file():
            self.search_birthday_according_to_operators_name_button.setEnabled(False)

        layout.addWidget(self.search_birthday_according_to_operators_name_button)

        # 根据生日查询是否有对应生日的干员
        # 需要完成根据日期查询干员的功能，需要注意可能会有多个查询结果，即多个干员在同一天生日的可能性
        self.search_operators_according_to_day_button = QPushButton(self.tr('查询某天生日的干员'))
        self.search_operators_according_to_day_button.setFont(QFont('微软雅黑', 10))
        # 设置按钮不可用（对应文件不存在的情况下）
        if not arkjson.is_file():
            self.search_operators_according_to_day_button.setEnabled(False)

        layout.addWidget(self.search_operators_according_to_day_button)

        # 添加显示干员按钮
        self.show_operatos_list_btn = QPushButton('显示所有干员')
        self.show_operatos_list_btn.setFont(QFont(Font_Style, 10))
        if not arkjson.is_file():
            self.show_operatos_list_btn.setEnabled(False)

        layout.addWidget(self.show_operatos_list_btn)

        self.main_quit_button = QPushButton(self.tr('退出'))
        self.main_quit_button.setFont(QFont('微软雅黑', 10))
        self.main_quit_button.clicked.connect(self.close)

        # self.test_btn = QPushButton('测试')
        # self.test_btn.clicked.connect(self.call_test)
        # self.test_btn.setFont(QFont('微软雅黑', 10))
        # layout.addWidget(self.test_btn)

        layout.addWidget(self.main_quit_button)

        self.setLayout(layout)

    def call_test(self):
        QMessageBox.information(self, '爬取信息完毕提示', '爬取信息完毕！', QMessageBox.Ok | QMessageBox.Cancel)

    def activate_spider(self):
        # 爬取信息
        try:
            # 启动一个新的进程独立处理爬虫业务
            craw_process = Process(target=run.run, args=())
            craw_process.start()
            craw_process.join()
            craw_process.close()
            # 爬取信息后，可使用按钮进行查询、
            self.search_birthday_according_to_operators_name_button.setEnabled(True)
            self.search_operators_according_to_day_button.setEnabled(True)
            self.show_operatos_list_btn.setEnabled(False)
            self.show_operatos_list_btn.setText('重新运行程序可查看所有干员')

            reply = QMessageBox.information(self, '爬取信息完毕提示', '爬取信息完毕！', QMessageBox.Ok | QMessageBox.Retry)
            if reply == QMessageBox.Retry:
                # 重试
                self.activate_spider()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainInterface()
    main.show()

    search_from_name_panel = SearchOperatorsBirthdays()
    # 设置exec_则无法同时对多个窗口进行交互，设置show则可以对多个窗口进行交互
    main.search_birthday_according_to_operators_name_button.clicked.connect(search_from_name_panel.exec_)
    search_from_date_panel = SearchFromDate()
    main.search_operators_according_to_day_button.clicked.connect(search_from_date_panel.exec_)
    show_all_operators_panel = ShowALLOperatorsListPanel()
    main.show_operatos_list_btn.clicked.connect(show_all_operators_panel.exec_)

    sys.exit(app.exec_())
