# 类和对象的关系
# 先定义类，通过类创建对象


# 定义类
class Person:
    pass


# 创建对象
"""
类名()
"""
p1 = Person()
print(p1)      # 16进制
# print(id(p1))  # 10进制
print(hex(id(p1)))

p2 = Person()
print(p2)
print(hex(id(p2)))

"""
说明：
1. 一个类可以创建多个对象
2. 对象之间是隔离的.每创建一个对象就开启新的内存空间进行存储。
"""
