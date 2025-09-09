import uvicorn
from fastapi import FastAPI

# 创建一个 FastAPI 应用，并将其赋值给变量 app
# 这个应用将作为我们的 Web 应用程序的入口点，并处理所有的 HTTP 请求
app = FastAPI()

# 定义一个路由，处理 GET 请求到根路径 "/"
# app.get("/") 是一个装饰器，它告诉 FastAPI 应用程序，当有一个 GET 请求到根路径时，应该调用 index 函数来处理这个请求
@app.get("/")
# index 函数是一个异步函数，它将被调用来处理这个 GET 请求
# 这个函数将返回一个 JSON 对象，其中包含 "msg" 键和值为 "Hello World"
def index():
    """
    第一个API接口 \n
    :return:
    """
    return {"msg": "Hello World"}

# 主函数，用于启动 Web 服务器
# uvicorn.run() 函数用于启动 Web 服务器
# uvicorn.run("main:app") 表示启动 main.py 文件中的 app 变量，即 FastAPI 应用
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")