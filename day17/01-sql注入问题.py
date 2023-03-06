import pymysql

conn = pymysql.connect(user='root', password='root', database='advanced', charset='utf8')
cursor = conn.cursor()

# 根据标题删除新闻
# 接收用户输入的标题
title = input('标题：')  # " or 1 = 1 or "
sql = f'delete from news where title = "{title}"'

# delete from news where title = "" or 1 = 1 or ""

try:
    rows = cursor.execute(sql)
except Exception as e:
    print(e)
    conn.rollback()
    print('删除失败')
else:
    conn.commit()
    print('删除成功')

# 关闭资源
cursor.close()
conn.close()
