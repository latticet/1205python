"""
语法：
try:
    可能发生异常的代码
except 异常类型:
    捕获成功执行的代码
else:
    没有发生异常执行的代码块
"""

try:
    num = int(input('数字：'))
except ValueError:
    print('输入有误')
else:
    print('ok')
