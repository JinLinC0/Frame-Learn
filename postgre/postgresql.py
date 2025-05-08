import psycopg2

#连接postgresql数据库
conn = psycopg2.connect(dbname="postgres", user="postgres", password="j13579", host="10.234.75.59", port="5432")
print("Successfully connected!")

#创建cursor来访问数据库
cur = conn.cursor()

#创建表
cur.execute('''create table student1(id serial primary key, name varchar(10),age int,class int);''')
print("table created successfully!")

#插入数据
cur.execute("insert into student1(name,age,class) values('xiaoming',20,3)")
cur.execute("insert into student1(name,age,class) values('xiaohong',21,1)")
cur.execute("insert into student1(name,age,class) values('xiaogang',19,2)")
print("table inserted successfully!")

#查询并打印数据
cur.execute("select * from student1")
rows = cur.fetchall()
print("----------------------------------------------------")
for row in rows:
   print("id=" + str(row[0]) + " name=" + str(row[1]) + " age=" + str(row[2]) + " class=" + str(row[3]))
print("----------------------------------------------------\n")

"""""
# 删除表student1某行的数据
cur.execute("delete from student1 where id=1")
cur.execute("select * from student1")
rows = cur.fetchall()
print("----------------------------------------------------")
for row in rows:
    print('id=' + str(row[0]) + ' name=' + str(row[1]) +' age=' + str(row[2]) + ' class=' + str(row[3]))
print("----------------------------------------------------\n")
"""""

"""""
# 更新数据
cur.execute("update student1 set age=23,class=3 where id=2")
cur.execute("select * from student1")
rows = cur.fetchall()
print("----------------------------------------------------")
for row in rows:
    print('id=' + str(row[0]) + ' name=' + str(row[1]) + ' age=' + str(row[2]) + ' class=' + str(row[3]))
print("----------------------------------------------------\n")
"""""

"""""
#查询表
cur.execute("select * from student1")
rows = cur.fetchall()
print("----------------------------------------------------")
for row in rows:
    print('id=' + str(row[0]) + ' name=' + str(row[1]) +' age=' + str(row[2]) + ' class=' + str(row[3]))
print("----------------------------------------------------\n")
"""""
#删除表
#cur.execute("drop table student")

#提交事务
conn.commit()

#关闭连接
conn.close()
