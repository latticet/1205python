# TODO 1.导入pymysql
import pymysql

# TODO 2.创建连接对象
# 返回数据库连接对象
# host:mysql服务主机，默认是localhost
# port:端口号。默认是3306
# user:mysql账号
# password：mysql密码
# database：要操作的数据库
# charset:客户端和服务端通信的字符集。一般写utf8
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                       database='advanced', charset='utf8')

# TODO 3.获取游标对象
# 作用：执行sql语句，获取结果集
cursor = conn.cursor()

# TODO 4.执行sql语句
# rows:受影响行数
rows = cursor.execute('select * from student')
print(f'受影响行数：{rows}')

# TODO 5.获取结果集
# 说明：游标对象只能获取一次结果集。
# 每次获取一条记录
print(cursor.fetchone())

# 批量获取指定条记录
# size：获取记录数
print(cursor.fetchmany(size=2))

# 一次性获取所有结果集
print(cursor.fetchall())

# TODO 6.关闭游标对象
cursor.close()

# TODO 7.关闭连接对象
conn.close()
