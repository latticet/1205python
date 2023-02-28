# 装饰器
def wrapper(fn):
    def inner():
        print('前置')
        fn()
        print('后置')

    return inner


# 被装饰的函数
@wrapper
def demo1():  # demo1 = wrapper(demo1)
    print('demo1')


@wrapper
def demo2():
    print('demo2')


demo1()

demo2()
