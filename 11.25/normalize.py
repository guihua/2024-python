from functools import reduce

# 函数 normalize 用于将输入的字符串 name 进行规范化处理
def normalize(name):
    # 将字符串的第一个字符转换为大写
    # 使用切片操作 name[0] 获取第一个字符，upper() 方法将其转换为大写
    # 将字符串除第一个字符外的其余部分转换为小写
    # 使用切片操作 name[1:] 获取从第二个字符开始到末尾的部分，lower() 方法将其转换为小写
    return name[0].upper() + name[1:].lower()

# 函数 prod 用于计算列表 L 中元素的乘积
def prod(L):
    # 使用 reduce 函数和 lambda 表达式将列表中的元素依次相乘
    return reduce(lambda x, y: x * y, L)

CHAR_TO_INT = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

CHAR_TO_FLOAT = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, ".": -1}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)

