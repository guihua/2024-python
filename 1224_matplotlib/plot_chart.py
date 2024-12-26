# matplotlib 是一个 Python 的 2D 绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形，它可以用于 Python 脚本，Python 和 IPython 会话，Jupyter 笔记本，Web 应用程序服务器和四个图形用户界面工具包。
# 安装 matplotlib：
# pip install matplotlib
# matplotlib 使用的是一套名为 rcsetup 的配置系统，它允许用户自定义各种属性，例如字体、线宽、颜色、背景等。
# matplotlib 可以绘制折线图，柱状图，散点图，饼图，直方图，箱线图，热力图，气泡图，3D图等
import matplotlib
from matplotlib import pyplot as plt

# 设置中文字体
# rcParams 是一个字典，它包含了所有的 rc 参数，我们可以通过它来设置字体
matplotlib.rcParams['font.family'] = 'PingFang'

# 定义一个列表，包含了每个季度的销售额
data = [{'年份': 2016, '收入': 14.5},
        {'年份': 2017, '收入': 15.6},
        {'年份': 2018, '收入': 17.9},
        {'年份': 2019, '收入': 23.4},
        {'年份': 2020, '收入': 18.6}
       ]

# 列表推导式，将字典中的年份和收入分别存储在两个列表中
year = [str(item['年份']) for item in data]
income = [item['收入'] for item in data]

# 绘制折线图
# plot() 函数的参数是一个列表，列表中的元素是 x 轴和 y 轴的数据，color 参数是线条的颜色，marker 参数是数据点的标记，linestyle 参数是线条的样式
plt.plot(year, income, color='green', marker='o', linestyle='solid')
# 设置图表的标题和坐标轴的标签
# title() 函数的参数是图表的标题，xlabel() 函数的参数是 x 轴的标签，ylabel() 函数的参数是 y 轴的标签
plt.title('收入情况')
plt.xlabel('年份')
plt.ylabel('万元')
# 显示图表
plt.show()