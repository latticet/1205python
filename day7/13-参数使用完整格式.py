# 必填参数，位置不定长，默认参数，关键字不定长

def fn(a, b, *args, m=100, **kwargs):
    print(a, b)
    print(args)
    print(m)
    print(kwargs)


fn(1, 2, 100, 200)
print('==' * 20)

fn(1, 2, 100, 200, x='x', y='y')
print('==' * 20)

fn(1, 2, 100, 200, m=1000, x='x', y='y')
print('==' * 20)

print(1, 2, 3, ' ')