from fastapi import FastAPI
from enum import Enum

# 创建一个 FastAPI 应用，并将其赋值给变量 app，这个应用将作为我们的 Web 应用程序的入口点，并处理所有的 HTTP 请求
app = FastAPI()

# 定义一个枚举类，用于定义图书类型
# 继承自 Enum 类，Enum 类是 Python 标准库中的一个枚举类，用于定义枚举类型
class BookType(str, Enum):
    Novel = 'novel'             # 小说
    Economics = 'Economics'     # 经济类

# 定义一个路由，处理 GET 请求到路径 "/books/{book_type}"
# app.get("/books/{book_type}") 是一个装饰器，它告诉 FastAPI 应用程序，当有一个 GET 请求到路径 "/books/{book_type}" 时，应该调用 book_info 函数来处理这个请求
@app.get('/books/{book_type}')
# book_info 函数是一个异步函数，它将被调用来处理这个 GET 请求
# book_type: BookType 是一个类型提示，它告诉 FastAPI 应用程序，book_type 参数应该是一个 BookType 枚举类型
# page: int = 0 是一个默认值，它告诉 FastAPI 应用程序，如果没有传入 page 参数，应该使用 0 作为默认值
# limit: int = 10 是一个默认值，它告诉 FastAPI 应用程序，如果没有传入 limit 参数，应该使用 10 作为默认值
def book_info(book_type: BookType, page: int = 0, limit: int = 10):
    return {'msg': f'返回{book_type} 类型图书， 第{page}页， 每页{limit}条数据'}