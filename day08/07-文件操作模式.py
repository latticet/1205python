# r(read):只读
# w(write):覆盖写
# a(append):追加写
# b(bytes):二进制模式，不能单独使用，必须配合r、w、a使用
# +(extension):扩展模式。不能单独使用，必须配合r、w、a使用。r+:读写模式。w+:读写。a+:读写。
# +扩展模式会遵循主模式的特点

# 打开文件
f = open('resource/demo4.txt', mode='w+', encoding='utf8')

# 操作文件
# 写入内容
f.write('你好python')

# TODO 光标移动
# f.seek([int]) 用于移动文件读取指针到指定位置。
f.seek(3)

# 读取内容
print(f.read())

# 关闭文件
f.close()
