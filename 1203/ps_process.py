# psutil 包括 5 个模块，分别是：
# 1. cpu 模块，用于获取 CPU 信息
# 2. memory 模块，用于获取内存信息
# 3. disk 模块，用于获取磁盘信息
# 4. net 模块，用于获取网络信息
# 5. process 模块，用于获取进程信息
import psutil

# 所有进程ID
# 它的值是一个 list，它的元素分别是：pid
pids = psutil.pids()
print(pids)

# 5. process 模块，用于获取进程信息
# 进程信息，它的值是一个 tuple，它的元素分别是：pid、name、exe、cmdline、create_time、cpu_times、cpu_percent、memory_percent、memory_info、io_counters、connections、threads、num_threads、username
# pid 表示进程 id
# name 表示进程名
# exe 表示进程的可执行文件路径
# cmdline 表示进程的命令行参数
# create_time 表示进程创建时间
# cpu_times 表示进程的 CPU 时间
# cpu_percent 表示进程的 CPU 使用率
# memory_percent 表示进程的内存使用率
# memory_info 表示进程的内存信息
# io_counters 表示进程的 IO 信息
# connections 表示进程的连接信息
# threads 表示进程的线程信息
# num_threads 表示进程的线程数
# username 表示进程的用户名
process = psutil.Process(3570)
print(process)