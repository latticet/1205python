"""
语法：
第一种：
try:
    可能发生异常的代码
except (异常类型1， 异常类型2， ...):
    捕获到异常执行的代码块

第二种：
try:
    可能发生异常的代码
except 异常类型1:
    捕获到异常执行的代码块1
except 异常类型2:
    捕获到异常执行的代码块2
"""

# 第一种演示
"""
try:
    num = int(input('数字：'))
    result = num / 0
except (ZeroDivisionError, ValueError):
    print('输入有误')
"""
# 第二种演示

try:
    num = int(input('数字：'))
    result = num / 0
except ZeroDivisionError:
    print('0不能作为除数')
except ValueError:
    print('输入数据有误')
