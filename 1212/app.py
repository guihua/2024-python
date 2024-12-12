# Flask 是一个使用 Python 编写的轻量级 Web 应用框架。其 WSGI 工具箱采用 Werkzeug，模板引擎则使用 Jinja2。Flask 使用 BSD 授权。
# 安装 Flask：
# pip install flask
from flask import Flask
# request 是 Flask 提供的一个模块，从请求中获取用户数据
# 从 flask 包中导入 request 模块
from flask import request

# Flask 实例
# Flask 实例是一个 WSGI 应用，它接收 HTTP 请求并返回 HTTP 响应
# __name__ 是当前模块的名称，Flask 会根据这个名称寻找模板和静态文件的位置
# 这里的 __name__ 是一个特殊变量，它表示当前模块的名称
app = Flask(__name__)

# 使用 route() 装饰器来告诉 Flask 什么样的 URL 能触发我们的函数
# 这里的 / 表示根目录
# 这里的 methods 参数是一个 list，默认情况下，一个路由只回应 GET 请求
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

# 这里的 /signin 表示 /signin 这个 URL
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
        <p><input name="username"></p>
        <p><input name="password" type="password"></p>
        <p><button type="submit">Sign In</button></p>
        </form>'''

# 这里的 /signin 表示 /signin 这个 URL
# post 方法用来获取表单数据
@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容
    # 使用request.form['']获取表单的内容
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

# main 函数，启动 Flask 实例
if __name__ == '__main__':
    app.run()