import tornado
import tornado.ioloop
from tornado.web import RequestHandler
from tornado.web import URLSpec

class HelloHandler(RequestHandler):
    # 初始化方法，用于初始化请求处理类，例如初始化数据库连接等
    def initialize(self, db):
        print('initialize')
        self.db = db
        #  self.finish('over')  这里不可以调用finish

    # 准备方法，用于准备请求处理类
    def prepare(self):
        print('prepare')
        self.finish('over')

    # get方法，用于处理GET请求
    def get(self):
        self.write(f'{self.db} ok')

# 定义一个路由列表，用于存储请求处理类
# 路由列表是一个列表，列表中的每个元素是一个元组，元组的第一个元素是请求路径，第二个元素是请求处理类
# URLSpec是一个元组，元组的第一个元素是请求路径，第二个元素是请求处理类，第三个元素是请求处理类的参数
url_handlers = [
    URLSpec(r'/hello', HelloHandler, {'db': 'mysql'})
]

# 创建一个应用对象，用于存储请求处理类
app = tornado.web.Application(url_handlers)
# 创建一个HTTP服务器对象，用于监听端口
http_server = tornado.httpserver.HTTPServer(app)
# 监听端口
http_server.listen(8990)
# 启动服务器
http_server.start()
# 启动IOLoop，开始监听请求
tornado.ioloop.IOLoop.instance().start()