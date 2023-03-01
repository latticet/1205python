import re

# TODO * 匹配前一个字符出现0次或者无限次 {0,}
"""
print(re.search('he*', 'h'))
print(re.search('he*', 'he'))
print(re.search('he*', 'hee'))
print(re.search('he*', 'heee'))
print(re.search('h\d*', 'h18493478397'))
print(re.search('h\w*', 'h243sfdI你好_'))
"""

# TODO +	匹配前一个字符出现1次或者无限次 {1,}
"""
print(re.search('h\d+', 'h1'))
print(re.search('h\d+', 'h1234324'))
print(re.search('h\d+', 'ha'))
print(re.search('h\d+', 'h'))
"""

# TODO ?	匹配前一个字符出现1次或者0次 {0,1}
"""
print(re.search('h\w?', 'ha'))
print(re.search('h\w?', 'h'))
print(re.search('h\w?', 'h1'))
print(re.search('h\w?', 'h_'))
print(re.search('h\w?', 'h-'))
"""

# TODO {m}	匹配前一个字符出现m次
"""
print(re.search('h\d{2}', 'h1'))
print(re.search('h\d{2}', 'h23'))
print(re.search('h\d{2}', 'h0943fdks;ladfd'))
"""

# TODO {m,n}	匹配前一个字符出现从m到n次
# 注意：逗号后面不能写空格
"""
print(re.search('h\w{2,5}', 'hab'))
print(re.search('h\w{2,5}', 'habc'))
print(re.search('h\w{2,5}', 'hab_你好'))
print(re.search('h\w{2,5}', 'hab78_你好'))
"""

# {m,}	匹配前一个字符至少出现m次
print(re.search('h\w{2,}', 'hab'))
print(re.search('h\w{2,}', 'habc'))
print(re.search('h\w{2,}', 'hab_你好'))
print(re.search('h\w{2,}', 'hab78_你好'))
print(re.search('h\w{2,}', 'hab78_你好范德萨发的jkljfdklj894859'))