# 所有对字符串产生影响的操作，都是返回新的字符串，不会影响原字符串
# TODO string.replace(原字符串， 新字符串[,count] )  将原字符串替换为新字符串
# count:能替换的最大次数
str1 = 'python and mysql or python'
str2 = str1.replace('python', 'java', 1)

print(str1)
print(str2)
