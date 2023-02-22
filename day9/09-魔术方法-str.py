# __str__
# 作用：当print打印对象的时候，可以输出自定义的字符串
# 触发：当对象被print打印的时候
# 注意：必须返回字符串类型


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


s1 = Student('hello', 10)
print(s1)


s2 = Student('good', 10)
print(s2)