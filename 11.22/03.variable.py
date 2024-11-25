a = 123 # a 是整数
print(a)
a = 'ABC' # a 变为字符串
print(a)

# 由于 Python 是动态语言，根据变量本身类型自动转换
x = 10
x = x + 2
print(x)

b = a
a = 'XYZ'
print(b, a)