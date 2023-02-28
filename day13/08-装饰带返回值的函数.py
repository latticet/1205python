# 装饰器
def wrapper(fn):
    def inner():
        print('正在计算中...')
        return fn()

    return inner


# 函数
@wrapper
def add():    # add = wrapper(add)
    return 1 + 2


print(add())
