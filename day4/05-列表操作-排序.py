# TODO list.sort()
# 升序：从小到大
list1 = [10, 11, 20, 3, 9, 35]
print(list1)
list1.sort()
print(list1)

# 降序：从大到小
# list.sort(reverse=True)
list1.sort(reverse=True)
print(list1)
print('--' * 20)

list2 = ['ab', 'cd', 'b', 'f', 'g', 'k']
list2.sort()
print(list2)
print('--' * 20)

"""
# 类型不同不能排序
list3 = ['hello', 'word', 12, 11]
list3.sort()
print(list3)
"""

print('==' * 20)

# TODO list.reverse()
list1 = [10, 11, 20, 3, 9, 35]
list1.reverse()
print(list1)
print('==' * 20)

# 问题
list1 = [10, 11, 20, 3, 9, 35]
# list.pop()
print(list1.pop())  # 返回删除的那个元素  None
print(list1)

# list.sort()
print(list1.sort())

print(list1.index(10))
