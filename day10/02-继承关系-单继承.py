# 一个子类只继承一个父类

# 定义员工类
class Staff:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}吃东西')


# 定义讲师类
class Teacher(Staff):
    def teach(self):
        print(f'{self.name}讲课')


# 定义班主任类
class Manager(Staff):
    def manage(self):
        print(f'{self.name}管理班级')


# 调用
teacher = Teacher('hello', 19)
teacher.eat()
teacher.teach()
print('==' * 20)

manager = Manager('good', 18)
manager.eat()
manager.manage()
