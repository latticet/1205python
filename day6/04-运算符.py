# TODO + 拼接运算符
# 使用：序列
# str
str1 = 'hello' + ' world'
print(str1)

# list
list1 = [1, 2] + [3, 4]
print(list1)
list2 = ["1", "2"] + ['a', 'b'] + ["1", "2"]
print(list2)

# tuple
t1 = (1, 2) + (2, 3)
print(t1)

# TODO * 重复拼接
# 适用：序列
# 注意：序列只能和正整数相乘
# str
str1 = '||||' * 2
print(str1)
# list
list1 = ['a', 'b'] * 2
print(list1)
# tuple
t1 = (1, 2) * 3
print(t1)

print('==' * 20)

# TODO in 判断元素在容器中
print('1' in {'1', '2'})
d1 = {'name':'hello', 'age':19}
print('name' in d1)
print('name' in d1.keys())
print('hello' in d1.values())

# TODO not in 判断元素不在容器中
print('name' not in d1)