import numpy as np

# savetxt()函数用于将数组写入文本文件，参数是文件名和数组，数组可以是一维数组或二维数组
# savetxt()函数的参数：
# 1.fname: 文件名
# 2.X: 要写入的数组
# 3.fmt: 写入文件时使用的格式
# 4.delimiter: 分隔符
# 5.newline: 换行符
# 6.header: 表头
# 7.footer: 表尾
# 8.comments: 注释符号

# 生成一个维度是(3, 3) 的数组，元素是0到8之间的随机整数，数据类型是int32
array = np.random.randint(9, size=(3, 3), dtype=np.int32)
# 写入文件
np.savetxt('./1219_numpy/data.txt', array)

# genfromtxt()函数用于从文本文件中加载数据，参数是文件名和分隔符
# genfromtxt()函数的返回值是一个二维数组，数组的元素是文本文件中的数据
# genfromtxt()函数的参数：
# 1.fname: 文件名
# 2.dtype: 数据类型
# 3.comments: 注释符号
# 4.delimiter: 分隔符
# 5.skip_header: 跳过文本文件的前n行
# 6.usecols: 使用的列
# 7.names: 列名
# 8.max_rows: 最大行数
# 9.encoding: 编码方式
# 10.unpack: 解包
# 11.usemask: 使用掩码
# 12.invalid_raise: 无效引发

# 从文件中读取数据，数据类型是int32
array = np.genfromtxt('./1219_numpy/data.txt', dtype=np.int32)
print(array)