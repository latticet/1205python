# str tuple list 都可以使用切片
# 索引
# 语法：list[index]
"""
list1 = ['python', 'mysql', 'linux', 'git', 'shell']
print(list1[0])
print(list1[-3])
"""
# 切片
# 说明：利用索引批量获取列表中的元素,切片返回的还是原数据类型。对原数据不造成影响
# 语法：list[start:end:step]
# start:开始下标，默认是0
# end:结束下标，不包括结束下标. 不指定具体结束下标，提取到末尾
# step:步长，默认是1
list1 = ['python', 'mysql', 'linux', 'git', 'shell', 'xx']
print(list1[0:2])
print(list1)
print('--' * 20)

# step
print(list1[:5:1])
print(list1[:5:2])
print(list1[:5:3])
print(list1[:5:4])

print('--' * 20)

# end：不指定具体下标
list1 = ['python', 'mysql', 'linux', 'git', 'shell']
print(list1[:])  # 列表复制
print(list1)

print(list1[3:])
print(list1[1::2])
print('==' * 20)

# 语法：list[start:end:step]
# start end负数
# step: 负责切片的方向
# 正数：由左至右进行切片
# 负数：由右至左进行切片
list1 = ['python', 'mysql', 'linux', 'git', 'shell']
# ['linux', 'git', 'shell']
# print(list1[2:])
print(list1[-3:])
print('--' * 20)

# step:负数
# 'python', 'mysql'
# 列表反转
print(list1[::-1])
print(list1[::-2])
print('--' * 20)

print(list1[1:4])
print(list1[1:4:-1])
print('--' * 20)

# 列表反转
list1 = ['python', 'mysql', 'linux', 'git', 'shell']
# list.reverse()
list1.reverse()  # 对原数据进行反转
print(list1)
print('--' * 20)
# list[::-1]
list2 = list1[::-1]  # 不影响原数据
print(list2)
print(list1)
