# psutil 包括 5 个模块，分别是：
# 1. cpu 模块，用于获取 CPU 信息
# 2. memory 模块，用于获取内存信息
# 3. disk 模块，用于获取磁盘信息
# 4. net 模块，用于获取网络信息
# 5. process 模块，用于获取进程信息
import psutil

# 1. cpu 模块，用于获取 CPU 信息
# CPU 逻辑数量，12 表示是 12 个核
cpu = psutil.cpu_count()
# physical 表示物理核心，logical 表示逻辑核心，physical 表示 6 个核，logical 表示 12 个核
logical_cpu = psutil.cpu_count(logical=False)
print(cpu, logical_cpu)

# CPU 信息，它的值是一个 tuple，它的元素分别是：user、nice、system、idle、iowait、irq、softirq、steal、guest、guest_nice
# user 表示用户态的 CPU 时间总和
# nice 表示用户态低优先级的 CPU 时间总和
# system 表示内核态的 CPU 时间总和
# idle 表示空闲时间总和
# iowait 表示等待 I/O 的 CPU 时间总和
# irq 表示硬中断的 CPU 时间总和
# softirq 表示软中断的 CPU 时间总和
# steal 表示被其他虚拟机占用的 CPU 时间总和
# guest 表示运行在虚拟机上的 CPU 时间总和
# guest_nice 表示运行在虚拟机上的用户态 CPU 时间总和
cpu_info = psutil.cpu_times()
print(cpu_info)

# 获取 CPU 的使用率，它的值是一个 float，它的单位是百分比
# interval 表示间隔时间
# percpu 表示是否返回每个 CPU 的使用率
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))