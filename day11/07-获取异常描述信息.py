"""
语法：
try:
    可能发生异常的代码
except 异常类型 as 变量:
    变量里面就是异常描述信息
    捕获到异常执行的代码块

try:
    可能发生异常的代码
except (异常类型1， 异常类型2， ...) as e:
    捕获到异常执行的代码块

try:
    可能发生异常的代码
except 异常类型1 as e:
    捕获到异常执行的代码块1
except 异常类型2 as e:
    捕获到异常执行的代码块2
"""

try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(e)
