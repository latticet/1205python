"""
类名：DB
方法：
    __init__:  初始化conn， cursor
    read
    write
    __del__: 关闭conn， cursor
"""
import pymysql


class DB:
    def __init__(self, user, password, database, host='localhost', port=3306, charset='utf8',
                 cursor=pymysql.cursors.Cursor):
        """初始化conn， cursor"""
        self.conn = pymysql.connect(host=host, port=port,
                                    user=user, password=password,
                                    database=database, charset=charset)
        self.cursor = self.conn.cursor(cursor=cursor)

    def read(self, sql):
        """读操作"""
        try:
            rows = self.cursor.execute(sql)
        except Exception:
            return 0, ()
        else:
            return rows, self.cursor.fetchall()

    def write(self, sql):
        """写操作"""
        try:
            rows = self.cursor.execute(sql)
        except Exception:
            self.conn.rollback()
            return 0
        else:
            self.conn.commit()
            return rows

    def __del__(self):
        """关闭资源"""
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db = DB(user='root', password='root', database='advanced')
    rows, data = db.read('select * from student1') # (2, ((),(),()))
    print(rows)
    print(data)

    # 写入
    rows = db.write('delete from news where title = "title9"')
    print(rows)
