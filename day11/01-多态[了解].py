"""
多态实现：
1. 有继承关系
2. 子类重写父类方法
3. 调用这个方法
"""


# 定义
class Animal:
    def call(self):
        print('动物叫')


class Dog():
    def call(self):
        # 开始时间
        print('旺旺旺')
        # 结束时间
        # 结束时间 - 开始时间


class Cat():
    def call(self):
        # 开始时间
        print('喵喵喵')
        # 结束时间
        # 结束时间 - 开始时间


class Person():
    def call(self):
        # 开始时间
        print('你过来啊')
        # 结束时间
        # 结束时间 - 开始时间


# 调用
"""
dog = Dog()
cat = Cat()

dog.call()
cat.call()
"""


# 多态方式调用
def do_call(obj):
    # 开始时间
    obj.call()
    # 结束时间
    # 结束时间 - 开始时间


do_call(Dog())
do_call(Cat())
do_call(Person())
