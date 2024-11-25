from trim import trim

L = list(range(100))

# 取前10个元素
print(L[:10])

# 取后10个元素
print(L[-10:])

# 前11-20个数
print(L[10:20])

# 前10个数，每两个取一个
print(L[:10:2])

# 所有数，每5个取一个
print(L[::5])

# 什么都不写，只写[:]就可以原样复制一个list
print(L[:])

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')