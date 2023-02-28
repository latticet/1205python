# TODO 定义
# 第一种[常用]
# 语法：(item1， item2, ...)
tuple1 = ('hello', 'good', 1, True, False, [1, 2])
tuple2 = ()
print(tuple1)
print(tuple2)
print('--' * 20)

# 注意：如果元组中是单个元素，那么元素后必须加逗号
tuple3 = ('hello',)
print(tuple3)

print('--' * 20)

# 第二种
# 语法：tuple()
# 空元组
tuple3 = tuple()
tuple4 = tuple('hello')
print(tuple4)
tuple5 = tuple([1, 2])
print(tuple5)
print('==' * 20)

# TODO 特点
"""
1. 元组中可以存任何数据类型
2. 元组中元素可以重复
3. 元组是有序的
4. 元组是不可以修改的
"""

# TODO 元组操作
tuple1 = ('python', 'mysql', 'linux', 'git', 'shell')
# 下标
print(tuple1[1])
print(tuple1[-4])

# 切片
print(tuple1[:3])

# 修改元组中的元素
tuple1[0] = 'java'
