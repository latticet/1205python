# TODO int()
# 说明：将其他数据类型转换为整型

# str -> int
# 注意：只能将整数型字符串转换为整型

"""
str1 = '10'
num1 = int(str1)
print(num1, type(num1))

str2 = '1abc'
num2 = int(str2)
print('--' * 20)

str3 = '10.1'
num3 = int(str3)
"""

# float -> int
float1 = 10.1
num1 = int(float1)
print(num1, type(num1))
print('==' * 20)

# bool -> int
num2 = int(True)
num3 = int(False)
print(num2, type(num2))
print(num3, type(num3))

# TODO float()
# 将其他数据类型转换为浮点型
# int -> float
f1 = float(10)
f2 = float(0)
print(f1, type(f1))
print(f2, type(f2))
print('--' * 20)

# str -> float
# 注意：只能将数字型字符串进行转换
str1 = '10'
str2 = '10.1'
str3 = '1abc'
f1, f2 = float(str1), float(str2)
print(f1, type(f1))
print(f2, type(f2))
"""
不能转换
f3 = float(str3)
print(f3, type(f3))
"""
print('--' * 20)

# bool -> float
f1, f2 = float(True), float(False)
print(f1, type(f1))
print(f2, type(f2))
print('==' * 20)

# TODO str()
# 将其他数据类型转换为字符串
# int -> str
str1 = str(10)
print(str1, type(str1))

str2 = str(0)
print(str2, type(str2))
print('--' * 20)

# float -> str
str3 = str(10.1)
print(str3, type(str3))
print('--' * 20)

# bool -> str
str4 = str(True)
str5 = str(False)
print(str4, type(str4))
print(str5, type(str5))
