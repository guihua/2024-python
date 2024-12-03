from urllib import request

# get请求，获取网页内容
# 模拟浏览器访问，返回一个类似file的对象，必须调用close()方法，也可以使用with语句自动调用close()方法
with request.urlopen('https://liaoxuefeng.com/books/python/built-in-modules/datetime/index.html') as f:
    # 读取响应内容，返回bytes类型，需要解码为str类型
    data = f.read()
    # 读取响应状态码和原因短语，返回一个tuple，包含了状态码和原因短语
    print('Status:', f.status, f.reason)
    # 读取响应头信息，返回一个类似dict的对象，包含了响应头的所有信息
    # getheaders()方法返回的是一个list，每个元素是一个tuple，包含了响应头的key和value
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # 使用utf-8编码解码响应内容，返回一个str类型
    print('Data:', data.decode('utf-8'))