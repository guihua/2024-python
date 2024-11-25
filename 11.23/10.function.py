# 内置函数, 常用的内置函数有 abs(), max(), min(), len(), sum(), round(), pow(), sorted()

# abs() 求绝对值
a = abs(-100)
print(a)

# 数据类型转换，使用 int(), float(), str(), bool() 等函数进行类型转换
b = int('123')
c = float('12.34')
d = str(100)
e = bool(1)
print(b, c, d, e)

n1 = 255
n2 = 1000

# hex() 函数将一个整数转换成十六进制表示的字符串
print(hex(n1), hex(n2))

# 定义函数
# 定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))