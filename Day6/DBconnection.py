import pymysql


class DBconnection:
    def execute_sql_command(self,sql):
        conn = pymysql.Connect(host='127.0.0.1', user='root', password="root",
                 database='pirate', port=3306,
                 charset='utf8')
        try:
            # 获取数据库游标
            cursor = conn.cursor()
            # 执行sql语句
            cursor.execute(sql)
            # 获取执行结果
            row = cursor.fetchall()
            conn.commit()
            return row
        finally:
            # 链接关闭
            conn.close()

if __name__ == '__main__':
    sql = 'select * from hd_user order by id desc;'
    row = DBconnection().execute_sql_command(sql)
    print(row)