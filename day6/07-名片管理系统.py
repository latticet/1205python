"""
名片管理 系统
# 名片盒子  列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
cards = [
    {“name”:”张三”,”tel”:”17715154242”,”job”:”CEO”,”addr”:”天府新谷”,”company”:”源码时代”},  # 字典
    {名片信息2},
    {名片信息3}
]
需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面  cards.append(一个人的名片字典)
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片:  录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
    如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""
# 初始变化名片存储变量
cards = [
    {'name': 'hello1', 'tel': '1111', 'addr': '上海'},
    {'name': 'hello2', 'tel': '2222', 'addr': '北京'}
]

while True:
    # 接收用户输入选择功能
    code = input('选择功能[1添加|2显示|3修改|4删除|quit退出]：')

    # 根据用户输入的code选择不同功能
    if code == '1':
        # 接收用户输入
        name = input('name:')
        tel = input('tel:')
        addr = input('addr:')

        # 将用户输入的数据封装成字典
        card_info = {'name': name, 'tel': tel, 'addr': addr}

        # 将名片信息添加到列表中（cards）
        cards.append(card_info)
        print(f'【{name}】添加成功')
    elif code == '2':
        # 输出信息的字段名
        print('姓名\t电话\t地址')
        for card_dict in cards:
            print(f'{card_dict["name"]}\t{card_dict["tel"]}\t{card_dict["addr"]}')
    elif code == '3':
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
    elif code == '4':
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
    elif code == 'quit':
        print('系统退出')
        break
    else:
        print('输入错误')
