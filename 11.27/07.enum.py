# 从 enum 模块中导入 Enum 和 unique 类
from enum import Enum, unique

# 使用 unique 装饰器确保枚举类中的成员值唯一
@unique
class Weekday(Enum):
    """
    定义一个名为 Weekday 的枚举类，用于表示一周的七天。
    每个成员都有一个唯一的整数值。
    """
    # 周日，值为 0
    Sun = 0
    # 周一，值为 1
    Mon = 1
    # 周二，值为 2
    Tue = 2
    # 周三，值为 3
    Wed = 3
    # 周四，值为 4
    Thu = 4
    # 周五，值为 5
    Fri = 5
    # 周六，值为 6
    Sat = 6

# 创建一个 Weekday 枚举类的实例，代表周一
day1 = Weekday.Mon
# 打印 day1 的信息
print("day1 =", day1)

# 打印 Weekday.Tue 的信息
print("Weekday.Tue =", Weekday.Tue)
# 通过键访问 Weekday 枚举类的成员 Tue 并打印
print("Weekday['Tue'] =", Weekday["Tue"])
# 打印 Weekday.Tue 的值
print("Weekday.Tue.value =", Weekday.Tue.value)

# 检查 day1 是否等于 Weekday.Mon 并打印结果
print("day1 == Weekday.Mon?", day1 == Weekday.Mon)
# 检查 day1 是否等于 Weekday.Tue 并打印结果
print("day1 == Weekday.Tue?", day1 == Weekday.Tue)
# 检查 day1 是否等于通过值 1 创建的 Weekday 枚举类成员并打印结果
print("day1 == Weekday(1)?", day1 == Weekday(1))

# 遍历 Weekday 枚举类的成员并打印成员的名称和成员对象
for name, member in Weekday.__members__.items():
    print(name, "=>", member)

# 使用 Enum 类的另一种创建枚举类的方式，定义一个名为 Month 的枚举类，用于表示十二个月
Month = Enum("Month", ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

# 遍历 Month 枚举类的成员并打印成员的名称、成员对象和成员的值
for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)
