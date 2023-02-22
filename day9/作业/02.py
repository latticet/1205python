"""
读取一个py文件，显示除了以井号(#)开头的行以外的所有行
"""

# 打开文件
f = open('../../day8/11-案例3-任何类型任何大小文件复制-升级版.py', encoding='utf8')

# 操作文件-r
# TODO 第一种：一次性读取所有行
"""
content_list = f.readlines()
for content_line in content_list:
    if not content_line.startswith('#'):
        print(content_line, end='')
"""

# TODO 第二种：一次读取一行
while True:
    content_line = f.readline()
    if not content_line:
        break

    if not content_line.startswith('#'):
        print(content_line, end='')
  
# 关闭文件
f.close()
