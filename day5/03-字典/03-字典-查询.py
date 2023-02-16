# TODO 根据key获取值
# 第一种：中括号
# 语法：dict[key]
# 说明：如果key不存在，会抛出错误
dict1 = {'name': 'hello', 'age': 18}
print(dict1['name'])
# print(dict1['addr'])
print('==' * 20)

# 第二种：方法
# 语法：dict.get(key[, None])
# 说明：如果key不存在，返回第二个参数的值，第二个参数默认是None
dict1 = {'name': 'hello', 'age': 18}
print(dict1.get('name'))
print(dict1.get('age'))
print(dict1.get('addr'))
print(dict1.get('addr', '成都'))
print('==' * 20)

# TODO 获取字典中的所有key
# 语法：dict.keys()
dict1 = {'name': 'hello', 'age': 18}
print(dict1.keys())

# TODO 获取字典中的所有value
# 语法：dict.values()
print(dict1.values())

# TODO 获取字典中的所有key和value
# 语法：dict.items()
print(dict1.items())

# len() # 通用：获取容器长度
print(len(dict1))
print('==' * 20)

# TODO in 通用：判断元素是否在容器中
# 语法： item in 容器
# dict
dict1 = {'name': 'hello', 'age': 18}
# 判断'name'是否在字典的key列表中
print('name' in dict1.keys())
print('name' in dict1)

# 判断hello是否在字典的value列表中
print('hello' in dict1.values())
print('==' * 20)

# str
print('a' in 'abc')
# list
print('a' in ['a', '1'])
# tuple
print('hello' in (1, 2, 3))

