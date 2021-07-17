# -*- coding: UTF-8 -*
import pickle
import json


def save_data():
    with open('Arknight_operators_birthdays/arknights.json', 'r') as data:
        # 将json文件读取成python对象
        operators_list = json.load(data)

        with open('data.pik', 'wb') as file:
            # 将读取的列表以pickle保存到本地
            pickle.dump(operators_list, file)


if __name__ == '__main__':
    save_data()
