# 三元运算符：三目运算符
# 三元运算符表达式
# 语法： 条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
# 其他语言：   条件 ? 条件成立执行的表达式 : 条件不成立执行的表达式




a = 2
b = 10

if a > b:
    c = a
else:
    c = b

print(c)

c = a if a > b else b

print(c)
