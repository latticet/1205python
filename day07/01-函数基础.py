a = 'AAAAAAAAAAAAAAAAAAAA'
"""

for i in range(3):
    print(a)

print(111)

for i in range(3):
    print(a)

print(222)

for i in range(3):
    print(a)
    
"""
# TODO 函数说明
# 函数是一个带名字的代码块
# 名字：函数名
# 代码块：函数体

# TODO 函数使用
## 定义
"""
语法:
def 函数名():
    代码块(函数体)
    
函数名命名规范：
必须符合标识符的命名规范
"""


# 定义了一个名字叫info的函数
def info():
    for i in range(5):
        print(a)


## 调用
"""
语法：
函数名()
"""

info()

# TODO 总结函数特点
"""
1. 函数定义的时候不执行，只有在调用的时候才会执行
2. 一次定义多次调用。解决冗余代码和后期扩展维护问题。
3. 函数会把运行结果返回到调用的地方
"""
