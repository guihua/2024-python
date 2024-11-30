from datetime import datetime, timedelta, timezone

# 获取当前datetime，并以指定的格式输出
# 格式如：2015-12-21 19:21:54.123000
now = datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)

ts = dt.timestamp() # 把datetime转换为timestamp
print(ts)

# str -> datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime -> str
t = dt.timestamp()
print("timestamp -> datetime:", datetime.fromtimestamp(t))
print("timestamp -> datetime as UTC+0:", datetime.utcfromtimestamp(t))

# datetime -> str
print("strftime:", cday.strftime("%a, %b %d %H:%M"))

# datetime加减
print("current datetime =", cday)
print("current + 10 hours =", cday + timedelta(hours=10))
print("current - 1 day =", cday - timedelta(days=1))
print("current + 2.5 days =", cday + timedelta(days=2, hours=12))

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print("UTC+0:00 now =", utc_dt)
print("UTC+8:00 now =", utc8_dt)