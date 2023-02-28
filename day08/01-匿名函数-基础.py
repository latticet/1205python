# lambda表达式【匿名函数】
# 语法：lambda [参数列表]:表达式
# 返回：表达式的运行结果
# 注意：这儿不能写return，会自动把表达式的结果返回

# 求1和2的和
def add1():
    return 1 + 2


add2 = lambda: 1 + 2
print(add2())


# 求任意2个数的和
def add3(a, b):
    return a + b


add4 = lambda a, b: a + b
print(add4(1, 2))




