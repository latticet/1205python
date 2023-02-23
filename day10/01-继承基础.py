# 定义A类
class A:
    def __init__(self):
        self.name = 'hello'
        self.age = 18


# B类继承A类

# 定义B类
class B(A):
    pass


# 创建B类的实例
b = B()
print(b.name)
print(b.age)
