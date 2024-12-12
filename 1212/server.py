# 从wsgiref模块导入，导入WSGI服务器的生成函数
# simple_server是一个简单的WSGI服务器
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
# 这里的8000端口可以改为其他的端口，但是需要管理员权限
# 这里的application函数也可以改为其他的函数，比如：
# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
#     return [body.encode('utf-8')]
# 这里的application函数是一个符合WSGI标准的HTTP处理函数，它接收两个参数：
# 1. 一个包含所有HTTP请求信息的dict对象；
# 2. 一个发送HTTP响应的函数。
# 然后，web服务器调用application()函数，将( environ , start_response )两个参数传入，获得HTTP响应内容。
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
# serve_forever()方法，会永久运行，直到服务器遇到错误或者用户中断程序，或者调用httpd.shutdown()方法
httpd.serve_forever()