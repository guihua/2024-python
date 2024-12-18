import asyncio
import motor.motor_asyncio
import sys

# 解决 macOS 上的 RuntimeError: Event loop is closed 问题
if sys.platform == "darwin":
    # mac 上的事件循环策略是 uvloop，需要使用默认的事件循环策略
    # DefaultEventLoopPolicy 是 mac 上的默认事件循环策略，需要使用 set_event_loop_policy() 设置
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

uri = "mongodb://admin:guihua.pgh@localhost:27017/app"
# AsyncIOMotorClient 异步客户端
# 异步客户端，创建数据库连接
client = motor.motor_asyncio.AsyncIOMotorClient(uri)

# 选择数据库，创建集合
db = client.app
print(db)

async def insert_one():
    data = {'name': '小红', 'age': 14}
    # 插入一条数据，返回一个字典
    result = await db.user.insert_one(data)
    # 新增数据的id
    print(result.inserted_id)

loop = asyncio.get_event_loop()
loop.run_until_complete(insert_one())