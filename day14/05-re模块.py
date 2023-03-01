import re

# TODO re.search(pattern, string[,flags])
# 说明：在字符串中查找正则匹配的字符串，第一个匹配到的对象或者None
re_obj = re.search('hello', 'hello world hello python')
# re_obj.group()  # 获取匹配到的字符串
print(re_obj.group())

re_obj = re.search('hello1', 'hello world hello python')
print(re_obj)


# TODO re.findall(pattern, string[,flags])
# 说明：列出字符串中所有的匹配项， 返回列表。
match_list = re.findall('hello', 'hello world hello python')
print(match_list)

match_list = re.findall('hello1', 'hello world hello python')
print(match_list)