# 打开文件
# mode = w(write): 覆盖写。如果文件不存在，新建文件。如果原文件有内容，会覆盖。
f = open('resource/demo2.txt', mode='w', encoding='utf8')

# mode = a(append):追加写。如果文件不存在，新建文件。在原内容后面继续追加内容。
# f = open('resource/demo3.txt', mode='a', encoding='utf8')

# 写入文件
# TODO write(要写入的内容) 一次性写入一个数据
"""
f.write('123')
f.write('456')
"""
# TODO writelines([数据1, 数据2, ...]) 一次性写入多个数据
f.writelines(['123\n', '456\n', '789\n'])

# 关闭文件
f.close()
