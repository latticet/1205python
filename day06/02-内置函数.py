# TODO len() 获取容器长度
print(len('hello'))
print(len([1, 2]))
print(len(('a', 'b')))
print(len({'name': 'aa', 'age': 18}))
print(len({1, 2}))

print('==' * 20)
# TODO del 删除通用语法
num = 100
del num

list1 = [1, 2]
del list1[0]

dict1 = {'name': 'aa', 'age': 18}
del dict1['name']

# str1 = 'abc'
# del str1[0]

# TODO max()  获取容器中的最大值
print(max([1, 2, 3]))


# TODO min()  获取容器中的最小值
print(min(('a', 'b', 'd')))
