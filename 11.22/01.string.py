# \ 是 Python 中的转义字符
print('I\'m \"OK\"!')

# \n 表示换行
print('I\'m learning\nPython.')

# \t 表示制表符
print('\\\t\\')

# Python 还允许用 r'' 表示 '' 内部的字符串默认不转义
print(r'\\\t\\')
# 对比 r 在内与在外的区别
print('r\\\t\\')

# 多行字符串
# 用 '''...''' 的格式表示多行内容
print('''line1
... line2
... line3''')

# 多行字符串 '''...''' 还可以在前面加上 r 使用，就可以把多行内容当作普通字符串，不转义
print(r'''hello,\n
world''')