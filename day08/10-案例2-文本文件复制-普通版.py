import os

complete_filename = input('要复制的文件名：')  # demo1.txt

# 打开原文件
old_file = open(f'resource/{complete_filename}', 'r', encoding='utf8')

# 文件操作
content = old_file.read()

# 关闭文件
old_file.close()

# 构造新文件名
old_filename, extension = os.path.splitext(complete_filename)  # (demo1, .txt)
new_complete_filename = old_filename + '-副本' + extension
print(new_complete_filename)

# 打开新文件-w
new_file = open(f'resource/{new_complete_filename}', 'w', encoding='utf8')
# 写入文件
new_file.write(content)
# 关闭文件
new_file.close()
