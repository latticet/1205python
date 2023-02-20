# 打开文件
# b:bytes 二进制
# rb:二进制模式的读
# r：文本模式的读
# wb:二级制模式的写
# w:文本模式的写
# 注意：在使用二进制的时候，要去掉encoding
# 文本模式的读
f = open('resource/demo1.txt', mode='r', encoding='utf8')
# 二进制模式的读
# f = open('resource/demo1.txt', mode='rb')
# 读取文件内容
# TODO read([int])
# 第一种：不写任何参数，一次性读取所有内容
"""
content = f.read()
print(content)
"""
# 第二种：int第一种情况: 如果是文本模式的读, 那么int就是字符个数
"""
content1 = f.read(5)
print(content1)
content2 = f.read(2)
print(content2)
"""

# 第三种：int第二种情况: 如果是二进制模式的读,那么int就是字节数   3个字节1个汉字
"""
word = f.read(6)
print(word)
# 二级制转化为字符串
print(word.decode())
"""

# TODO readline()   一次读取一行
"""
line = f.readline()
print(line, end='')

line = f.readline()
print(line, end='')

line = f.readline()
print(line, end='')
"""

# TODO readlines()  一次性读取所有行，返回列表
line_list = f.readlines()
print(line_list)

# 关闭文件
f.close()
