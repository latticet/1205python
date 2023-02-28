# TODO 多个值赋值给多个变量
a, b, c = 1, 2, 3

# TODO 交换变量的值
x = 100
y = 200
# 把x的值赋值给y， 把y的值赋值给x
# 传统方式
z = x
x = y
y = z
print(x, y)
print('--' * 20)

x, y = y, x
print(x, y)

# TODO 多个变量赋相同的值
m = n = t = 100
print(m, n, t)
# 语法规范：必须遵守 不遵循SyntaxError
# 编码规范：不是必须 PEP8

# 格式化：Ctrl Alt l
