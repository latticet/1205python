# timedelta：计算时间的类
# 作用：创建单位的时间的对象 1天 1周
from datetime import timedelta, datetime
# 创建实例 7天
weeks1 = timedelta(weeks=1)

# 获取7天前的时间
obj_datetime = datetime.today()
print(obj_datetime - weeks1)

# 获取7天后的时间
print(obj_datetime + weeks1)

