# 类方法
"""
1. 在类的内部定义
2. 在类方法上加一个装饰器
3. 第一个参数必须传入cls
4. 其他和函数相同
"""


# cls:
# cls就是当前类


class Person:
    country = 'China'

    # 定义类方法
    @classmethod
    def get_info(cls):
        print(f'cls:{cls}')
        print(cls.country)
        print('类方法')


# 调用
# 类名.类方法名() [常用]
Person.get_info()
print(f'Person:{Person}')
print('==' * 20)

# 类的实例.类方法名()
Person().get_info()
