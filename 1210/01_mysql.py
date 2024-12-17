# 导入MySQL驱动
import mysql.connector

# 连接 MySQL 服务器
# connect() 方法需要传入数据库名、用户名、密码等信息
# 注意把 password 设为你的 root 口令
conn = mysql.connector.connect(user='root', password='guihua.pgh', database='test')
# 用cursor()方法创建一个Cursor对象，通过Cursor对象执行SQL语句
cursor = conn.cursor()
# 为避免创建表异常，创建之前先删除表
cursor.execute('drop table if exists user')
# 创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
# 提交事务
conn.commit()
cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
# fetchall() 方法可以取出结果集，结果集是一个 list，每个元素都是一个 tuple
# 可以通过 rowcount 获取结果条数
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection
cursor.close()
conn.close()