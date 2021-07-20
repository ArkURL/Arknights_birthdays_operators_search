import bir_search as b

"""
主执行脚本，使用本脚本查询干员生日或查询是否有对应日期生日的干员
"""

# import save_local as s  # 已被优化的保存-调用方法，当然取消注释后也可以使用


# 主函数
def main():
    # 首先先保存data到本地
    # s.save_data()，此保存方式已被优化，可以直接加载ark.json而不需要保存成pickle再调用
    prompt = "欢迎使用干员生日查询器，按1通过生日查询同一天生日的干员，按2查询特定干员的生日,输入q退出:"
    while True:
        choice = input(prompt)
        prompt = "输入1启动生日-干员查询，输入2启动干员-生日查询，输入q退出程序:"
        if choice == '1':
            # 通过生日查询同一天生日的干员函数
            b.birth_to_operators()
        elif choice == '2':
            # 查询干员生日程序函数
            b.operators_to_birth()
        elif choice == 'q':
            break
    print('感谢使用明日方舟干员-生日查询器！')


if __name__ == '__main__':
    main()
