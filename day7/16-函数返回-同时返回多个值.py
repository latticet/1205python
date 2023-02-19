# 函数同时返回多个值
"""
语法：
def fn():
    return 表达式1, 表达式2, ...
说明：
函数返回的多个值，会打包到元组中
"""


def fn1():
    return 1, 2, 'python', 'mysql'


a, b, c, d = fn1()
print(a, b, c, d)
