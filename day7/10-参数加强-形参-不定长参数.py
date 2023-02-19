# 不定长参数
# 说明：不定长这样的形参可以传入任意多个实参


# TODO 位置不定长参数
# 说明：
"""
函数调用时可以传入任意多个位置参数,打包为一个元组（args）
"""


# 定义
def fn1(*args):
    print(args)


# 调用
fn1('a', 1, 2, 'hello', True)
print('==' * 20)


# TODO 关键字不定长参数
# 函数调用时可以传入任意多个关键字实参,打包为一个字典
# 定义
def fn2(**kwargs):
    print(kwargs)


# 调用
fn2(a=1, b=2, c='hello', name='tt', age=19)
print('==' * 20)


# 位置不定长和关键字不定长一起使用
def fn3(*args, **kwargs):
    print(args)
    print(kwargs)


fn3(1, 2, 3, a=100, b=200, c=300)
