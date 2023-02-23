# 子类重写(覆盖)父类属性和方法
# 说明：子类和父类有同名的方法这种情况

# 人类
class Person:
    def __init__(self):
        self.name = '人类'
        self.age = 100

    def eat(self):
        print('人类eat')


# 学生类
class Student(Person):
    def __init__(self):
        self.name = '学生'
        self.age = 10

    def eat(self):
        print('学生eat')


s1 = Student()
print(s1.name)
print(s1.age)

s1.eat()