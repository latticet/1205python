try:
    # 打开文件-只读
    f = open('resource/demo1.txt', 'r', encoding='utf8')
except FileNotFoundError as e:
    f = open('resource/demo1.txt', 'w', encoding='utf8')
    f.write('123465')
else:
    # 操作文件-读取内容
    print(f.read())
finally:
    f.close()
