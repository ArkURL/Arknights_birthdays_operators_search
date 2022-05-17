# import pickle
import json
import datetime

"""
with open('data.pik', 'rb') as f:
    operators_list = pickle.load(f)
"""


def get_operators_list_for_cmdline():
    try:
        with open('./arknights.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(e)


# 通过日期查询对应生日干员函数
def birth_to_operators():
    operators_list = get_operators_list_for_cmdline()
    prompt = "请输入你的生日(格式为xx月xx日，如12月24日，输入q返回上一级）:"
    while True:
        tag = 0
        user_input = input(prompt)
        if user_input == 'q':
            break
        elif user_input == '今天':
            now = datetime.datetime.now()
            month = now.month
            day = now.day
            user_input = str(month) + '月' + str(day) + '日'
        prompt = "请输入你的生日:"
        for each in operators_list:
            if user_input == each['birthday']:
                print('你和{0}同一天生日哦！'.format(each['name']))
                tag = 1
        if tag == 0:
            print('看来没有和你同一天生日的干员呢...')


# 查询特定干员生日函数
def operators_to_birth():
    operators_list = get_operators_list_for_cmdline()
    prompt = "请输入你要查询的干员（如：能天使，输入q返回上一级）:"
    while True:
        operator = input(prompt)
        prompt = "请输入你要查询的干员:"
        tag = 0
        if operator == 'q':
            break
        for each in operators_list:
            if operator == each['name']:
                print("干员{0}的生日是{1}".format(each['name'], each['birthday']))
                tag = 1
        if tag == 0:
            print('未查询到对应干员，请输入有效的干员名')


if __name__ == '__main__':
    print('测试：根据生日查询干员')
    birth_to_operators()
    print('测试：根据干员名查询生日')
    operators_to_birth()
