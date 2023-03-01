import re

# 贪婪模式
print(re.search('h\w{2,5}', 'habc_12'))

# 非贪婪模式
print(re.search('h\w{2,5}?', 'habc_12'))

str1 = '<HTML><head></head><body><h1></h2><li></li></body></html>'
print(re.search('<.+?>', str1))
print(re.findall('<.+?>', str1))

