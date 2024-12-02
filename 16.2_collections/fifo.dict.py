from collections import OrderedDict

# 实现一个 FIFO（先进先出）的 dict，当容量超出限制时，先删除最早添加的 Key
class LastUpdatedOrderedDict(OrderedDict):
    # 初始化，传入容量
    def __init__(self, capacity):
        # 调用父类的初始化方法
        super(LastUpdatedOrderedDict, self).__init__()
        # 保存容量
        self._capacity = capacity

    def __setitem__(self, key, value):
        # 如果 key 已经存在，先删除
        containsKey = 1 if key in self else 0

        # 如果容量超出限制，先删除最早添加的 Key
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey: # 存在则删除
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))

        # 调用父类的 setitem 方法
        OrderedDict.__setitem__(self, key, value)