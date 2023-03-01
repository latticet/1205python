# TODO re.I  Ignore 使匹配对大小写不敏感，也就是不区分大小写的模式
import re

print(re.search('hello', 'Hello'))
print(re.search('hello', 'Hello', re.I))
print('==' * 20)

# TODO re.S  space  使 .这个通配符能够匹配包括换行在内的所有字符，针对多行匹配
print(re.search('hello.world', 'hello\nworld'))
print(re.search('hello.world', 'hello\nworld', re.S))
