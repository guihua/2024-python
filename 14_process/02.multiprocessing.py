# multiprocessing 模块，提供了一个Process类来代表一个进程对象
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数
    # 创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start() # 启动子进程，父进程会等待子进程结束后再继续往下运行
    p.join() # 等待子进程结束后再继续往下运行
    print('Child process end.')