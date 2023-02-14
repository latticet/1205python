# str tuple list 都可以使用切片
# 索引
# 语法：list[index]
"""
list1 = ['python', 'mysql', 'linux', 'git', 'shell']
print(list1[0])
print(list1[-3])
"""
# 切片
# 说明：利用索引批量获取列表中的元素,切片返回的还是原数据类型。对元数据不造成影响
# 语法：list[start:end:step]
# start:开始下标，默认是0
# end:结束下标，不包括结束下标
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