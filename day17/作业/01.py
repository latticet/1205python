# a. 一次性添加5条记录
# b. 根据用户输入的标题删除记录
import pymysql
from datetime import datetime


class News:
    def __init__(self):
        self.conn = pymysql.connect(user='root', password='root', database='advanced', charset='utf8')
        self.cursor = self.conn.cursor()

    def add(self):
        """一次性添加5条记录"""
        for i in range(1, 6):
            # 接收用户输入
            """
            title = input('标题：')
            author = input('作者：')
            content = input('内容：')
            post_time = datetime.now()
            clicks = int(input('点击：'))
            """
            title = f'title{str(i)}'
            author = f'author{str(i)}'
            content = f'content{str(i)}'
            post_time = datetime.now()
            clicks = i

            # 写入数据库
            # 执行sql语句
            sql = f"INSERT INTO news(title, author, content, post_time, clicks)" \
                  f" VALUES('{title}', '{author}', '{content}', '{post_time}', {clicks})"
            print(sql)

            try:
                rows = self.cursor.execute(sql)
            except Exception as e:
                print('添加失败')
                print(f'失败原因：{e}')
                self.conn.rollback()
                break
        else:
            print('添加成功')
            self.conn.commit()

    def del_news_by_title(self):
        """根据用户输入的标题删除记录"""
        # 接收用户输入的标题
        title = input('标题：')

        # 查看标题是否存在
        sql = f'select * from news where title = "{title}"'
        rows = self.cursor.execute(sql)
        if not rows:
            print('要删除的标题不存在')
            return

        # 删除标题对应的记录
        sql = f'delete from news where title = "{title}"'
        try:
            rows = self.cursor.execute(sql)
        except Exception:
            print('删除失败')
            self.conn.rollback()
        else:
            if rows:
                print('删除成功')
            else:
                print('删除失败')
            self.conn.commit()

    def __del__(self):
        # 关闭资源
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    news = News()
    # news.add()
    news.del_news_by_title()
