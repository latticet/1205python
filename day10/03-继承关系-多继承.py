# 一个子类同时继承多个父类
"""
语法：
class A(B, C, D):
    pass
A类继承了B、C、D类
"""


# 定义人类
class Person:
    def __init__(self):
        self.name = '佩奇'
        self.age = 3

    def talk(self):
        print(f'{self.name}说话')


# 定义猪类
class Pig:
    def call(self):
        print(f'{self.name}哼哼')


# 定义佩奇
class PeiQ(Person, Pig):
    pass


peiq = PeiQ()
peiq.talk()
peiq.call()
