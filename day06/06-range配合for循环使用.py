# for循环
# TODO  遍历容器
# str， list， tuple， dict， set
"""
for 临时变量 in 容器:
    代码块 临时变量
"""

# TODO 控制循环次数
# range()
# 说明：创建一个可迭代（可遍历的）对象
# 语法：range(start, stop[, step])
# start,stop,step必须是正整数
# start: 开始数字,默认是0
# stop: 结束数字，不包括stop
# step: 步长，默认为1
# range(0, 5)  # [0, 1, 2, 3, 4]
print(range(0, 3))
print(list(range(0, 3)))
print(list(range(3)))
print('==' * 20)

print(list(range(0, 5, 2)))
print('==' * 20)

# for循环次数
for i in range(5):
    print(i)
print('==' * 20)

# 1-9
for i in range(1, 10):
    print(i)

print('==' * 20)

# 1-10之间的偶数
for i in range(2, 11, 2):
    print(i)

# 用for循环实现99乘法表