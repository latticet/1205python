import os

# 打开原文件
source_complete_filename = input('要复制的文件名：')
source_file = open(f'resource/{source_complete_filename}', 'rb')
# 打开目标文件
# 构造目标文件名
source_filename, extension = os.path.splitext(source_complete_filename)
target_complete_filename = source_filename + '-副本' + extension
target_file = open(f'resource/{target_complete_filename}', 'wb')

# 读取原文件内容-1024kb
# 将读到的内容写入目标文件
while True:
    content = source_file.read(1024)
    """
    if content:
        target_file.write(content)
    else:
        break
    """
    if not content:
        break
    target_file.write(content)

# 关闭2个文件
source_file.close()
target_file.close()
