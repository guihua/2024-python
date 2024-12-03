# pool 进程池
# 批量创建子进程，然后批量等待子进程结束，再继续往下运行
# 进程池的大小为4，所以，最多同时执行4个进程，当一个进程执行完毕后，会自动启动一个新的进程，直到所有进程执行完毕
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # 进程池大小为4，所以，最多同时执行4个进程
    # 当一个进程执行完毕后，会自动启动一个新的进程，直到所有进程执行完毕，再继续往下运行
    p = Pool(4)
    for i in range(5):
        # 批量创建子进程，然后批量等待子进程结束，再继续往下运行
        # 子进程执行的函数为long_time_task，参数为i
        # apply_async()方法会立即返回，不会等待子进程执行完毕，而是继续往下运行
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close() # 调用close()方法之后，就不能继续添加新的Process了
    p.join() # 等待所有子进程执行完毕，再继续往下运行
    print('All subprocesses done.')