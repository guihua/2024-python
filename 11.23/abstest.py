# 定义一个函数, 求绝对值
def my_abs(x):
    # 数据类型检查, 可以使用 isinstance() 函数判断一个变量是不是字符串, 整数等类型
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x