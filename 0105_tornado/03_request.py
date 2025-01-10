import tornado.ioloop
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.options import options, define

# 定义一个端口，默认监听8000端口
define('port', default=8000, help='监听端口')

# 定义一个请求处理类，继承自RequestHandler，用于处理请求
# 一个请求处理类可以处理多个请求，例如GET请求、POST请求等
class HelloHandler(RequestHandler):
    # get方法用于处理GET请求
    def get(self):
        # request是一个Request对象，用于存储请求的信息
        # 我们可以通过Request对象获取请求的信息，例如请求的方法、请求的路径、请求的参数、请求的首部等
        # Request对象是一个不可变对象，我们不能修改Request对象的属性
        # Request对象的属性有：
        #   method：请求的方法，例如GET、POST、PUT、DELETE等
        #   path：请求的路径，例如/index.html
        #   query：请求的参数，例如?name=admin&password=password
        #   headers：请求的首部，例如Host、User-Agent、Accept等
        #   body：请求的正文，例如POST请求的正文
        #   remote_ip：请求的IP地址
        #   files：请求的文件，例如上传文件
        #   cookies：请求的cookie，例如Cookie: name=admin; password=password
        #   arguments：请求的参数，例如name=admin&password=password
        #   host：请求的主机名
        #   protocol：请求的协议，例如http、https
        #   uri：请求的URI，例如/index.html?name=admin&password=password
        #   version：请求的版本，例如HTTP/1.1
        #   request_time：请求的时间，例如2020-01-01 00:00:00
        print(self.request.headers)             # 字典形式存储的headers信息
        print(self.request.headers['host'])     # 获取某一个首部
        print(self.request.path)                # 请求的path
        self.write('ok')

# 主函数，用于启动服务器
if __name__ == '__main__':
    # 解析命令行参数
    options.parse_command_line()
    # 定义一个路由列表，用于存储请求处理类
    handlers_routes = [
        (r'/', HelloHandler)
    ]
    # 创建一个应用对象，用于存储请求处理类
    app = Application(handlers=handlers_routes)
    # 创建一个HTTP服务器对象，用于监听端口
    http_server = HTTPServer(app)
    # 监听端口
    http_server.listen(options.port)
    # 启动服务器
    tornado.ioloop.IOLoop.current().start()