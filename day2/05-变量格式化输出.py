# 变量格式化输出
# 说明：将变量和字符串拼接在一起输出的过程
"""
# 接收用户输入
name = input('姓名:')
age = input('年龄:')

# 姓名：xxx， 年龄：xx岁
print('姓名：', name, '年龄：', age)
"""

# TODO f格式化
"""
name = input('姓名:')
age = input('年龄:')
print(f'姓名：{name}\n年龄：{age}岁')
"""
# TODO %格式化
# 先使用占位符进行占位，然后填充内容
# %s 字符串占位符
# %d 整型占位符
# %f 浮点型占位符, 默认保留小数点后6位 %.nf:n小数点后保留位数
"""
name = input('姓名:')
age = int(input('年龄:'))
height = float(input('身高：'))

print(height)
# 格式化一个变量
print('姓名：%s' % name)
print('年龄：%d' % age)
print('身高：%f' % height)
print('身高：%.2f' % height)

# 同时格式化多个变量
print('姓名：%s， 年龄：%d岁, 身高:%f厘米' % (name, age, height))
"""

# 整型占位符，填充0
# num1 = int(input('数字：'))
# print('数字：%04d' % num1)

# 验证码
"""
import random

random_num = random.randint(1, 999999)
code = '%06d' % random_num
print(code)
"""
