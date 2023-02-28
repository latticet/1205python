# 拷贝
"""
list1 = [1, 2, 3]
list2 = list1
print(list1, id(list1))
print(list2, id(list2))

list3 = list1[:]
print(list3, id(list3))
"""
import copy

# TODO 浅拷贝
# 说明：只拷贝对象的最外层
# 语法：copy.copy(要拷贝的数据) 返回拷贝之后的结果
# list
list1 = [1, 2, ['a', 'b']]
list2 = copy.copy(list1)
print(f'list1:{id(list1)}, list1[-1]:{id(list1[2])}')
print(f'list2:{id(list2)}, list2[-1]:{id(list2[2])}')
print('--' * 20)

# str
str1 = 'hello'
str2 = copy.copy(str1)
print(id(str1))
print(id(str2))
print('==' * 20)

# TODO 深拷贝
# 说明：拷贝对象的所有层级
# 语法；copy.deepcopy(要拷贝的数据) 返回拷贝之后的结果
list1 = [1, 2, ['a', 'b']]
list2 = copy.deepcopy(list1)
print(f'list1:{id(list1)}, list1[-1]:{id(list1[2])}')
print(f'list2:{id(list2)}, list2[-1]:{id(list2[2])}')