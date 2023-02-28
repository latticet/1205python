# TODO 查询
# 下标(索引)
# 元素在列表的中的位置序号：下标
# 从左至右从0开始，从右至左从-1开始
# 通过下标找到对应的元素
# 中括号方式
# 语法：list[index]
list1 = ['python', 'mysql', 'linux', 'mysql']
print(list1[1])
print(list1[-2])
print('--' * 20)

# 查询数据第一次出现的索引
# list.index(元素)
# 判断元素是否在列表中,如果不存在抛出错误
print(list1.index('mysql'))
print(list1.index('linux'))
# list1.index('git')  # 不在抛出错误
print('--' * 20)

#
#
#
#
#
#
#
# len(容器)
# list
list1 = ['python', 'mysql', 'linux', 'mysql']
print(len(list1))
# str
print(len('hello'))

# TODO 修改
# 语法：list1[index] = value
# 说明：修改指定索引的数据
list1 = ['python', 'mysql', 'linux', 'mysql']
list1[1] = 'redis'
print(list1)
