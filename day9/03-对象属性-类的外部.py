# 定义类
class Person:
    # 类的内部
    pass


# 创建对象
p1 = Person()

# TODO 增：为对象设置属性
# 语法：obj.属性名(attr) = 属性值(value)
p1.name = '胡会'
p1.age = 18

# TODO 查
# 语法：obj.attr
print(p1.name)
print(p1.age)

# TODO 改
# 语法：obj.属性名(attr) = 属性值(value)  # attr:attribute
p1.name = '雪梅'
p1.age = 19
print(p1.name)
print(p1.age)

# TODO 删
# del obj.attr
del p1.name
print(p1.name)