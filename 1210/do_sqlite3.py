# SQLite 是一种嵌入式数据库，它的数据库就是一个文件
# SQLite 的特点是轻量级、无服务器、零配置、事务性，支持NULL，支持数据库加密，可移植性好，支持多种编程语言
# SQLite 是一个进程库，包含在标准 Python 发行版中；所以，在任何操作系统下，不需要安装任何东西，直接使用
# 导入 SQLite 驱动
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')
# cursor是用来执行SQL语句的，所以我们要创建一个Cursor对象，通过Cursor对象执行SQL来实现对数据库的操作
# 创建一个Cursor对象
cursor = conn.cursor()
# 新建user表前，先删除user表，以免重复创建
# cursor.execute('drop table user')
# 执行一条SQL语句，创建user表
# 执行SQL语句时，SQL语句需要以元组的形式传入，所以我们要先创建一个元组
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数
cursor.rowcount

# 提交事务，对数据库进行修改，要调用commit()方法
conn.commit()
# 关闭Cursor，释放资源
cursor.close()
# 关闭Connection，释放资源
conn.close()

