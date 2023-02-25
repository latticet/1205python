# init，str，del
# __new__
# 作用：创建对象并且返回对象
# 触发：创建对象时

class Demo(object):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


demo = Demo()
print(demo)  # None
