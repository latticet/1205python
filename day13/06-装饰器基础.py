def fn1():
    # 开始时间
    print(1111)
    # 结束时间
    # 结束时间 - 开始时间


def fn2():
    # 开始时间
    print(2222)
    # 结束时间
    # 结束时间 - 开始时间


def fn3():
    # 开始时间
    print(3333)
    # 结束时间
    # 结束时间 - 开始时间


# 装饰器(特殊的闭包)
def wrapper(fn):  # fn: 要装饰的那个函数
    def inner():
        # 前置扩展
        print('前置扩展')
        fn()
        # 后置扩展
        print('后置扩展')

    return inner


inner = wrapper(fn1)
inner()

inner = wrapper(fn2)
inner()
