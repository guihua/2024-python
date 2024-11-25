# 定义一个名为 fact 的函数，用于计算 n 的阶乘
def fact(n):
    # 如果 n 等于 1，则阶乘为 1
    if n==1:
        return 1
    # 否则，n 的阶乘等于 n 乘以 (n-1) 的阶乘
    return n * fact(n - 1)