# __del__
# 作用：对象销毁之前的收尾工作
# 触发：对象被销毁前

# 定义类
class Demo:
    def __del__(self):
        print('del执行了')


# 创建对象
d1 = Demo()
# del d1
