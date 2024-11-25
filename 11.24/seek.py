# 使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        return (L[0], L[0])
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            elif i > max:
                max = i
        return (min, max)