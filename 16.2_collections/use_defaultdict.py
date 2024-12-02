from collections import defaultdict

# defaultdict 是一个字典，字典的作用是存储数据，然后可以通过字典的键获取值
# 字典的键可以是任意类型，值可以是任意类型，字典的键可以通过d['key']获取，也可以通过d.get('key')获取
# defaultdict 适用于需要频繁添加和删除数据的场景，例如统计单词的出现次数
dd = defaultdict(lambda: 'N/A')

# key1 存在于dd中，返回key1的值
dd['key1'] = 'abc'
print(dd['key1'])

# key2 不存在于dd中，返回默认值 N/A
print(dd['key2'])