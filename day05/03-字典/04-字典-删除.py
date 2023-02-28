# TODO del dict[key] 通用语法
dict1 = {'name': 'hello', 'age': 18}
del dict1['name']
print(dict1)
print('==' * 20)

# TODO dict.pop(key, param)  弹出（删除并返回）key对应的数据
# 说明：如果传入的key不存在，那么返回第二个参数param.不指定第二个参数就报错。
dict1 = {'name': 'hello', 'age': 18}
print(dict1.pop('name', 'good'))
print(dict1)

print(dict1.pop('addr', 'xx'))
print('==' * 20)

# TODO dict.clear() 清空字典
dict1 = {'name': 'hello', 'age': 18}
dict1.clear()
print(dict1)

print('==' * 20)
class_a = [
    {'name': '付艺1', 'age': 18, 'addr': '成都', 'stu_no': 18},
    {'name': '付艺2', 'age': 18, 'addr': '成都', 'stu_no': 18},
    {'name': '付艺3', 'age': 18, 'stu_no': 18}
]

for stu_info in class_a:
    print(stu_info.pop('addr', '成都'))
    print(stu_info)
