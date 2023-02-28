# 函数返回None一共有三种情况

# TODO 第一种
# 函数在没有写return的情况下，会返回None
def fn1():
    result = 1 + 1


print(fn1())


# 练习
def fn11(a, b):
    print(a + b)


print(fn11(1, 2))
print('==' * 20)


# TODO 第二种
def fn2():
    return None


print(fn2())


# TODO 第三种
# return什么都不写，返回的也是None
def fn3():
    return


print(fn3())
