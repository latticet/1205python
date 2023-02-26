name = 'module1'


def fn1():
    print('module1中的fn1函数')


class Demo:
    pass


# __all__
# 说明：指定from...import * 时导入的资源。列表类型
# 注意：写的是标识符的字符串形式

__all__ = ['name', 'fn1']
