# 通用装饰器
def decorator(fn):
    def inner(*args, **kwargs):
        print('前置扩展')
        result = fn(*args, **kwargs)
        print('后置扩展')
        return result

    return inner


# 函数
@decorator
def add1(a, b, c):
    return a + b + c


@decorator
def add2(a, b, c, d, e):
    return a + b + c + d + e


print(add1(1, 2, 3))
print(add2(1, 1, 1, 1, 1))
