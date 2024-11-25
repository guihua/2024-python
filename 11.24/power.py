# 计算 x 的 n 次方,
# 默认值 n = 2，即计算 x 的平方
def power(x, n = 2):
    s = 1
    # 当 n 大于 0 时，执行循环
    while n > 0:
        n = n - 1
        s = s * x
    return s