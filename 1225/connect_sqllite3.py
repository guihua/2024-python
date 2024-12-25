# 导入 sqlite3 模块，用于操作 SQLite 数据库，它是 Python 标准库的一部分
import sqlite3

# 创建连接，连接到数据库文件 students.db
conn = sqlite3.connect('./1225/students.db')

# 创建游标对象
c = conn.cursor()
# 删除表，如果表不存在则不执行
c.execute("DROP TABLE IF EXISTS students")
# 建表语句
c.execute("""CREATE TABLE students (
            name TEXT,
            age INTEGER,
            height REAL
    )""")
# 执行
conn.commit()

# 插入数据
# 插入一条数据
c.execute("INSERT INTO students VALUES ('mark', 20, 1.9)")
# 提交更改
conn.commit()

all_students = [
    ('john', 21, 1.8),
    ('david', 35, 1.7),
    ('michael', 19, 1.83),
]
# 插入多条数据
# executemany() 方法用于执行多条 SQL 语句，参数为 SQL 语句和参数列表
# ? 表示占位符，会被后面的参数列表中的元素替换
c.executemany("INSERT INTO students VALUES (?, ?, ?)", all_students)
# 提交更改
conn.commit()

# 查询数据
c.execute("SELECT * FROM students")
# fetchall() 方法用于获取所有查询结果，返回一个列表
# fetchone() 方法用于获取一条查询结果，返回一个元组
print(c.fetchall())

# 关闭连接
conn.close()