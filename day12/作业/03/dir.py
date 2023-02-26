"""
目录操作模块有以下功能：
创建目录
删除目录（空目录或非空目录）
查找目录中是否存在某个文件
"""
import os
import shutil


class Directory:
    @staticmethod
    def mkdir(name):
        """
        创建目录
        :param name: 目录名
        :return:
        """
        os.mkdir(name)
        print('创建成功')

    @staticmethod
    def rmdir(name):
        shutil.rmtree(name)
        print('删除成功')

    @staticmethod
    def is_file_in_dir(dir_name, file_name):
        resource_list = os.listdir(dir_name)
        return file_name in resource_list


# Directory.mkdir('dir1')
print(Directory.is_file_in_dir('dir1', 'mydemo.txt'))
print(Directory.is_file_in_dir('dir1', 'demo.txt'))

Directory.rmdir('dir1')
