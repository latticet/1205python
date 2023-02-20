num = 100

print(num)


def fn():
    num = 10


fn()

print(num)
print('==')


# global
# 将局部变量声明为全局变量
def fn1():
    # 将num声明为全局变量
    global num
    num = 1000

fn1()
print(num)


# 总结：
"""
1.全局变量可以在全局作用域和局部作用域访问
2.全局变量默认只能在全局作用域修改
3.局部变量只能在局部作用域访问和修改
4.通过global关键字可以将局部变量声明为全局变量
"""


