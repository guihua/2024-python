import itertools

natuals = itertools.count(1)
# 无限序列，但是只取前 50 个，因为 takewhile() 函数会根据条件判断来截取序列
# 注意：takewhile() 函数会根据条件判断来截取序列，当条件不满足时，就会停止迭代，所以需要使用 break 语句来退出循环，否则会无限循环
# lambda x: x <= 50 是一个匿名函数，它的作用是判断 x 是否小于等于 50，如果是，就返回 True，否则返回 False
ns = itertools.takewhile(lambda x: x <= 50, natuals)
# 将 ns 转换为列表
print(list(ns))