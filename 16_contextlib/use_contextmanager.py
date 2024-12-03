from contextlib import contextmanager

# Query 类
class Query(object):
    # __init__ 方法，用于初始化 Query 对象，参数为 name
    def __init__(self, name):
        self.name = name

    # query 方法，打印查询信息
    def query(self):
        print('Query info about %s...' % self.name)

# create_query 函数，用于创建 Query 对象
# 参数为 name，返回 Query 对象
# 使用 contextmanager 装饰，使函数成为上下文管理器
# 该函数的作用是在进入上下文时执行 __enter__ 方法，退出上下文时执行 __exit__ 方法
# __enter__ 方法打印 "Begin"，返回 Query 对象
# __exit__ 方法打印 "End"
# contextmanager 装饰后，可以使用 with 语句来使用该函数
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

# 使用 with 语句来使用 create_query 函数，调用 Query 对象的 query 方法
with create_query('Bob') as q:
    q.query()