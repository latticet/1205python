# TODO string.startswith(str)  判断string是否以str开头
print('hello world'.startswith('hell'))
print('1hello world'.startswith('he'))
print('==' * 20)

# TODO string.endswith(str)  判断string是否以str结束
print('hello world'.endswith('ld'))
print('1hello world'.endswith('ldd'))
print('==' * 20)

# TODO string.find(str)  判断str在string字符串中的位置（下标）。不在返回-1。从左查。
print('python'.find('p'))
print('python'.find('on'))
print('python'.find('ff'))  # -1
print('hello'.find('l'))
print('==' * 20)

# TODO string.rfind(str)  判断str在string字符串中的位置（下标）。不在返回-1。从右查。
print('hello'.rfind('l'))
print('hello'.rfind('f'))
print('==' * 20)

# TODO string.index(str) 判断str在string字符串中的位置（下标）.不在抛出错误。从左查.
print('hello'.index('l'))
# print('hello'.index('d'))
print('==' * 20)

# TODO string.rindex(str) 判断str在string字符串中的位置（下标）.不在抛出错误。从右查.
print('hello'.rindex('l'))
# print('hello'.rindex('d'))
print('==' * 20)
