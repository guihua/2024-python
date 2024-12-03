import hmac

message = b'Hello, world!'
key = b'secret'

# 计算 hmac，传入消息和 key，返回一个 hmac 对象
# 注意：消息是 bytes 类型，str 类型需要使用 encode() 方法转换
# 注意：key 也是 bytes 类型，str 类型需要使用 encode() 方法转换
# 注意：digestmod 参数默认为 MD5，也可以是其他哈希算法，例如 SHA1，SHA256，SHA512
# 注意：hmac 算法针对相同的消息，但是不同的 key ，会产生不同的 hmac，因为 key 是用来签名的
h = hmac.new(key, message, digestmod='MD5')

# hexdigest() 返回的是十六进制字符串
# bytes 类型需要使用 hexdigest() 方法转换，str 类型不需要使用 hexdigest() 方法转换
print(h.hexdigest())