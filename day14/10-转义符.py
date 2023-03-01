# 需求：输入一个文件名,判断是否符合文件名的规则
# xxx.xxx  \w.mp4  .txt .exe .py jpeg  .JPEG  4xx
import re

filename = input('文件名：')
if re.search('^\w{1,32}\.[a-zA-Z]{1,5}\d?$', filename):
    print('ok')
else:
    print('fail')


