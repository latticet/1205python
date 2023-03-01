import copy


# 封装一个类，实现对字典的浅拷贝，深拷贝，和普通的赋值操作。
class CopyDict:
    def __init__(self, dict1):
        self.dict1 = dict1

    def copy(self):
        """浅拷贝"""
        return copy.copy(self.dict1)

    def deepcopy(self):
        """深拷贝"""
        return copy.deepcopy(self.dict1)

    def assignment(self):
        """普通赋值"""
        dict2 = self.dict1
        return dict2


if __name__ == '__main__':
    # 创建对象
    dict0 = {'name': 'hello', 'info': {'name': 'hello', 'age': 18}}
    copy_dict = CopyDict(dict0)
    print(id(dict0), id(dict0['info']))

    # 浅拷贝
    dict1 = copy_dict.copy()
    print(id(dict1), id(dict1['info']))   # 0 1

    # 深拷贝
    dict2 = copy_dict.deepcopy()
    print(id(dict2), id(dict2['info']))   # 0 0

    # 赋值操作
    dict3 = copy_dict.assignment()
    print(id(dict3), id(dict3['info']))   # 1 1
