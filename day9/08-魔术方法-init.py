# __init__:对象初始化方法
# 作用：初始化对象属性
# 触发: 创建类的对象以后

# 定义类
class Demo:
    # 定义魔术方法init
    def __init__(self):
        print('init执行了')


# 创建对象
Demo()
print('==' * 20)


# 定义学生类
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建对象
s1 = Student('hello', 18)
print(s1.name, s1.age)

s2 = Student('good', 19)
print(s2.name)
print(s2.age)

"""
s1 = Student()
s1.name = 'hello'
s1.age = '19'

s2 = Student()
s2.name = 'good'
s2.age = '20'
"""
