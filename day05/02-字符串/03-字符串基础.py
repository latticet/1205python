# 容器
"""
str
list
tuple
"""
# 普通数据
"""
int float
bool
None
"""
# 可变不可变
"""
# 可变
list
dict
# 不可变
tuple
str
int float
bool
"""

# TODO 定义
# 单引号
str1 = 'hello'
# 双引号
str2 = "hello"
# 说明: 单引号双引号的定义方式没有区别

# 三单引号
str3 = '''hello'''
# 三双引号
str4 = """hello"""
print(str3, type(str3))
print(str4, type(str4))
# 说明：三单引号和三双引号没有任何区别
print('==' * 20)

# 三个引号和2个引号的区别
# 三个引号的字符串会保留字符串的原生格式
str5 = 'hello' \
       'world'

str6 = '''
    hello
    world
'''

print(str5)
print('--' * 20)
print(str6)
print('--' * 20)
