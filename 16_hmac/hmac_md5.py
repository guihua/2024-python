import hmac, random

# HMAC算法：Keyed-Hashing for Message Authentication，它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
# 计算hmac，传入key和消息，返回一个hmac对象
def hmac_md5(key, s):
    # 注意：key和s都是bytes类型，str类型需要使用encode()方法转换
    # 注意：MD5是默认的算法，也可以传入其他算法，例如SHA1，SHA256，SHA512
    # 注意：hexdigest()返回的是十六进制字符串，bytes类型需要使用hexdigest()方法转换，str类型不需要使用hexdigest()方法转换
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

# User 类，包含用户名、key和密码
class User(object):
    # 初始化用户对象，传入用户名和密码，生成key和密码
    def __init__(self, username, password):
        self.username = username
        # 生成随机key，长度为20，包含数字和字母
        # 注意：chr()函数传入一个数字，返回对应的字符
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        # 计算密码，传入key和密码，返回一个hmac对象
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    # 计算密码，传入key和密码，返回一个hmac对象
    return user.password == hmac_md5(user.key, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')