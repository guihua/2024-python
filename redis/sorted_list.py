from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

# 添加数据
# zadd 方法向有序集合中添加元素，参数是有序集合的名称和元素，元素是一个字典，键是元素的值，值是元素的分数
# zadd 方法返回一个整数，表示添加元素的结果，1表示添加成功，0表示添加失败
# 元素的分数是一个浮点数，分数越小，元素的排名越靠前
# 元素的值可以是任何类型，但是必须是可比较的，例如字符串，整数，浮点数，字典，元组，列表等
r.zadd('sort_list', {'小明': 8733})
r.zadd('sort_list', {'小刚': 4355})
r.zadd('sort_list', {'小红': 5635})
r.zadd('sort_list', {'小丽': 7653})
r.zadd('sort_list', {'小王': 8765})
r.zadd('sort_list', {'小刘': 9876})

# 获取排名前3的元素
def get_top(count):
    # zrevrange 方法返回一个列表，列表中的元素是有序集合中的元素，元素的顺序是从大到小的
    # zrevrange 方法的参数是有序集合的名称和范围，范围是一个元组，元组的第一个元素是起始位置，第二个元素是结束位置
    # zrevrange 方法的返回值是一个列表，列表中的元素是有序集合中的元素，元素的顺序是从大到小的
    top_three = r.zrevrange('sort_list', 0, count, withscores=True)
    for name, score in top_three:
        print(name.decode(), score)

get_top(2)

# 修改数据，重新排名
r.zadd('sort_list', {'小红': 11093})

# 打印**分割线
print("*"*20)
get_top(2)