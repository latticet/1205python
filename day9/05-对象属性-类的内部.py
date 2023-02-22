# 对象属性类的内部操作
# 类的内部->对象方法中

# 定义类
class Person:
    # 定义对象方法
    def set_info(self):
        # TODO 增：设置属性
        # 语法：self.attr = value
        self.name = 'hello'
        self.age = 18

    def get_info(self):
        # TODO 查询
        print(self.name)
        print(self.age)

    def edit_info(self):
        # TODO 修改
        self.name = 'good'
        self.age = 10

    def del_info(self):
        # TODO 删除
        del self.name
        del self.age


# 创建对象
p1 = Person()
p1.set_info()

print(p1.name)
print(p1.age)
print('==' * 20)

# 调用查询方法
p1.get_info()
print('==' * 20)

# 调用修改方法
p1.edit_info()
p1.get_info()

# 调用删除
p1.del_info()
# p1.get_info()
print(p1.name)
print(p1.age)
