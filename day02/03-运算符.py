# TODO 数学运算符
# % 取模运算符，求2个数的余数
print(10 % 3)
print(10 % 2)
print('--' * 10)

# ** 幂运算符
# 2的平方
print(2 ** 2)
# 5的立方
print(5 ** 3)
# 3的4次方
print(3 ** 4)
print('--' * 10)

# / 除法运算符
# 得到的结果永远是浮点数
print(10 / 2)
print(10 / 3)
print('--' * 10)

# // 整除运算符
# 得到的结果永远是整数,取结果的整数部分
print(10 // 2)
print(10 // 3)
print('==' * 20)

# TODO 比较运算符
# ==
print(10 == 10)
print(10 == 11)
print('--' * 20)

# !=
print(10 != 10)
print(10 != 11)
print('==' * 20)

# TODO 赋值运算符
# =
# +=
a = 1
b = 2
a += b  # a = a + b
print(a)  # 3

a -= b  # a = a - b
print(a)  # 1

a *= b  # a = a * b
print(a)
print('--' * 20)

b //= 2  # 1
print(b)
b /= 2  #
print(b)

x = 5
x %= 2
print(x)

# TODO 身份运算符
# 数据内存地址的比较
str1 = 'hello'
str2 = 'hello'
print(str1 == str2)

# is
print(str1 is str2)
print(id(str1))
print(id(str2))

num1 = 10000
num2 = 10000

print(num1 is num2)
print('--' * 20)

str3 = 'hello'
str4_1 = 'he'
str4_2 = 'llo'
str4 = str4_1 + str4_2  # 字符串拼接
print(str3 == str4)
print(id(str3))
print(id(str4))
print(str3 is str4)
print('--' * 20)

# is not 比较2个数据不是同一个内存地址
print(str1 is not str2)
print(str3 is not str4)

print('==' * 20)

# TODO 逻辑运算符
# and 并且 &&
# 说明：如果左边的运行结果是True，那么会执行右边。如果左边执行结果是False，那么不执行右边
# False：0，空字符串，空列表，空字典，空集合，空元组
print(10 and 100)
print(0 and 100)
print(100 and 0)
print('ok' and '11')
print('' and 'fail')
print(' ' and 'fail')
print(True and True)
print(True and False)
print('--' * 20)

# or 或者
# 说明：如果左边的运行结果是True，那么不执行右边。如果左边的运行结果是False，那么执行右边
print(10 or 100)
print(0 or 100)
print('0' or 100)
print('' or 'fail')
print(' ' or 'fail')
print(True or True)
print(True or False)
print('--' * 20)

# not 取反 !
print(not 1)
print(not 'ok')
print(not '')
print(not 0)
print(not True)
print(not False)
