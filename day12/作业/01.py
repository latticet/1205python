"""
1. 定义一个模块
模块里面具有 三个类
厨师: 炒菜方法
服务员: 接待客人方法  送走客人方法
收银员: 收钱方法
"""


class Cooker:
    @staticmethod
    def cook():
        print('炒菜')


class Waiter:
    def welcome(self):
        print('接待')

    def bye(self):
        print('送客人')


class Cashier:
    def money(self):
        print('收钱')


