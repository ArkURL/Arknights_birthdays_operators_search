import pickle
import json

'''
with open('data.pik', 'rb') as f:
    operators_list = pickle.load(f)
'''

with open('Arknight_operators_birthdays/arknights.json', 'r', encoding='utf-8') as f:
    operators_list = json.load(f)


# 通过生日查询同一天生日干员函数
def birth_to_operators():
    prompt = "请输入你的生日(格式为xx月xx日，如12月24日，输入q返回上一级）:"
    while True:
        tag = 0
        birth = input(prompt)
        if birth == 'q':
            break
        prompt = "请输入你的生日:"
        for each in operators_list:
            if birth == each['birthday']:
                print('你和{0}同一天生日哦！'.format(each['name']))
                tag = 1
        if tag == 0:
            print('看来没有和你同一天生日的干员呢...')


# 查询特定干员生日函数
def operators_to_birth():
    prompt = "请输入你要查询的干员（如：能天使，输入q返回上一级）:"
    while True:
        operator = input(prompt)
        prompt = "请输入你要查询的干员:"
        tag = 0
        if operator == 'q':
            break
        for each in operators_list:
            if operator == each['name']:
                print("干员{0}的生日是{1}".format(each['name'],each['birthday']))
                tag = 1
        if tag == 0:
            print('未查询到对应干员，请输入有效的干员名')


if __name__ == '__main__':
    birth_to_operators()
    operators_to_birth()
