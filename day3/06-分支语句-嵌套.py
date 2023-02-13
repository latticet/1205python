# 语法
"""
if 条件表达式:
    if 条件表达式:
        代码块
"""
# 代码块：代码块里面可以写任何代码

if 1 == 1:
    if 2 == 2:
        print('ok')

print('==' * 20)

"""
需求:
坐公交, 有票就可以上车坐公交, 有座,就可以坐下
"""
"""
# 接收数据
is_bus = input('是否上公交【Y|N】:')

# 根据条件输出内容
if is_bus == 'Y':
    is_seat = input('是否有座位【Y|N】')
    if is_seat == 'Y':
        print('有座位')
    else:
        print('没有座位')
else:
    print('没有上车')
"""

"""
# 注意：接收到'False' 字符串转化为bool类型是True
# 接收数据
is_bus = bool(input('是否上公交:'))

# 根据条件输出内容
if is_bus:
    is_seat = bool(input('是否有座位:'))
    if is_seat:
        print('有座位')
    else:
        print('没有座位')
else:
    print('没有上车')
"""