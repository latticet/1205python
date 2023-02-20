"""
编写1个python程序，完成以下要求：
4.1 设计一个功能从键盘获取用户的姓名、性别、家庭地址
4.2 打印从该功能中获取的信息
"""


def info():
    # 接收用户输入
    name = input('name:')
    gender = input('gender:')
    addr = input('addr:')

    # 输出信息
    print(f'name:{name}, gender:{gender}, addr:{addr}')


info()
