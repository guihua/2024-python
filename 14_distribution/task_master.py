import random, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象
# 调用Queue对象的方法时, 实际调用的是网络上的Queue对象，而不是本地的，所以可以实现分布式多进程
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口5000, 设置验证码'abc'
# 这个验证码相当于一个口令，只有知道口令的进程才能操作对应的Queue
# 由于这个QueueManager只从网络上获取Queue，所以，只需要监听5000端口
manager = QueueManager(address=('', 5000), authkey=b'abc')

# 启动Queue，把Queue注册到网络上, 并让所有进程都访问Queue
manager.start()

# 获得通过网络访问的Queue对象，调用Queue对象的方法
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    # 调用put方法把任务放进Queue中，调用put方法时，参数就是任务本身，而不是Queue本身
    task.put(n)

# 从result队列读取结果
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

# 关闭 Queue，关闭管理器
manager.shutdown()
print('master exit.')