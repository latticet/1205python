# 装饰器
def wrapper(fn):
    def inner(a, b):
        print('计算中...')
        return fn(a, b)

    return inner


# 函数
@wrapper
def add(a, b):  # add = wrapper(add)
    return a + b


print(add(1, 2))
print(add(5, 2))
