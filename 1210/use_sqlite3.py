import os, sqlite3

# 文件路径
# 注意要使用os.path.join()来拼接路径，这样可以在不同的操作系统上正常工作
# 注意，os.path.dirname(__file__)可以获取当前文件所在的目录，因此，我们可以直接使用__file__变量，而不需要传入当前目录的路径
# 注意，os.path.dirname()返回的是目录路径，因此，我们需要使用os.path.join()来拼接目录路径和文件名
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
# 判断文件是否存在，如果存在则删除
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
# cursor.execute('drop table user')
# execute()方法执行一条SQL语句，然后返回结果
# execute()方法执行SELECT语句时，返回的是一个Cursor对象
# execute()方法执行INSERT、UPDATE、DELETE语句时，需要传入一个tuple，返回的是受影响的行数
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
conn.commit()
cursor.close()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # 执行SQL语句，注意SQL语句后面的?占位符，然后，按照位置传入参数
    # 参数需要是一个tuple，所以我们要先创建一个tuple
    cursor.execute('select name from user where score between? and? order by score', (low, high))
    # 获得查询结果集，返回一个list
    # 注意，fetchall()返回的是一个list，list中的每个元素都是一个tuple，tuple的元素就是数据库记录的字段
    # 所以，我们需要把list中的每个tuple转换成一个list，然后，把list中的所有list组合成一个list，最后返回这个list
    values = cursor.fetchall()
    print(values)
    # 关闭Cursor和Connection
    cursor.close()
    conn.close()

    return [x[0] for x in values]

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')