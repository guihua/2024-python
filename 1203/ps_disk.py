# psutil 包括 5 个模块，分别是：
# 1. cpu 模块，用于获取 CPU 信息
# 2. memory 模块，用于获取内存信息
# 3. disk 模块，用于获取磁盘信息
# 4. net 模块，用于获取网络信息
# 5. process 模块，用于获取进程信息
import psutil

# 3. disk 模块，用于获取磁盘信息
# 磁盘信息，它的值是一个 tuple，它的元素分别是：total、used、free、percent、mountpoint
# total 表示总磁盘空间
# used 表示已使用磁盘空间
# free 表示空闲磁盘空间
# percent 表示磁盘使用率
# mountpoint 表示磁盘挂载点
disk = psutil.disk_usage('/')
print(disk)

# 磁盘分区信息，它的值是一个 list，它的元素分别是：device、mountpoint、fstype、opts
# device 表示设备名
# mountpoint 表示挂载点
# fstype 表示文件系统类型
# opts 表示挂载选项
disk_partitions = psutil.disk_partitions()
print(disk_partitions)

# 磁盘 IO 信息，它的值是一个 tuple，它的元素分别是：read_count、write_count、read_bytes、write_bytes、read_time、write_time、read_merged_count、write_merged_count
# read_count 表示读取次数
# write_count 表示写入次数
# read_bytes 表示读取字节数
# write_bytes 表示写入字节数
# read_time 表示读取时间
# write_time 表示写入时间
# read_merged_count 表示读取合并次数
# write_merged_count 表示写入合并次数
disk_io_counters = psutil.disk_io_counters()
print(disk_io_counters)