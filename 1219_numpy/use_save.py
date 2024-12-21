import numpy as np

# 生成一个包含3行3列的二维数组，数据类型为int32
array = np.random.randint(9, size=(3, 3), dtype=np.int32)
array2 = np.random.randint(9, size=(3, 3), dtype=np.int32)

# save() 函数可以将数组保存到磁盘文件中，文件默认是以.npy格式保存的
# save() 函数的第一个参数是文件名，它的值为 d1；第二个参数是数组，它的值为 array
# save() 函数会将数组保存到当前目录下，文件名是 d1.npy
np.save('./1219_numpy/d1', array)

# savez() 函数可以将多个数组保存到磁盘文件中，文件默认是以.npz格式保存的
# savez() 函数的第一个参数是文件名，它的值为 d2；第二个参数是数组，它的值为 array
# savez() 函数会将数组保存到当前目录下，文件名是 d2.npz
np.savez('./1219_numpy/d2', array, array2)

# savez_compressed() 函数可以将多个数组保存到磁盘文件中，文件默认是以.npz格式保存的
# savez_compressed() 函数的第一个参数是文件名，它的值为 d3；第二个参数是数组，它的值为 array
np.savez_compressed('./1219_numpy/d3', array, array2)