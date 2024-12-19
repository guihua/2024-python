import time
# arange 函数用于创建数组
from numpy import arange
from timeit import Timer

n_elements = 100000
n_timeits = 10000

# arange 函数创建数组，list 函数创建列表
# arange 函数创建的是 numpy.ndarray 类型，list 函数创建的是 list 类型
# numpy.ndarray 类型的对象支持向量化运算，list 类型的对象不支持向量化运算
x = arange(n_elements)
# range 函数创建的是 range 对象，不支持向量化运算，需要转换为 list 类型
# 向量化运算的效率比循环运算的效率高
y = list(range(n_elements))

# Timer 类用于计算代码执行时间
# Timer 类的构造函数的第一个参数是要执行的代码，第二个参数是要执行的代码的环境
t_numpy = Timer("x.sum()", "from __main__ import x")
t_list = Timer("sum(y)", "from __main__ import y")

t1 = time.time()
# timeit 函数用于计算代码执行时间，第一个参数是要执行的代码，第二个参数是要执行的代码的环境
t_numpy.timeit(n_timeits)
t2 = time.time()
t_list.timeit(n_timeits)
t3 = time.time()

print(f"numpy 执行数组求和{n_timeits}次，耗时{t2-t1}秒")
print(f"list 执行数组求和{n_timeits}次，耗时{t3-t2}秒")