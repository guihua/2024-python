from fastapi import FastAPI

# 创建一个 FastAPI 应用，并将其赋值给变量 app，这个应用将作为我们的 Web 应用程序的入口点，并处理所有的 HTTP 请求
app = FastAPI()

# 定义一个路由
# 动态路由，uid是一个变量，会被作为参数传递给user_info函数
@app.get('/userinfo/{uid}')
def user_info(uid):
    return {'msg': f"recv uid :{uid} type is {str(type(uid))}"}

# 定义一个路由，处理 GET 请求到路径 "/get"
# app.get("/get") 是一个装饰器，它告诉 FastAPI 应用程序，当有一个 GET 请求到路径 "/get" 时，应该调用 get 函数来处理这个请求
@app.get("/get")
def get():
    return {"msg": "recv get request"}

# 定义一个路由，处理 POST 请求到路径 "/post"
# app.post("/post") 是一个装饰器，它告诉 FastAPI 应用程序，当有一个 POST 请求到路径 "/post" 时，应该调用 post 函数来处理这个请求
@app.post("/post")
def post():
    return {"msg": "recv post request"}

# 定义一个路由，处理 GET 请求到路径 "/userinfo/all"
# app.get("/userinfo/all") 是一个装饰器，它告诉 FastAPI 应用程序，当有一个 GET 请求到路径 "/userinfo/all" 时，应该调用 user_info_all 函数来处理这个请求
@app.get('/userinfo/all')
def user_info_all():
    return {'msg': "all user info"}

# 定义一个路由，处理 GET 请求到路径 "/userinfo/{uid}"
# app.get("/userinfo/{uid}") 是一个装饰器，它告诉 FastAPI 应用程序，当有一个 GET 请求到路径 "/userinfo/{uid}" 时，应该调用 user_info 函数来处理这个请求
# uid: int 是一个类型提示，它告诉 FastAPI 应用程序，uid 参数应该是一个整数
@app.get('/userinfo/{uid}')
def user_info(uid: int):
    return {'msg': f"recv uid :{uid} type is {str(type(uid))}"}