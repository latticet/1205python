# 静态方法
# 在类中的定义的函数
# 需要在前面加一个装饰器
# 静态方法属于整个类

class Person:
    # 静态方法定义
    @staticmethod
    def info():
        print('信息')


# 静态方法调用
# 类名.静态方法名()[常用]
Person.info()

# 类实例.静态方法名()
Person().info()
