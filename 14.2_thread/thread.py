import time, threading

def loop():
    # 子线程，是主线程的子线程，是唯一的线程
    # 子线程的名字为LoopThread，可以通过threading.current_thread().name获取，也可以通过threading.current_thread().name获取
    # 子线程的作用是执行loop函数，然后等待loop函数执行完毕后再继续往下运行
    # threading.current_thread().name获取当前线程的名字，然后打印
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

# 主线程，是程序的入口，也是唯一的线程
# 主线程的名字为MainThread，可以通过threading.current_thread().name获取，也可以通过threading.main_thread().name获取
# 主线程的作用是创建其他线程，然后等待其他线程结束后再继续往下运行
print('thread %s is running...' % threading.current_thread().name)

# 创建一个线程，参数为loop函数，名字为LoopThread
# 线程的作用是执行loop函数，然后等待loop函数执行完毕后再继续往下运行
# threading.Thread()方法会立即返回，不会等待线程执行完毕，而是继续往下运行，直到线程执行完毕
t = threading.Thread(target=loop, name='LoopThread')

t.start() # 启动线程，子线程会自动调用loop函数
t.join() # 等待线程执行完毕后再继续往下运行

print('thread %s ended.' % threading.current_thread().name)