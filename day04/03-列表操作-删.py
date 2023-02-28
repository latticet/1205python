# del 通用语句
# TODO del list[index]
# 根据下标删除指定元素
list1 = ['python', 'mysql']
del list1[1]
print(list1)
print('==' * 20)

# TODO list.remove(元素)
# 说明：删除第一个指定元素
list1 = ['python', 'mysql', 'python']
list1.remove('python')
print(list1)
print('==' * 20)

# TODO list.pop([index])
# 没有参数，弹出列表中的最后一个元素。
# 设置下表, 根据索引弹出元素
# 弹出：删除并返回
list1 = ['python', 'mysql', 'linux', 'git']
# 没有参数
print(list1.pop())
print(list1)

# 有参数
# print(list1.pop(1))
# print(list1)

print(list1.pop(-2))
print(list1)
print('==' * 20)

# TODO list.clear()
# 说明：清空列表
list1 = ['python', 'mysql', 'linux', 'git']
list1.clear()
print(list1)

# 问题讲解
list2 = ['python', 'mysql', 'linux', 'git']
list2.pop()

item = list2.pop()
print(item)
