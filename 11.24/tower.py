# 定义一个名为 hanoi 的函数，用于解决汉诺塔问题
# 参数 n 表示盘子的数量，a、b、c 表示三个柱子
def hanoi(n, a, b, c):
    # 如果只有一个盘子
    if n == 1:
        # 直接将盘子从柱子 a 移动到柱子 c
        print(a, '-->', c)
    else:
        # 先将 n-1 个盘子从柱子 a 借助柱子 c 移动到柱子 b
        hanoi(n-1, a, c, b)
        # 再将最底下的一个盘子从柱子 a 移动到柱子 c
        hanoi(1, a, b, c)
        # 最后将 n-1 个盘子从柱子 b 借助柱子 a 移动到柱子 c
        hanoi(n-1, b, a, c)
