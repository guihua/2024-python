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
    return {"msg": "Hello World"}
