# 为什么要学习字典
# list1 = ['x', 'x', 'x']
#
# stu1 = ['付艺', 19, '成都', 18]
# stu2 = ['余丽', 17, '重庆', 20]

# key:value形式的数据结构
# TODO 定义字典
# 第一种[常用]
# dict1 = {key1:value1, key2:value2, keyn:valuen}
dict1 = {'name': '付艺', 'age': 18, 'addr': '成都', 'stu_no': 19}
print(dict1)
print(type(dict1))
dict3 = {}
print(dict3, type(dict3))

# 第二种
# dict2 = dict(key1=value, kye2=value2)
dict2 = dict()
print(dict2)
print(type(dict2))

# TODO 特点
dict1 = {'name': '付艺', 'age': 18, 'addr': '成都', 'stu_no': 18, 'name': 'hello'}
print(dict1)
"""
1. 字典的key是唯一的。
2. 字典的值可以是任何数据类型
3. 字典的key必须是不可变数据类型，一般key就使用字符串
4. 字典是可变数据类型
"""

# 字典配合列表使用
class_a = [
    {'name': '付艺1', 'age': 18, 'stu_no': 18},
    {'name': '付艺2', 'age': 18, 'addr': '成都', 'stu_no': 18},
    {'name': '付艺3', 'age': 18, 'addr': '成都', 'stu_no': 18}
]