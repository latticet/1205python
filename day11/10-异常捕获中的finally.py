"""
语法：
# 异常的完整格式
try:
    可能发生异常的代码
except 异常类型:
    捕获异常执行的代码
except 异常类型:
    捕获异常执行的代码
else:
    没有异常的时候执行的代码
finally:
    无论是否异常都要执行的代码
"""

try:
    num = int(input('num:'))
except NameError:
    print('标识符未定义')
except ValueError as e:
    print(e)
else:
    print('ok')
finally:
    print('finally')
