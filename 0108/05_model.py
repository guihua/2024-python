from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

# 创建 FastAPI 应用实例，命名为 app，FastAPI 的实例是 FastAPI 的主要交互方式，也是整个应用程序的入口
# 通过调用 FastAPI 的各种方法和属性，可以定义路由、处理请求、返回响应等
app = FastAPI()

# 定义一个数据模型类 User，继承自 BaseModel
# 数据模型类用于定义请求和响应的数据结构，可以使用 Pydantic 库来进行数据验证和序列化/反序列化
# 在 User 类中，定义了三个属性：name、age 和 address，分别表示用户的姓名、年龄和住址
# 其中，address 属性使用 Optional 类型进行了可选设置，表示该属性可以为空
class User(BaseModel):
    name: str       # 姓名
    age: int        # 年龄
    address: Optional[str] = None       # 住址 可选字段

# 使用 FastAPI 的 @app.post 装饰器定义了一个 POST 请求的路由，路由的路径为 '/users'
# 当客户端向该路由发送 POST 请求时，FastAPI 会调用 add_user 函数来处理请求
# 在 add_user 函数中，使用 User 类来接收请求体中的 JSON 数据，并将其转换为 User 类的实例
# 然后，从 User 实例中获取 name 属性的值，并将其拼接到一个字符串中，作为响应的消息体返回给客户端
@app.post('/users')
def add_user(user: User):
    return {'msg': f'recv user info ,name is {user.name}'}