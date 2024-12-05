# psutil 包括 5 个模块，分别是：
# 1. cpu 模块，用于获取 CPU 信息
# 2. memory 模块，用于获取内存信息
# 3. disk 模块，用于获取磁盘信息
# 4. net 模块，用于获取网络信息
# 5. process 模块，用于获取进程信息
import psutil

# 2. memory 模块，用于获取内存信息
# 内存信息，它的值是一个 tuple，它的元素分别是：total、available、percent、used、free、active、inactive、buffers、cached、shared、slab、wired
# total 表示总内存
# available 表示可用内存
# percent 表示内存使用率
# used 表示已使用内存
# free 表示空闲内存
# active 表示正在使用中的内存
# inactive 表示未使用中的内存
# buffers 表示缓存
# cached 表示缓存
# shared 表示共享内存
# slab 表示 slab 内存
# wired 表示 wired 内存
memory = psutil.virtual_memory()
print(memory)