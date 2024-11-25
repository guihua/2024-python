# dict 字典, 无序的集合，使用键-值（key-value）存储，具有极快的查找速度, 适合用于查找，不适合用于插入和删除
# key 是唯一的, 不可变类型，如字符串，整数等，value 可以是任何数据类型
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# value 可以是任何数据类型, 可以是 list, tuple, dict 等
d['Jack'] = 90
print(d)

# value 重新赋值，不会追加到 list 中， 也不会删除原来的值， 只是覆盖原来的值
d['Jack'] = 88
print(d)

# key 不存在会报错, 可以使用 in 判断 key 是否存在, 也可以使用 get() 方法获取 value, key 不存在返回 None
# print(d['Jack1'])
str = d.get('Jack1')
print(str)

# 删除 key, 也可以使用 pop() 方法删除 key, key 不存在会报错
d.pop('Jack')
print(d)