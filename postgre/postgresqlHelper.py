import psycopg2

#连接数据库
def connect_db():
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres",
                                password="j13579", host="10.234.75.59", port="5432")
    except Exception as e:
        print('数据库连接失败！')
    else:
        return conn
    return None

#关闭数据库
def close_db_connection(conn):
    conn.commit()
    conn.close()


if __name__ == '__main__':
    conn = connect_db()
    close_db_connection(conn)