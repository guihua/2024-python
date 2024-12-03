import itertools

# groupby() 把迭代器中相邻的重复元素挑出来放在一起，并返回一个 key 和 group 组成的迭代器
# 注意：groupby() 函数会根据条件判断来截取序列，当条件不满足时，就会停止迭代，所以需要使用 break 语句来退出循环，否则会无限循环
# 注意：groupby() 函数只会对相邻的元素进行分组，而不会对未相邻的元素进行分组，所以需要使用 sorted() 函数对序列进行排序，然后再使用 groupby() 函数进行分组
# 注意：groupby() 函数返回的是一个迭代器，需要使用 list() 函数将其转换为列表，否则只会打印出第一个元素
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 忽略大小写分组
# 将 A a 视为同一组，将 B b 视为同一组，将 C c 视为同一组
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))