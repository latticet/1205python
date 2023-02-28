# 输入
# 说明：接收用户的输入,返回输入的结果
# 语法：input('用户输入提示信息')
# 特点：
"""
1.阻塞代码继续向下运行
2.输入内容回车继续向下运行
3.input不管输入什么内容，返回的都是字符串类型
"""
# 接收姓名
name = input('姓名：')
print(name)
print(type(name))
print('==' * 20)

# 接收年龄
age = input('年龄：')
print(age)
print(type(age))

# 体重
weight = input('体重：')
print(weight)
print(type(weight))
