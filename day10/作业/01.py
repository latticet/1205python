"""
1. 新建一个文件，定义一个猫类，创建一个猫对象，调用上面的属性和方法
2. 新建一个文件，定义一个狗类，创建一个狗对象，调用上面的属性和方法

4. 定义一个高级字符串工具类
   具有如下方法:
   将给定字符串反转（传入abcd返回dcba）
"""


class Cat:
    def __init__(self, name, age):
        # 初始化属性
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}吃东西')

    def run(self):
        print(f'{self.name}跑步')


# 调用
cat = Cat('hello', 10)
cat.eat()
cat.run()
