# 1. 编写1个python程序，完成以下要求
# A. 从键盘获取用户的姓名、性别、家庭地址
# B. 使用一个print输出： 姓名，男，地址：
# 接收用户输入
name = input('姓名：')
gender = input('性别：')
address = input('地址：')

# 格式化输出
info = f'姓名：{name}, 性别：{gender}, 地址：{address}'
print(info)
