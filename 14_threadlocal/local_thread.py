import threading

# 创建全局ThreadLocal对象
# 任何函数都可以直接调用它，也可以把它看成全局变量
# 每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理
# 每个Thread对它都可以读写student属性，但互不影响
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student，如果没有绑定student，会返回默认值None
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student，每个Thread都有各自的local_school，互不干扰
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()