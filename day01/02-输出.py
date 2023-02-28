# 输出
# 说明：将内容输出到终端
# 语法：print(content1 [, content2, ..., sep=' ', end='\n'])
# 输出的内容：参数

# TODO 一次输出一个内容
print('今天天气挺好，适合好好学习！')
print(123)

# TODO 同时输出多个内容, 多个之间用逗号隔开
print('mysql', 'linux', 'shell', 'git', end='===')

# TODO 结尾符参数, end='\n'
# 指定了print的结尾符
print(123, end='---')
print(456, end='|||')
print(789)
print('==' * 20)

# TODO 分隔符参数，sep=' '
# 指定了多个输出内容之间的分割符号
print('apple', 'orange', 'banana', sep='|', end='1')
print('apple', 'orange', 'banana', sep='-', end='2')
print('apple', 'orange', 'banana', sep='+')
