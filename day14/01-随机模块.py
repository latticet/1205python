import random

# random.random()	实数相关	用于生成一个0到1的随机浮点数: [0, 1)
"""
print(random.random())  
"""

# random.uniform(a,b)		生成[a,b]或[b,a]之间的均匀分布随机浮点数。
"""
for i in range(3):
    print(random.uniform(1, 10))
"""

# random.randint(a,b)	整数相关	生成[a,b]的随机整数，要求a < b。
"""
for i in range(3):
    print(random.randint(1, 3))
"""

# random.randrange(a,b,c=1)		生成[a,b)的随机整数，第三个参数可以指定步长。
"""
print(random.randrange(1, 5, 2))
"""

# random.choice(seq)	序列相关	从序列中随机选择一个元素，若序列为空，则抛出异常。
# 序列：str，list，tuple
"""
print(random.choice(['python', 'mysql', 'linux']))
"""

# random.shuffle(list)		打乱原序列，原序列必须可写。
"""
list1 = ['python', 'mysql', 'linux']
random.shuffle(list1)
print(list1)
"""

# random.sample(seq,k)		从序列中随机选择k个元素返回，原序列不变。
"""
list1 = ['python', 'mysql', 'linux', 'git']
print(random.sample(list1, 2))
"""

# random.seed(n=none)	初始化	初始化随机熵池。
# 种子数

random.seed(2)
print(random.randint(1, 10))

random.seed(3)
print(random.choice(['python', 'mysql', 'linux']))
