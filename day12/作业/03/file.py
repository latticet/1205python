"""
文件操作模块有以下功能(写在类里面的函数)：
读取文件内容
写入内容到文件中
复制文件
删除文件
文件改名
"""
import os


class File:
    def read(self, filename):
        """读取文件内容"""
        f = open(filename, 'r', encoding='utf8')
        content = f.read()
        f.close()
        return content

    def write(self, filename, content):
        """写入内容到文件中"""
        f = open(filename, 'w', encoding='utf8')
        f.write(content)
        f.close()
        print('写入成功')

    def copy(self, filename):
        """复制文件"""
        # 构造新文件名
        source_filename, extension = os.path.splitext(filename)
        target_filename_complete = source_filename + '-副本' + extension

        # 打开文件
        source_file = open(filename, 'rb')
        target_file = open(target_filename_complete, 'wb')

        # 循环写入
        while True:
            content = source_file.read(1024)
            if not content:
                break

            target_file.write(content)

        # 关闭文件
        source_file.close()
        target_file.close()

    def remove(self, filename):
        """删除文件"""
        os.remove(filename)
        print('删除成功')

    def rename(self, source_filename, target_filename):
        """文件改名"""
        os.rename(source_filename, target_filename)
        print('修改成功')


# 调用
file = File()
# file.write('demo.txt', '123\n789\nabc\njfkd\ndjfkls')
# print(file.read('demo.txt'))
# file.copy('demo.txt')
# file.remove('demo-副本.txt')

file.rename('demo.txt', 'mydemo.txt')
