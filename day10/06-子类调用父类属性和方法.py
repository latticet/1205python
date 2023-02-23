# 子类在和父类同名的情况下
# 子类调用父类的方法
# super():指向上级类


class Person:
    def __init__(self):
        self.name = '人类'
        self.age = 100

    def eat(self):
        print('人类eat')


# 学生类
class Student(Person):
    def __init__(self):
        super().__init__()
        self.code = 100
        self.classinfo = '1班级'

    def eat(self):
        super().eat()
        print('学生eat')


s1 = Student()
print(s1.name)
print(s1.age)
print(s1.code)
print(s1.classinfo)

print('--' * 20)

s1.eat()
