# 函数可以作为参数使用，也可以作为返回值使用。和使用变量效果是一样的。

def add(a, b):
    return a + b


def dec(a, b):
    return a - b


# str1 = 'hello'

# 运算功能的函数
def operation(fn, num1, num2):
    # 加减乘除的运算
    return fn(num1, num2)


print(operation(add, 4, 5))
print(operation(dec, 5, 1))

# 使用lambda表达式作为运算
print(operation(lambda x, y: x * y, 2, 20))
print(operation(lambda x, y: x / y, 20, 2))
print(operation(lambda x, y: x // y, 20, 2))
