import pandas as pd

data = {
    '语文': [90, 98, 87, 90],
    '数学': [92, 87, 90, 98]
}

# 创建 DataFrame 对象，行索引为指定的列表，列索引为字典的键
df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
# 计算语文最高分
yuwen_series = df['语文']
# 语文最高分，使用 max() 方法
max_yuwen = yuwen_series.max()
# format() 方法用于格式化字符串，{max_score} 是占位符，用于接收 max_yuwen 的值
print('语文最高分{max_score}'.format(max_score=max_yuwen))

# 创建出总分列, 由每一行的语文和数学分数相加
df['总分'] = df['语文'] + df['数学']
# 计算总分最高分
# max() 方法返回的是最大值，即总分最高分
max_sum = df['总分'].max()
# 计算总分最高的学生
# idxmax() 方法返回的是最大值所在的索引，即总分最高的学生姓名
# 注意，idxmax() 方法返回的是索引，而不是值，所以需要通过索引获取值
stu_name = df['总分'].idxmax()
# 格式化输出总分最高的学生姓名和总分
# format() 方法用于格式化字符串，{stu} 是占位符，用于接收 stu_name 的值，{score} 是占位符，用于接收 max_sum 的值
print('{stu}总分最高, {score}'.format(stu=stu_name, score=max_sum))