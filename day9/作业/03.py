"""
python编写一个聊天记录保存功能，不断获取用户输入信息，保存到record.log文件
"""
while True:
    msg = input('信息：')

    f = open('record.log', 'a', encoding='utf8')
    f.write(f'{msg}\n')
    f.close()

    if msg == 'quit':
        break