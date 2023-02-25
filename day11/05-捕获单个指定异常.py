# 捕获单个指定异常
"""
语法：
try:
    可能发生异常的代码
except 异常类型:
    捕获到异常执行的代码块
"""
try:
    result = 1 / 0
except ZeroDivisionError:
    print('除数不能是0')

print('11111')
