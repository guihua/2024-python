from collections import OrderedDict

# 普通的dict的Key是无序的
# 注意Key的顺序是按照插入的顺序排列的,不是Key本身排序
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的

# OrderedDict的Key是有序的，可以实现一个FIFO（先进先出）的dict
# 当容量超出限制时，先删除最早添加的Key
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict的Key是有序的