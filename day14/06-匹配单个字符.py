# 原字符：原生字符
# 元字符: \d
import re

# TODO . 匹配任意1个字符（除了\n）
"""
print(re.search('he.', 'hea'))
print(re.search('he.', 'he-'))
print(re.search('he.', 'he '))
print(re.search('he.', 'he\n'))
"""

# TODO [ ]	匹配[ ]中列举的字符[0-9][a-z][A-Z][\u4e00-\u9fa5]
"""
print(re.search('he[abc]', 'hea'))
print(re.search('he[abc]', 'heb'))
print(re.search('he[abc]', 'hec'))
print(re.search('he[abc]', 'hed'))
print(re.search('he[0-9]', 'he1'))
print(re.search('he[a-z]', 'hef'))
print(re.search('he[\u4e00-\u9fa5]', '规范的三个地方he你好给对方三个地方'))
"""

# TODO TODO \d	匹配数字，即0-9  [0-9]
"""
print(re.search('he\d', 'he1'))
print(re.search('he\d', 'he8'))
"""

# TODO \D	匹配非数字，即不是数字
"""
print(re.search('he\D', 'hea'))
print(re.search('he\D', 'he.'))
print(re.search('he\D', 'he='))
print(re.search('he\D', 'he '))
print(re.search('he\D', 'he8'))
"""

# TODO \s	匹配空白，即 空格，tab键, \n
"""
print(re.search('he\s', 'he '))
print(re.search('he\s', 'he\t'))
print(re.search('he\s', 'he\n'))
print(re.search('he\s', 'he\r'))
print(re.search('he\s', 'he='))
"""

# TODO \S	匹配非空白
"""
print(re.search('he\S', 'he '))
print(re.search('he\S', 'he\t'))
print(re.search('he\S', 'he\n'))
print(re.search('he\S', 'he\r'))
print(re.search('he\S', 'he='))
"""

# TODO \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字 [a-zA-Z0-9_\u4e00-\u9fa5]
"""
print(re.search('he\w', 'hea'))
print(re.search('he\w', 'heD'))
print(re.search('he\w', 'he1'))
print(re.search('he\w', 'he_'))
print(re.search('he\w', 'he你回复'))
print(re.search('he\w', 'he-回复'))
"""

# TODO \W	匹配特殊字符，即非字母、非数字、非汉字、非下划线

# TODO | 匹配|俩边的内容
"""
print(re.search('he|你好', 'hello'))
print(re.search('he|你好', '你好天气不错'))
"""