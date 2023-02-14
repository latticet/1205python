# for循环
# 作用：遍历可迭代的数据[str, list, tuple, dict]
# 遍历：将容器中的数据依次获取

list1 = ['python', 'git', 'mysql', 'linux']
"""
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
"""
# 循环
# while循环
# len:length
"""
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
"""

# TODO for循环语法
list1 = ['python', 'git', 'mysql', 'linux']
"""
for 临时变量 in 要遍历的数据:
    代码块：临时变量
"""
# list
for item in list1:
    print(item)

print('--' * 20)

# str
str1 = 'hello'
for char in str1:
    print(char)
