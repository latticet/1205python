# TODO 语法
"""
while 条件语句:
    while 条件语句:
        循环体
"""

# TODO 练习
# 需求1：
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
"""
j = 0
while j < 5:
    i = 0
    while i < 5:
        print('*', end=' ')
        i += 1
    print()
    j += 1
"""
# 外层循环控制星星的行数，内存循环控制星星个数

# 需求2：
"""
* 
* * 
* * * 
* * * * 
* * * * *
"""
"""
j = 1
while j < 6:
    i = 0
    while i < j:
        print('*', end=' ')
        i += 1
    print()
    j += 1
"""
"""
i = 0
while i < 1:
    print('*')
    i += 1

i = 0
while i < 2:
    print('*', end=' ')
    i += 1
print()

i = 0
while i < 3:
    print('*', end=' ')
    i += 1
print()

i = 0
while i < 4:
    print('*', end=' ')
    i += 1
print()

"""

# 需求3：99乘法表
# \n:换行  \t:tab键
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {i*j}', end='\t')
        j += 1
    print()
    i += 1
