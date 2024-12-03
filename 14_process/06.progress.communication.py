from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        # 写入数据到队列中
        # 如果队列已满，会一直等待，直到队列中有空闲位置
        q.put(value)
        # 等待随机时间，模拟写入数据的过程
        time.sleep(random.random())

# 读数据进程执行
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        # 从队列中读取数据
        # 如果队列为空，会一直等待，直到队列中有数据，然后读取数据
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # Queue是多进程安全的队列，可以实现进程间通信，可以在多个进程中共享数据
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    # 父进程创建两个子进程，一个负责写入，一个负责读取，用Queue实现进程间通信
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入数据到队列中
    pw.start()
    # 启动子进程pr，从队列中读取数据
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止，用terminate()方法终止
    pr.terminate()