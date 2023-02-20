"""
名片管理系统-函数版
"""
# 初始变化名片存储变量
cards = [
    {'name': 'hello1', 'tel': '1111', 'addr': '上海'},
    {'name': 'hello2', 'tel': '2222', 'addr': '北京'}
]


# 添加名片
def add_card():
    # 接收用户输入
    name = input('name:')
    tel = input('tel:')
    addr = input('addr:')

    # 将用户输入的数据封装成字典
    card_info = {'name': name, 'tel': tel, 'addr': addr}

    # 将名片信息添加到列表中（cards）
    cards.append(card_info)
    print(f'【{name}】添加成功')


# 查看所有名片
def show_cards():
    print('姓名\t电话\t地址')
    for card_dict in cards:
        print(f'{card_dict["name"]}\t{card_dict["tel"]}\t{card_dict["addr"]}')


# 修改名片
def edit_card():
    # 接收要修改的姓名
    edit_name = input('要修改姓名：')

    # 遍历名片列表,找到要修改的名片字典，然后进行修改操作
    for card_dict in cards:
        if edit_name == card_dict['name']:
            # 进行修改操作
            card_dict['name'] = input('name:')
            card_dict['tel'] = input('tel:')
            card_dict['addr'] = input('addr:')
            print('修改成功')
            break
    else:
        print('姓名不存在')


# 删除名片
def del_card():
    # 接收要删除的姓名
    del_name = input('要删除的姓名：')

    # 遍历名片列表，找到对应的名片字典， 将其删除
    for card_dict in cards:
        if del_name == card_dict['name']:
            cards.remove(card_dict)
            print('删除成功')
            break
    else:
        print('姓名不存在')


def main():
    while True:
        # 接收用户输入选择功能
        code = input('选择功能[1添加|2显示|3修改|4删除|quit退出]：')

        # 根据用户输入的code选择不同功能
        if code == '1':
            add_card()
        elif code == '2':
            show_cards()
        elif code == '3':
            edit_card()
        elif code == '4':
            del_card()
        elif code == 'quit':
            print('系统退出')
            break
        else:
            print('输入错误')


main()
