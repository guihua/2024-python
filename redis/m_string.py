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
        # 将学生的成绩存储到redis中
        r.set(f"score::{name}", score)

# 获取小明的总成绩
score = r.get('score::小明')
score = int(score)
print(score)

# 批量获取学生考试分数
# mget 方法可以同时获取多个键的值，参数是多个键的名称，返回值是一个列表，列表中的元素是键的值
score_lst = r.mget(['score::小明', 'score::小红'])
print(score_lst)