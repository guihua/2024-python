import os

# 进程，是操作系统中执行的一个程序，每个进程都有自己的地址空间，内存，数据栈等
# 一个程序至少有一个进程，一个进程至少有一个线程
# getpid()获取进程id
# getppid()获取父进程id
print('Process (%s) start...' % os.getpid())

# Only works on Unix/Linux/Mac:
# fork() 调用一次，返回两次，因为操作系统自动把当前进程（父进程）复制了一份（子进程），然后，分别在父进程和子进程内返回
pid = os.fork()
# 子进程永远返回0，而父进程返回子进程的ID
# 一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID
if pid == 0:
    # 子进程返回0
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    # 父进程返回子进程id
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))