"""
1. 写代码，有如下变量，请按照要求实现每个功能
name = "  posekakaka  "
"""
# a. 移除name 变量对应的值两边的空格，并输出移除后的内容name = "posekakaka"
name = "  posekakaka  "
print(name.strip())
name = name.strip()
print('==' * 20)

# b. 判断name 变量对应的值是否以 "po" 开头，并输出结果
print(name.startswith('po'))
print('==' * 20)

# c. 判断name 变量对应的值是否以 "a" 结尾，并输出结果
print(name.endswith('a'))
print('==' * 20)

# d. 将name 变量对应的值中的 “k” 替换为 “c”，并输出结果
print(name.replace('k', 'c'))
print('==' * 20)

# e. 将name 变量对应的值根据 “k” 分割，并输出结果。
print(name.split('k'))
print('==' * 20)

# f. 请问，上一题 e 分割之后得到值是什么类型（可选）
# list