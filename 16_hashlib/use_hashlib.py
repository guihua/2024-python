import hashlib

# MD5 是一种常用的哈希算法，它可以用于给任意数据一个“签名”
# 注意：MD5 不是加密算法，它是一种摘要算法，它的结果是固定的，而且不可逆的
# 所以，我们可以通过比较两个不同的数据的 MD5 值，来判断这两个数据是否相同
# 所以，我们不能通过 MD5 值，反推原始数据
md5 = hashlib.md5()
# update() 方法可以一次传入任意字节数据，也可以分多次传入
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# hexdigest() 方法返回 16 进制的字符串表示
print(md5.hexdigest())

# SHA1 是一种常用的哈希算法，它的结果是 160 位的字节，通常用一个 40 位的 16 进制字符串表示
# 注意：SHA1 也是一种哈希算法，它的结果是固定的，而且不可逆的
# 所以，我们可以通过比较两个不同的数据的 SHA1 值，来判断这两个数据是否相同
# 所以，我们不能通过 SHA1 值，反推原始数据
# 调用 SHA1 与 MD5 完全类似
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())