# asyncio 异步操作 mongodb
import asyncio
# motor 异步操作 mongodb
# 安装 pip install motor
import motor.motor_asyncio

# mongodb 数据库连接
# 用户名:密码@主机:端口/数据库
uri = "mongodb://admin:guihua.pgh@localhost:27017/app"
# AsyncIOMotorClient 异步客户端，创建数据库连接
client = motor.motor_asyncio.AsyncIOMotorClient(uri)

# 选择数据库
db = client.app
print(db)

# do_find_one 查找一条数据，返回一个字典
async def do_find_one():
    # 异步操作，需要使用 async/await
    document = await db.user.find_one({})
    print(document)

# get_event_loop() 获取事件循环，run_until_complete() 运行事件循环
# 运行事件循环，直到完成
loop = asyncio.get_event_loop()
loop.run_until_complete(do_find_one())