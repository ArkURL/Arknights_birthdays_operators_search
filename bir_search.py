import pickle
import json

"""
with open('data.pik', 'rb') as f:
    operators_list = pickle.load(f)
"""


def get_operatos_list():
    try:
        with open('../arknights.json', 'r', encoding='utf-8') as f:
            operators_list = json.load(f)
            return operators_list
    except Exception as e:
        print(e)


# 图形界面使用
# 通过查询直接返回结果
def from_operatos_get_birthdays(operator_name):
    operators_list = get_operatos_list()
    for each in operators_list:
        if each['name'] == operator_name:
            return each['birthday']
    return False


# 图形界面使用
# 通过查询返回结果，注意可能有多个返回结果
def from_date_get_operators(date):
    operators_list = get_operatos_list()
    result = []
    for each in operators_list:
        if date == each['birthday']:
            result.append(each['name'])
    return result

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



# 通过生日查询ri天生日干员函数
def birth_to_operators():
    operators_list = get_operatos_list()
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
    operators_list = get_operatos_list()
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
    print('测试：根据生日查询干员')
    birth_to_operators()
    print('测试：根据干员名查询生日')
    operators_to_birth()
    print('图形界面用测试：根据生日查询干员')
    from_date_get_test()