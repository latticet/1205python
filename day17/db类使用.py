from db import DB
import pymysql


db = DB(user='root', password='root', database='advanced', cursor=pymysql.cursors.Cursor)
print(db.read('select * from student'))
