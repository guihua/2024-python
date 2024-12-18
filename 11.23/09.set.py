# set 集合, 无序的集合， 没有重复的元素, 可以看成数学意义上的无序和无重复元素的集合, 是一组 key 的集合， 不存储 value
# 可以看成是只有 key 没有 value 的 dict, 由于 key 不能重复， 所以，在 set 中，没有重复的 key
# 创建一个 set, 可以使用 set() 方法创建 set， 也可以使用 {} 方法创建 set
s1 = {1, 2, 3}
print(s1)

s2 = set([1, 2, 3]);
print(s2)

# 重复元素在 set 中自动被过滤
s3 = {1, 1, 2, 2, 3, 3}
print(s3)

# 添加元素, 使用 add() 方法添加元素， 可以重复添加，但不会有效果
s3.add(4)

# 删除元素, 使用 remove() 方法删除元素， 可以重复删除，但不会有效果
s3.remove(4)

# 两个 set 可以进行交集、并集、差集、对称差集运算， 交集运算使用 & 运算符， 并集运算使用 | 运算符， 差集运算使用 - 运算符， 对称差集运算使用 ^ 运算符
s4 = {1, 2, 3}
s5 = {2, 3, 4}

# 交集
print('交集', s4 & s5)
# 并集
print('并集', s4 | s5)
# 差集
print('差集', s4 - s5)
# 对称差集
print('对称差集', s4 ^ s5)