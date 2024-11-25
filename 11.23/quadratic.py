import math

# 计算一元二次方程 ax^2 + bx + c = 0 的根
# 使用求根公式 x = (-b ± √(b^2 - 4ac)) / 2a
def quadratic(a, b, c):
    # 检查 a 是否为 0，如果为 0 则方程不是一元二次方程
    if a == 0:
        raise ValueError("a 不能为 0，否则方程不是一元二次方程")
    # 计算判别式
    discriminant = b ** 2 - 4 * a * c

    # 计算第一个根
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    # 计算第二个根
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    # 返回两个根
    return x1, x2
