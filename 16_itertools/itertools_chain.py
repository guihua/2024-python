import itertools

# chain() 函数可以把一组迭代对象串联起来，形成一个更大的迭代器
# chain() 函数会把传入的参数作为一个迭代器返回，所以，字符串也是可迭代对象，因此，字符串也可以用 chain() 连接起来，形成一个更大的迭代器
cs = itertools.chain('ABC', 'XYZ')

for c in cs:
    print(c)