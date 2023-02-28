# 默认参数
# 说明：就是形参有默认值，可以不用传入实参
# 定义
def stu_info(name, age, class_name='1205'):
    print(name, age, class_name)


# 调用
stu_info('刘梦秋', 18)
stu_info('陈红', 19)
stu_info('罗燕', 19)

stu_info('hello', 20, '1010')
