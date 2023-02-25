"""
语法：
try:
    可能发生异常的代码
except Exception:
    捕获成功执行的代码块
"""

try:
    num = int(input('数字：'))
    result = num / 0
except Exception as e:
    print(e)
