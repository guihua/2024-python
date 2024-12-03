import hashlib

# MD5 是最常见的摘要算法，速度很快，生成结果是固定的 128 字节，通常用一个 32 位的 16 进制字符串表示
# 计算 MD5 值
# 通常情况下，用户的口令都是以明文保存的，这样会非常不安全
# 为了避免这种情况，我们可以使用 MD5 算法对用户的口令进行加密，然后存储在数据库中
# 当用户登录时，我们首先计算用户输入的口令的 MD5 值，然后与数据库中的 MD5 值进行比较
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def login(user, password):
    md5_password = calc_md5(password)

    if(db[user] == md5_password):
        return True;
    else:
        return False;

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')