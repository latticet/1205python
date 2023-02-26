# 语法： from 模块名 import 资源名1 [as 别名], 资源名2, ...

from module1 import name, fn1
from module2 import name as m2_name, fn1 as m2_fn1

print(name)
fn1()

print(m2_name)
m2_fn1()
