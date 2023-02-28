# 标识符
# 说明：python中所有的名字就是标识符。比如变量名

# TODO 标识符命名规则
# 必须要遵循，否则语法报错
"""
1. 由字母数字下划线组成，不能以数字开头
2. 标识符区分大小写
3. 不能使用python的关键字
"""
# python的关键字
# 说明：python官方用的单词，就是python关键字
# 查看python中的所有关键字
import keyword

print(keyword.kwlist)

# TODO 标识符命名风格
# 不是必须遵循
"""
1. 大驼峰命名（类名）：标识符中的所有单词首字母大写
    UserInfo  FirstName  NameError
2. 小驼峰命名：标识符中第一个单词首字母小写，后面所有单词首字母大写
    userInfo  firstName  nameError
3. 下划线命名(变量名，函数名，方法名)：单词之间用下划线分割
    user_info  first_name  name_error
"""