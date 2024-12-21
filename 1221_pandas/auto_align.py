from pandas import Series

score_dict_1 = {
    'c++': 99,
    'python': 100,
    'c#': 98,
    'go': 97
}
score_dict_2 = {
    'node.js': 99,
    'python': 100,
    'c#': 98,
    'java': 97
}

# 通过字典创建 Series 对象，索引默认为字典的键，值为字典的值，索引的顺序为字典的键的顺序
# 索引的长度必须和数据的长度一致，否则会报错
ser_1 = Series(score_dict_1)
ser_2 = Series(score_dict_2)

# 将两个 Series 对象相加，返回的是一个新的 Series 对象，索引为两个 Series 对象的索引的并集
# 如果索引相同，则值为两个 Series 对象对应索引的值相加的结果
# 如果索引不同，则值为 NaN
res = ser_1 + ser_2
print(res)