# else配合循环
# 说明：else可以和for或者while循环配合使用，使用机制相同
# TODO 语法
# while
"""
while 条件:
    代码块
else:
    代码块
"""
# for
"""
for i in list:
    代码块
else:
    代码块
"""
# TODO 运行机制
# 在循环正常执行完毕后，执行else代码块。
# 如果循环是break终止退出的，那么不会执行else代码块

# TODO 练习
# 循环正常退出
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('else代码块执行')
print('==' * 20)

# 循环break退出
i = 0
while i < 3:
    if i == 1:
        break
    print(i)
    i += 1
else:
    print('else代码块执行')

# 学生查询系统
# 学会姓名列表
names = ['aa', 'bb', 'cc']

# 输入学生姓名
name = input('姓名：')
# 如果找到了输出，学生存在。
# 如果不存在，找不到该学生。

for stu_name in names:
    if name == stu_name:
        print('学生存在')
        break
else:
    print('找不到该学生')



