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
# 得到的结果永远是整数
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
print('==' *20)

# TODO 赋值运算符
# +=
a = 1
b = 2
a += b   # a = a + b
print(a)  # 3

a -= b   # a = a - b
print(a)  # 1

a *= b   # a = a * b
print(a)
print('--' * 20)

b //= 2  # 1
print(b)
b /= 2   #
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
str4 = str4_1 + str4_2   # 字符串拼接
print(str3 == str4)
print(id(str3))
print(id(str4))
print(str3 is str4)
