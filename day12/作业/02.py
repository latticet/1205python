"""
可以去除传入的字符串里面的所有空格，返回去除空格之后的字符串
"""


def remove_space(string):
    return string.replace(' ', '')


str1 = input('字符串：')
print(remove_space(str1))
