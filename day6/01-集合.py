# TODO 定义
# 第一种[常用]
# 语法：s1 = {item1, item2, item3, ...}
s1 = {1, 'hello', (1, 2), 'hello'}
print(s1, type(s1))
print('==' * 20)

# s2 = {}   # 空字典

# 第二种
# 空集合
s3 = set()
print(s3, type(s3))

# 将其他容器转化为集合
# str，list， tuple，dict
list1 = ['python', 'mysql', 'python']
# 将列表转化为集合
s4 = set(list1)
print(s4)
# 将集合转化为列表
list2 = list(s4)
print(list2)
print('==' * 20)

# TODO 特征
"""
无序
唯一
"""

# TODO 其他
# 可以用for循环遍历
s1 = {1, 'hello', (1, 2), 'hello'}
for item in s1:
    print(item)

# 集合只能存储不可变数据类型
