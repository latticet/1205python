# TODO ● type  查看数据类型
print(type(10))
print(type('hello'))


class Demo():
    def __init__(self):
        self.name = 10

    def info(self):
        pass


print(type(Demo()))
print('==' * 20)

# TODO ● dir  查看对象上所有方法和属性
print(dir(Demo()))
print('==' * 20)


# TODO ● isinstance  查看对象是否属于某个类. True|False
# isinstance(obj, class)
class Demo2:
    pass


demo1 = Demo()
demo2 = Demo2()
print(isinstance(demo1, Demo))
print(isinstance(demo2, Demo))

print(isinstance(10, int))
print(isinstance('hello', str))
print(isinstance([], list))
isinstance('hello', object)
isinstance(demo1, object)
