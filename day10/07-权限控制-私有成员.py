# 私有成员：成员（属性和方法），只能在类的内部访问的属性和方法
# 私有成员语法：
"""
__attr = value
__fn
"""


class Person:
    def __init__(self):
        # 公有属性
        self.a = 100
        # 私有属性
        self.__b = 200

    def info(self):
        # TODO 在类的内部访问私有成员
        print(self.__b)

    def __fn(self):
        print('这是一个私有方法')

    def get_fn(self):
        self.__fn()


p1 = Person()

# 在类的内部可以访问到私有成员
p1.info()
p1.get_fn()

print('--' * 20)


# TODO 在派生类中访问私有成员
class Stu(Person):
    def sub_info(self):
        print(self.a)
        print(self.__b)

    def get_fn(self):
        self.__fn()


# 派生类中不能访问私有成员
"""
Stu().sub_info()
Stu().get_fn()
"""

# TODO 在类的外部访问私有成员
"""
print(Person().__b)
Person().__fn()
"""
# _类名__成员名
print(Person()._Person__b)
Person()._Person__fn()
