import numpy as np

# load() 函数可以从磁盘文件中加载数组，文件默认是以.npy格式保存的
# load()方法的参数包括：文件名，允许 mmap_mode，允许 allow_pickle，允许 fix_imports，允许 encoding
# 1.文件名：表示要加载的文件名
# 2.允许 mmap_mode：表示是否允许内存映射模式
# 3.允许 allow_pickle：表示是否允许加载pickle文件
# 4.允许 fix_imports：表示是否允许修复导入
# 5.允许 encoding：表示是否允许编码
# load() 函数会将数组加载到内存中，返回一个数组对象
array = np.load('./1219_numpy/d1.npy')
print(array)

data = np.load('./1219_numpy/d2.npz')
for key in data.files:
    print(data[key])

data2 = np.load('./1219_numpy/d3.npz')
for key in data.keys():
    print(data[key])
