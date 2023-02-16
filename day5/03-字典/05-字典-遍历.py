# TODO 遍历key
dict1 = {'name': 'good', 'age': 19}
# print(dict1.keys())
# 第一种
for key in dict1.keys():
    print(key)
print('--' * 20)
# 第二种
for key in dict1:
    print(key)
print('==' * 20)

# TODO 遍历value
for value in dict1.values():
    print(value)
print('==' * 20)

# TODO 遍历key和value
# dict1.items()  # [(key, value), (key, value), ...]
# key, value = ('name', 'good')
for key, value in dict1.items():  # [('name', 'good'), ('age', 19)]
    print(key, value)
