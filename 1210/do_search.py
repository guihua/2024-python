import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句，注意SQL语句后面的?占位符，然后，按照位置传入参数
# 参数需要是一个元组，所以我们要先创建一个元组
cursor.execute('select * from user where id=?', ('1',))
# 获得查询结果集，返回一个list
# 注意，调用fetchall()时，游标会移动到下一条记录，所以，再次调用fetchall()时，就没有结果返回了，必须再次调用cursor.execute()执行查询语句
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()