from typing import Optional,List
from pydantic import BaseModel
from fastapi import FastAPI

# 创建一个 FastAPI 实例，命名为 app，用于创建一个 Web 应用程序，并提供了一组路由和处理函数，用于处理客户端的请求和响应
app = FastAPI()

# 定义一个数据模型 SchoolInfo，继承自 BaseModel
# 用于定义学校的信息，包括学校名称和地址
class SchoolInfo(BaseModel):
    name: str      # 学校名称
    address: str   # 学校地址

# 定义一个数据模型 FamilyInfo，继承自 BaseModel
# 用于定义家庭的信息，包括父亲和母亲的姓名
class FamilyInfo(BaseModel):
    father: str    # 父亲姓名
    mother: str    # 母亲姓名

# 定义一个数据模型 Course，继承自 BaseModel
# 用于定义课程的信息，包括课程名称和分数
class Course(BaseModel):
    name: str       # 课程名称
    score: float    # 分数

# 定义一个数据模型 User，继承自 BaseModel
# 用于定义用户的信息，包括姓名、年龄、住址、家庭信息、学校信息和课程信息
class User(BaseModel):
    name: str       # 姓名
    age: int        # 年龄
    address: Optional[str] = None       # 住址 可选字段
    family: FamilyInfo      # 家庭信息
    school: SchoolInfo      # 学校信息
    course: List[Course]    # 课程信息

# 使用 FastAPI 的 @app.post 装饰器定义了一个 POST 请求的路由，路由的路径为 '/users'
# 当客户端向该路由发送 POST 请求时，FastAPI 会调用 add_user 函数来处理请求
# 在 add_user 函数中，使用 User 类来接收请求体中的 JSON 数据，并将其转换为 User 类的实例
# 然后，将 User 实例转换为 JSON 格式，并作为响应的消息体返回给客户端
@app.post('/users')
def add_user(user: User):
    return user.json()