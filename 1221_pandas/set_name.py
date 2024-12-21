from pandas import Series

score_dict = {
    'c++': 99,
    'python': 100,
    'c#': 98,
    'go': 97
}
# 创建 Series 对象，索引默认为字典的键，值为字典的值，索引的顺序为字典的键的顺序
ser = Series(score_dict)
# 设置 Series 对象的名称和索引的名称
# 名称可以通过 ser.name 和 ser.index.name 获取，可以通过 ser.name = 'name' 和 ser.index.name = 'name' 设置
ser.name = 'score'
ser.index.name = 'program'
print(ser)