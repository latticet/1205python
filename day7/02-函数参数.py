# 需求1:
# 求1和2的和
def add1():
    print(1 + 2)


add1()


# 需求2:
# 求3和5的和
def add2():
    print(3 + 5)


add2()


# 需求3:
# 求10和20的和
def add3():
    print(20 + 20)


add3()

print('==' * 20)


# TODO 参数
# 解决函数通用性问题
# 定义时的参数叫做形式参数：形参
def add(a, b):
    print(a + b)


# 调用时的参数叫做实际参数：实参
add(1, 2)
add(2, 3)
add(5, 3)
add(10, 20)

# 说明：实参必须和形参一一对应
