# 高阶函数
def add(f, *args):
    # 使用列表推导式将 args 中的每个元素 arg 作为参数传递给函数 f 进行计算，并将结果存储在列表 s 中
    s = [f(arg) for arg in args]
    return sum(s)

def f(x):
    return x*x
