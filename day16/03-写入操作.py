# TODO 1.导入pymysql
import pymysql

# TODO 2.创建连接对象
conn = pymysql.connect(user='root', password='root',
                       database='advanced', charset='utf8')

# TODO 3.获取游标对象
cursor = conn.cursor()

try:
    # TODO 4.执行sql语句
    # TODO 5.提交或者回滚
    sql = "INSERT INTO student(stu_no, stu_name, stu_age, class_id) " \
          "VALUES('itsrc-018', '周瑜', 18, 2)"
    rows = cursor.execute(sql)
    print(f'受影响行数：{rows}')
except Exception as e:
    # 回滚
    conn.rollback()
    print(e)
else:
    # 提交
    conn.commit()

# TODO 6.关闭游标对象
cursor.close()

# TODO 7.关闭连接对象
conn.close()
