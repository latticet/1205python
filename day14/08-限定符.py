import re

# TODO  ^ 限定开始（匹配开始）
"""
print(re.search('^he\w', 'heafdsfkl'))
print(re.search('^he\w', 'he1fdsfkl'))
print(re.search('^he\w', '1he1fdsfkl'))
"""

# TODO  $ 限定结尾（匹配结尾）
"""
print(re.search('he\w$', 'heafdsfkl'))
print(re.search('he\w$', 'fdsfdhe1'))
print(re.search('he\w$', '1he_'))
"""

# 同时限定开始和结尾
"""
print(re.search('^he\w$', 'heafdsfkl'))
print(re.search('^he\w$', 'fdsfdhe1'))
print(re.search('^he\w$', 'he_'))
"""

phone = input('手机号：')
if re.search('^1[3-9]\d{9}$', phone):
    print('ok')
else:
    print('fail')
