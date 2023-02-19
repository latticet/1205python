# 拆包
# 元组拆包
a, b, c = (1, 2, 3)

x, y, z = {'a': 1, 'b': 2, 'c': 3}
print(x, y, z)

x, y, z = {'a': 1, 'b': 2, 'c': 3}.values()
print(x, y, z)

print('==' * 20)


# TODO 针对位置传参的拆包
# list，tuple, str
# 定义函数
def fn1(name, age):
    print(name, age)


info = ['hello', 18]
# info = ('你好', '10')
# 调用函数
# fn1(info[0], info[1])
fn1(*info)
print('==' * 20)


# TODO 针对关键字传参的拆包
# 注意:字典的key必须和形参一一对应
# 定义
def fn1(name, age):
    print(name, age)


info_dict = {'name': 'hello', 'age': 18}
# 调用
fn1(age=info_dict['age'], name=info_dict['name'])

fn1(**info_dict)  # name='hello', age='18'
