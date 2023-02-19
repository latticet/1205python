# 函数说明文档，也就是函数注释的标准写法
"""
语法：
def fn():
    '''
    函数的注释
    '''
    函数体
说明：
写在函数的最上面
"""


# 求2个数的和
def add(a, b):
    """
    求2个数的和（函数功能描述）
    :param a: int 数字1
    :param b: int 数字2
    :return: int 2个数的和
    """
    return a + b

# help()
# 获取函数的说明文档
help(add)

help(print)
