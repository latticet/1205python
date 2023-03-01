from datetime import datetime
import time

# TODO 类方法  返回datetime的实例
# datetime.today()	当前时间，localtime。
"""
obj = datetime.today()
print(obj)
print(type(obj))
"""

# datetime.now()	当前的时间。
"""
print(datetime.now())
"""

# datetime.utcnow()	当前格林时间。
"""
print(datetime.utcnow())
"""

# datetime.fromtimestamp()	将时间戳的转换为时间。
"""
times = time.time()
print(datetime.fromtimestamp(times))
"""

# * datetime.strptime(str,fmt)	按照fmt的格式解析字符串生成datetime。
# 将字符串时间转化为 datetime对象时间
"""
str_datetime = '2023-10-01 10:10:10'
obj_datetime = datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
print(obj_datetime)
print(type(obj_datetime))
"""

# TODO 对象方法
# datetime_obj.date()	返回一个date对象。
"""
obj_datetime = datetime.now()
obj_date = obj_datetime.date()
print(obj_date)
print(type(obj_date))
"""

# datetime_obj.time()	返回time对象。
"""
obj_datetime = datetime.now()
obj_time = obj_datetime.time()
print(obj_time)
print(type(obj_time))
"""

# * datetime_obj.strftime(fmt)	按照fmt的格式生成字符串。
# 将datetime时间转化为字符串时间
obj_datetime = datetime.now()
str_datetime = obj_datetime.strftime('%Y/%m/%d %H:%M:%S')
print(str_datetime)
print(type(str_datetime))
