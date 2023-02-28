# 只能在循环体中使用
# TODO break
# 说明：退出整个循环，终止循环
# 需求：循环1-5，当等于3时退出整个循环
"""
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
"""

# TODO continue
# 说明：退出本次循环，下次循环继续
# 需求：循环1-5，跳过3
i = 1
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
