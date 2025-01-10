# IOLoop 是一个事件循环对象，用于监听请求，处理请求，并返回响应
import tornado.ioloop
# RequestHandler 是一个请求处理类，用于处理请求，并返回响应；我们可以通过继承RequestHandler，并重写get、post等方法，来处理请求
# Application 是一个应用对象，用于管理请求处理类，包括注册请求处理类、启动服务器等
from tornado.web import RequestHandler, Application
# HTTPServer 是一个http服务器对象，用于监听端口，接收请求，并将请求转发给应用对象
from tornado.httpserver import HTTPServer
from tornado.options import options, define

# 定义监听端口，默认监听8000端口
# 命令行启动：python 01_app.py --port=8000
# define('name', default=None, help=None, type=None, multiple=False, callback=None)
define('port', default=8000, help='监听端口')

# 定义一个请求处理类，继承自RequestHandler
# RequestHandler 是一个请求处理类，用于处理请求，并返回响应
# 我们可以通过继承RequestHandler，并重写get、post等方法，来处理请求
class HelloHandler(RequestHandler):
    # 重写get方法，处理get请求
    def get(self):
        self.write('hello world')

# 定义一个主函数，用于启动服务器
if __name__ == '__main__':
    # 解析命令行参数，并将参数赋值给options对象
    options.parse_command_line()
    # 定义一个路由列表，将请求路径和请求处理类绑定到一起
    # 路由列表是一个列表，列表中的每个元素是一个元组，元组的第一个元素是请求路径，第二个元素是请求处理类
    handlers_routes = [
        (r'/', HelloHandler)
    ]
    # 创建一个应用对象，将请求处理类注册到应用对象中
    # Application是一个应用对象，用于管理请求处理类，包括注册请求处理类、启动服务器等
    app = Application(handlers=handlers_routes)
    # 创建一个http服务器对象，将应用对象注册到http服务器对象中
    # HTTPServer是一个http服务器对象，用于监听端口，接收请求，并将请求转发给应用对象
    http_server = HTTPServer(app)
    # 启动服务器，监听指定端口
    http_server.listen(options.port)
    # 启动IOLoop，开始监听请求
    # IOLoop是一个事件循环对象，用于监听请求，处理请求，并返回响应，它是一个单例对象，我们可以通过IOLoop.current()方法来获取IOLoop对象
    # IOLoop.current().start()方法会启动IOLoop，开始监听请求，处理请求，并返回响应
    tornado.ioloop.IOLoop.current().start()