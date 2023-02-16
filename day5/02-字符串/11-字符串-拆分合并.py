# TODO * string.split(str[, num]) 利用str将字符串拆分为列表
# num:拆分最大次数
print('python,mysql,linux'.split(','))
print('python, mysql, linux'.split(' '))
print('python,mysql,linux'.split('y'))

print('python,mysql,linux'.split(',', 1))
print('==' * 20)

# TODO * string.join(容器) 利用string将容器中的元素拼接成一个新的字符串
list1 = ['python', 'mysql', 'linux']
print('-'.join(list1))
print(','.join(list1))
print('='.join(list1))
print(' '.join(list1))
t1 = ('a', 'b', 'c')
print('-'.join(t1))
str1 = 'abc'
print('-'.join(str1))

# TODO string.partition(str) 利用str将string分割成3个元素的元组, 从左找str
print('abc'.partition('b'))
print('aaaaaaabbbbccccccc'.partition('bbbb'))

# TODO string.rpartition(str) 利用str将string分割成3个元素的元组 从右找str
print('aaaaaaabbbbccccccc'.rpartition('b'))

# TODO string.splitlines() 利用换行将string分割成列表
print('hello\nworld'.splitlines())