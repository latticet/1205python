# TODO str.isspace()  判断字符串是否是空格
str1 = 'hello'
print(str1.isspace())  # False

str2 = 'hello world'
print(str2.isspace())  # False

str3 = ' '
print(str3.isspace())  # True
print('==' * 20)

# TODO * str.isalnum()  判断字符串是数字或者字母
print('hello'.isalnum())  # True
print('123'.isalnum())  # True
print('aa123'.isalnum())  # True
print('==' * 20)

# TODO * str.isalpha()  判断字符串是字母
print('abc'.isalpha())
print('123'.isalpha())
print('a12'.isalpha())
print('==' * 20)

# TODO str.isdecimal() 判断字符串是整数
print('123'.isdecimal())  # True
print('11.1'.isdecimal())  # False
print('abc'.isdecimal())  # False
print('==' * 20)

# TODO * str.isdigit() 判断字符串是整数
print('123'.isdigit())
print('12.3'.isdigit())
print('==' * 20)

# TODO str.isnumeric() 判断字符串是整数，支持中文
print('一二三'.isnumeric())
print('12.3'.isnumeric())
print('==' * 20)

# TODO str.istitle() 判断字符串中单词首字母大写
print('hello world'.istitle())
print('Hello world'.istitle())
print('Hello World'.istitle())
print('==' * 20)

# TODO str.islower() 判断字符串是全小写
print('hello world'.islower())
print('Hello world'.islower())
print('hello World'.islower())
print('==' * 20)

# TODO str.isupper() 判断字符串是全大写
print('hello world'.isupper())
print('Hello world'.isupper())
print('hello World'.isupper())
print('HELLO WORLD'.isupper())
print('==' * 20)

# TODO str.isdigit() 特殊格式的数字
print('①'.isdigit())
print('1'.isdigit())
print('==' * 20)

# TODO str.isnumeric()
print('123'.isnumeric())
print('123'.isnumeric())

"""
num = input('num1：')
# 判断是数字在进行转换
if num.isdigit():
    num = int(num)
"""
