# 循环
# 说明：程序重复的去执行

# 循环语句
"""
while
for
"""

# TODO 语法
"""
while 条件表达式:  
    代码块（循环体）
"""

# TODO 执行流程
# 判断条件表达式是否成立
# 如果是True，进入循环体执行
# 循环体执行完毕，继续执行条件表达式。
# 如果是True，重复上面执行流程
# 如果是Fase，跳过循环体，继续向下执行

"""
# 死循环
while 1:
    print('hello')
"""

# 设置循环次数
# 变量a输出3次
a = 'BAAAAAAAAAA'
# 计数器
# 计数器初始化
i = 0
while i < 3:
    i += 1  # 计数器累加
    print(a)

print('--' * 20)

"""
i = 1
while i <= 3:
    i += 1  # i = 3
    print(a)
"""