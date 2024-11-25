# 杨辉三角
def triangles():
    # 初始化列表 L，第一个元素为 1
    L = [1]
    while True:
        # 生成当前的列表 L
        yield L
        # 生成下一个列表，首尾元素为 1，中间元素为上一个列表相邻元素之和
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
