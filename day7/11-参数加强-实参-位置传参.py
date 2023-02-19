# 实参的两种传递形式
# 两种方式没有优劣之分，都可以使用
"""
1. 位置传参
2. 关键字传参
"""


# 位置传参
# 说明：按照形参的顺序传入实参

# 定义
def info(name, age, addr):
    print(name, age, addr)


# 调用
info('hello', 18, '成都')
