# WSGI 处理函数，接受两个参数：
# environ：一个包含所有 HTTP 请求信息的 dict 对象
# start_response：一个发送 HTTP 响应的函数。

# 下面的函数返回的是一个 HTTP 的响应头，一个只有一个元素的 list 对象，我们把 HTTP 的 body 写入 list 中，作为 HTTP 响应的 Body 返回。
def application(environ, start_response):
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]