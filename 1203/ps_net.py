# psutil 包括 5 个模块，分别是：
# 1. cpu 模块，用于获取 CPU 信息
# 2. memory 模块，用于获取内存信息
# 3. disk 模块，用于获取磁盘信息
# 4. net 模块，用于获取网络信息
# 5. process 模块，用于获取进程信息
import psutil

# 4. net 模块，用于获取网络信息
# 网络信息，它的值是一个 tuple，它的元素分别是：bytes_sent、bytes_recv、packets_sent、packets_recv、errin、errout、dropin、dropout
# bytes_sent 表示发送的字节数
# bytes_recv 表示接收的字节数
# packets_sent 表示发送的数据包数
# packets_recv 表示接收的数据包数
# errin 表示接收的错误数
# errout 表示发送的错误数
# dropin 表示接收的丢弃数
# dropout 表示发送的丢弃数
net = psutil.net_io_counters()
print(net)

# 网络接口信息，它的值是一个 dict，它的键是接口名，它的值是一个 list，它的元素分别是：snicaddr、netmask、broadcast、ptp
# snicaddr 表示接口地址
# netmask 表示接口掩码
# broadcast 表示接口广播地址
# ptp 表示接口 PTP 配置
net_if_addrs = psutil.net_if_addrs()
print(net_if_addrs)

# 网络接口统计信息，它的值是一个 dict，它的键是接口名，它的值是一个 list，它的元素分别是：isup、duplex、speed、mtu
# isup 表示接口是否启动
# duplex 表示接口的双工模式
# speed 表示接口的速度
# mtu 表示接口的最大传输单元
net_if_stats = psutil.net_if_stats()
print(net_if_stats)

# 网络连接信息，它的值是一个 list，它的元素分别是：fd、family、type、laddr、raddr、status、pid
# fd 表示连接的文件描述符
# family 表示连接的地址族
# type 表示连接的类型
# laddr 表示连接的本地地址
# raddr 表示连接的远程地址
# status 表示连接的状态
# pid 表示连接的进程 id
# net_connections = psutil.net_connections()
# print(net_connections)
# PermissionError: [Errno 1] Operation not permitted (originated from proc_pidinfo(PROC_PIDLISTFDS) 1/2)