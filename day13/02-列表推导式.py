# 语法： [生成元素的表达式 控制元素生成个数的表达式]

# 需求1：生成1-10的列表
# [1, 2, 3, ..., 10]
"""
list1 = []
for i in range(1, 11):
    list1.append(i)

print(list1)
"""
list1 = [i for i in range(1, 11)]
print(list1)
print('==' * 20)

# 需求2：生成1-10之间每个数的立方
list2 = [i ** 3 for i in range(1, 11)]
print(list2)
print('==' * 20)

# 需求3：生成列表中有10个python
list3 = ['python' + str(i) for i in range(10)]
print(list3)
print('==' * 20)

# 需求4：生成1-10的偶数列表
list4_1 = [i for i in range(2, 11, 2)]
print(list4_1)
print('--' * 20)
list4_2 = [i for i in range(1, 11) if i % 2 == 0]
print(list4_2)
"""
list4_3 = []
for i in range(1, 11):
    if i % 2 == 0:
        list4_3.append(i)
"""

# 需求5：[(1, 1), (1, 2), (2, 1), (2, 2)]
list5 = [(i, j) for i in range(1, 3) for j in range(1, 3)]
print(list5)

# list5_2 = []
# for i in range(1, 3):
#     for j in range(1, 3):
#         list5_2.append((i, j))
