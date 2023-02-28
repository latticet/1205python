"""
设计根据QQ和密码登录的过程(QQ和密码预设为指定的值).
执行结果为登录是否成功(boolean类型的值)
"""
"""
# 预设账号密码
username = '123456'
password = '123456'

# 接收用户输入
new_username = input('username:')
new_password = input('password:')

if new_username == username and new_password == password:
    print(True)
else:
    print(False)
"""


def login():
    # 预设账号密码
    username = '123456'
    password = '123456'

    # 接收用户输入
    new_username = input('username:')
    new_password = input('password:')

    if new_username == username and new_password == password:
        return True
    else:
        return False


print(login())
