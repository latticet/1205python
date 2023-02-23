# 受保护成员：只能在类内部，派生类中访问的属性和方法
# 受保护（protected）
# 语法：
"""
_attr
_fn
"""


class Demo:
    def __init__(self):
        # 受保护属性
        self._name = 'hello'

    def get_info(self):
        print(self._name)


Demo().get_info()


class SubDemo(Demo):
    def get_info(self):
        print(self._name)


# 在派生类中
SubDemo().get_info()

# 在类的外部
print(Demo()._name)
