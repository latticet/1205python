# 拆包
# 说明：将元组中的元素依次赋值给多个变量

t1 = ('python', 'mysql', 'linux')

# 拆包语法
# 语法：var1, var2, var3, ... = (item1, item2, item3, ...)
# 注意：变量名和元素要一一对应

a, b, c = t1
print(a, b, c)

# 一般我们使用的都是元组拆包
# list
a, b, c = [1, 2, 3]
print(a, b, c)

# str
a, b, c = 'xyz'
print(a, b, c)

