from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # render_template 函数从 templates 文件夹中读取模板并渲染
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    # 这里使用了 Jinja2 模板引擎，它会自动将 username 变量替换为用户输入的内容
    # 这里的 message 变量是一个占位符，它会被替换为一个字符串
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)

    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()