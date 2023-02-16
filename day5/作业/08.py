"""
假设有一个列表
names = [[“张飞”,”刘备”,”关羽”],[“曹操”,”典韦”,”司马懿”]],
如何将names这个列表通过代码 转变得到如下列表
li=[“张飞”,”刘备”,”关羽”,“曹操”,”典韦”,”司马懿”]
"""

names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]

# 准备空列表，用来加入name
result = []

# 遍历列表中的所有元素
"""
for list_name in names:
    for name in list_name:
        result.append(name)

print(result)
"""
"""
for list_name in names:
    result.extend(list_name)

print(result)
"""

names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]
a_list = names[0]
a_list.extend(names[1])
print(a_list)
