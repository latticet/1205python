# 列表增删改查排序
# TODO list.insert(索引， 数据)
# 说明：指定索引位置添加数据
# 索引(下标)：
# 每一个元素都有自己的一个序号
# 索引从左至右从0开始，从右至左从-1开始。
list1 = ['python', 'mysql', 'linux', 'shell']
list1.insert(0, 'git')
print(list1)

list1.insert(2, '禅道')
print(list1)

list1.insert(-1, '理论')
print(list1)
print('==' * 20)

# TODO list.append(数据)
# 说明：列表末尾追加数据
list2 = ['python', 'mysql']
list2.append('linux')
print(list2)
print('==' * 20)

# TODO list.extend(容器)
# 说明：将容器中的元素依次追加到列表末尾
# 容器：list，str

list3 = ['python', 'mysql']
list3.extend('linux')
print(list3)
list3.extend(['shell', 'git'])
print(list3)
