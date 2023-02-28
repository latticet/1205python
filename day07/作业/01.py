"""
写一个后期网络聊天项目的模块，用户不断从键盘输入，
每次输入回车后，将打印用户输入的字符个数和内容，
当用户输入'quit'后，退出该功能
"""

while True:
    msg = input('用户信息：')

    # 　判断如果用户输入的是‘quit’，那么break
    if msg == 'quit':
        print('退出的时候给他写一句话')
        break

    print(f'长度:{len(msg)}, 内容：{msg}')
