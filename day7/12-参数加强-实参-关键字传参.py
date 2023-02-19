# 关键字传参
# 说明：按照形参的名字传入实参。关键字传参和传入顺序没有关系，只和名字有关系。

# 定义
def info(name, age, addr):
    print(name, age, addr)


# 调用
info(age=18, name='zs', addr='重庆')
