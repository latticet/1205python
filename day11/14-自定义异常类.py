# 自定义异常类
"""
class 异常类名(Exception):
    def __str__(self):
        return '异常描述信息'
"""


class LenError(Exception):
    def __str__(self):
        return '长度不合法'


# 抛出自定义异常
"""
语法：
raise 自定义异常类()
"""

# 需求：判断用户输入的账号是否符合规则8-16位长度
# 接收用户输入
username = input('账号：')
if 8 <= len(username) <= 16:
    print('用户名ok')
else:
    try:
        # 抛出异常
        raise LenError()
    except LenError as e:
        print(e)
