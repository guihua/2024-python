# Description: 使用redis实现多线程下的阅读次数自增
# Thread 类用于创建一个线程，参数 target 是线程执行的函数，args 是函数的参数
from threading import Thread
from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

def add_view():
    for i in range(10):
        # id 为 1 的阅读次数加 1
        # incr 命令的参数是键，返回值是键的值加 1，键的值必须是整数
        r.incr('view::1')

lst = []
for i in range(10):
    # 创建一个线程，执行 add_view 函数
    # Thread 类的 start 方法用于启动线程，join 方法用于等待线程结束
    t = Thread(target=add_view)
    lst.append(t)

for t in lst:
    # 启动线程，执行 add_view 函数
    # start 方法的返回值是 None
    t.start()

for t in lst:
    # 等待线程结束，再执行后续代码
    # join 方法的返回值是 None
    t.join()

# 打印 id 为 1 的阅读次数
print(r.get('view::1'))