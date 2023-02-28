# TODO 1.打开文件
# 语法：open(文件路径[, mode='r', encoding='utf8'])
# 文件路径：要操作的文件位置，可以是绝对路径也可以是相对路径
# mode：打开模式,默认就是r。r：read，w：write
# encoding:编码格式，一般都写utf8
# 返回：文件操作的资源句柄
# 相对路径
# f = open('resource/demo1.txt', encoding='utf8')
# 绝对路径
f = open(r'E:\20221205软件测试\08.python阶段\1205python\day8\resource\demo1.txt', encoding='utf8')

# TODO 2.操作文件
# 读
content = f.read()
print(content)

# TODO 3.关闭文件
f.close()
