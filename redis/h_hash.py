from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

stu_lst = [
    {'小明': 588},
    {'小刚': 606},
    {'小红': 620}
]

for stu in stu_lst:
    for name, score in stu.items():
        # hset 方法向哈希表中添加元素，参数是哈希表的名称和元素，元素是一个字典，键是元素的键，值是元素的值
        # hset 方法返回一个整数，表示添加元素的结果，1表示添加成功，0表示添加失败
        # 元素的键和值可以是任何类型，但是必须是可比较的，例如字符串，整数，浮点数，字典，元组，列表等
        r.hset('stu_score', name, score)

# 获取小明的成绩
# hget 方法从哈希表中获取元素，参数是哈希表的名称和元素的键，返回值是元素的值
score = r.hget('stu_score', '小刚')
print(int(score))