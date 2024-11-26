# a 是整数
a = 123
print('a = ', a)

# a 变为字符串
a = 'ABC'
print('a = ', a)

# 由于 Python 是动态语言，根据变量本身类型自动转换
x = 10
x = x + 2
print('x = ', x)

b = a # 变量 b 指向变量 a 指向的字符串对象，字符串对象不可变，所以变量 a 改变后，变量 b 不会改变
a = 'XYZ'
print(b, a)