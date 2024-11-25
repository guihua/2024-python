# 对中文进行编码，需要指定编码，否则，Python 解释器会报错
# s = '包含中文的str'
print('包含中文的str')

# ord() 函数获取字符的整数表示, 中文对应的编码是 Unicode 编码
# chr() 函数把编码转换为对应的字符, 10进制和16进制都可以表示一个字符
a = ord('A')
b = ord('中')
c = chr(66)
d = chr(25991)
print(a, b, c, d)

# f-string 格式化字符串
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

s1 = 72
s2 = 85
s = (s2 - s1) / s1 * 100
print(f'小明成绩提升了 {s:.2f} %')