# 导入系统模块
import os

# TODO os.rename("文件名","新的文件名") 文件重命名（移动）
"""
os.rename('resource/file1.txt', 'resource/file100.txt')
"""

# TODO os.remove ("文件名") 删除文件
"""
os.remove('resource/file100.txt')
"""

# TODO os.mkdir ("文件夹的名字")  创建文件夹
"""
os.mkdir('resource/dir1')
"""

# TODO os.getcwd() 获取当前路径
"""
print(os.getcwd())
"""

# TODO os.chdir() 切换目录
"""
os.chdir('resource')
print(os.getcwd())
"""

# TODO os.listdir('目录路径')
"""
print(os.listdir())
print(os.listdir('resource'))
"""

# TODO os.rmdir("目录路径")  删除空目录
"""
os.rmdir('resource/dir1')
os.rmdir('resource/dir2')
"""
# 可以删除非空目录
"""
import shutil

shutil.rmtree('resource/dir2')
"""
# TODO  os.path.isdir("目录路径")  判断资源是目录
"""
print(os.path.isdir('resource/dir1'))
print(os.path.isdir('resource/demo1.txt'))
"""

# TODO os.path.isfile("文件路径") 判断资源是文件
"""
print(os.path.isfile('resource/dir1'))
print(os.path.isfile('resource/demo1.txt'))
"""

# TODO os.path.splitext ("文件名") 获取文件的名字和扩展名。返回的元组（name, extension）
file_tuple = os.path.splitext('01-匿名函数-基础.py')
filename, extension = os.path.splitext('01-匿名函数-基础.py')
print(filename)
print(extension)
