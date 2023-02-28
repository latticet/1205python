"""
开发敏感词语过滤程序，提示用户输入内容，
如果用户输入的内容中包含特殊的字符：
如 "python"等，将内容替换为 *
"""
# 敏感词库
words = ['python', 'mysql', 'linux','天气']

# 接收用户输入
msg = input('用户输入：')

# msg = '你好python今天天气不错，适合好好学习mysql'
# msg = '你好*今天天气不错，适合好好学习mysql'

for word in words:
    if word in msg:
        msg = msg.replace(word, '*' * len(word))
print(msg)