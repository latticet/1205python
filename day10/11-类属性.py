# 类属性
"""
class 类名:
    类属性 = 属性值
"""
# 说明
# 类属性属于整个类


class Person:
    # TODO 类属性定义
    country = '中国'


# TODO 类属性访问
# 类名.类属性名
print(Person.country)
# 类的实例.类属性名
print(Person().country)

# TODO 类属性修改
# 类名.类属性名 = value
Person.country = 'China'   # 类属性
# 不能通过对象修改
p1 = Person()
p1.country = 'xxx'   # 对象属性

print(Person.country)   # China
print(p1.country) # xxx
