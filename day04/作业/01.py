"""
使用if，编写程序，实现以下功能：
从键盘获取用户名、密码
如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误
"""
# 准备系统用户名和密码
sys_username = 'admin'
sys_password = '123456'

# 接收用户输入信息
username = input('用户名：')
password = input('密  码：')

# 判断账号信息
if (username == sys_username) and (password == sys_password):
    print(f'欢迎进入{username}的世界')
else:
    print('密码或者用户名错误')
