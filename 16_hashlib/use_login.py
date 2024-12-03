import hashlib, random

# 定义一个函数，传入用户和密码，返回经过salt加密后的密码
def get_md5(user, pws):
    md5 = hashlib.md5()
    # 先将密码和salt拼接起来，再进行md5加密
    md5.update((pws + user.salt).encode('utf-8'))
    return md5.hexdigest()

# User 类
class User(object):
    # 初始化函数，传入用户名、密码
    def __init__(self, username, password):
        self.username = username
        # salt是一个随机字符串，包含数字和字母，长度为20
        # chr()函数传入一个数字，返回对应的字符
        # randint()函数生成一个指定范围内的整数，包含最小值，但不包括最大值
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        # 计算经过salt加密后的密码，赋值给password属性
        self.password = get_md5(self, password)

# 模拟数据库，存储用户信息，键为用户名，值为User对象
# 密码经过salt加密后，只有用户自己知道自己的salt，其他人无法通过salt反推明文密码
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(user, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')