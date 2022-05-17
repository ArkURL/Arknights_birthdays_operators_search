# -*- coding:utf-8 -*-
# @Time:2022/5/17 11:42
# @Author:ui_none
import json


def get_operators_list():
    try:
        with open('../arknights.json', 'r', encoding='utf-8') as f:
            operators_list = json.load(f)
            return operators_list
    except Exception as e:
        print(e)


# 图形界面使用
# 通过查询返回结果，注意可能有多个返回结果
def from_date_get_operators(date):
    operators_list = get_operators_list()
    result = []
    for each in operators_list:
        if date == each['birthday']:
            result.append(each['name'])
    return result


# 图形界面使用
# 通过查询直接返回结果
def from_operators_get_birthdays(operator_name):
    operators_list = get_operators_list()
    for each in operators_list:
        if each['name'] == operator_name:
            return each['birthday']
    return False


def from_date_get_test():
    prompt = '按q退出，输入日期查询是否有对应干员在指定日期生日：'
    while True:
        birth = input(prompt)
        if birth == 'q':
            break
        result = from_date_get_operators(birth)
        if len(result) == 0:
            print('看来没有和你同一天生日的干员呢...')
        else:
            for operator in result:
                print(f'你和{operator}同一天生日哦！')

        prompt = '请输入日期，按q退出：'
