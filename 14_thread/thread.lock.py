import threading

# 定义一个全局变量balance，初始值为0，用于模拟银行存款和取款
balance = 0
# 定义一个锁，用于保证线程安全，防止多个线程同时对balance进行操作，导致数据不一致
# 保证线程安全的方法是加锁，当一个线程获得锁后，其他线程就不能获得锁，直到该线程释放锁后，其他线程才可以获得锁
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0
    global balance
    # 先对balance进行自增操作，然后再对balance进行自减操作
    balance = balance + n
    balance = balance - n

# 两个线程同时对balance进行操作，一个自增5，一个自减5，结果应该为0
def run_thread(n):
    for i in range(10000000):
        lock.acquire() # 获得锁，如果锁被占用，则等待锁释放后再继续往下运行
        try:
            change_it(n)
        finally:
            lock.release() # 释放锁，其他线程可以获得锁，继续往下运行

# 两个线程同时执行
# 一个线程自增5，一个线程自减5，结果应该为0
t1 = threading.Thread(target=run_thread, args=(5,))
# 一个线程自增8，一个线程自减8，结果应该为0
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)