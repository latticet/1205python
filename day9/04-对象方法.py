# 对象方法
# 定义类
class Person:
    # TODO 对象方法定义
    def eat(self):
        print(f'self:{self}')
        # print('吃饭')


"""
关于对象方法定义
1. 在类的内部定义
2. 第一个参数必须是self
3. 其他和函数都相同
4. self不需要手动传入，python解释器会自动把当前对象传入
"""
# TODO 对象方法调用
# 语法：obj.方法名()
# 创建对象
p1 = Person()
p1.eat()
print(f'p1:{p1}')

print('==' * 20)

p2 = Person()
p2.eat()
print(f'p2:{p2}')

"""
关于self
1. self指向当前的对象（self就是调用当前方法的对象）
"""
